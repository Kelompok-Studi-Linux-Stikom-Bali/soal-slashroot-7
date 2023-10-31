import express from "express";
import path from "path";
import { auth, complain } from "./model.js";
import cookieParser from "cookie-parser";
import * as find from "./find.js";
import { v4 } from "uuid";
import { runBot } from "./bot.js";
import sanitize from "mongo-sanitize";
import helmet from "helmet";
import { fileURLToPath } from "url";

// let admin;
let timeReset = Math.floor(new Date().getTime() / 1000 + 60 * 5); // 5 minutes

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const checkAdmin = await find.one({ role: "admin" }, auth);

if (!checkAdmin) {
  auth.create(
    {
      name: "admin",
      username: "admin",
      password:
        "75918197d351421efc2b52a4fdfbe165de3ca6ff7a37090e7ca539bbeb92656e",
      role: "admin",
    },
    (err) => {
      if (err) console.log(err);
    }
  );
}

const app = express();

app.set("view engine", "ejs");

app.use(
  helmet({
    contentSecurityPolicy: {
      directives: {
        "default-src": ["'self'"],
        "script-src": ["'self'", "'unsafe-inline'"],
        upgradeInsecureRequests: null,
      },
    },
  })
);

app.use(express.static(path.join(path.resolve(__dirname, "./public"))));

app.use(cookieParser());

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// reset all
app.use(async ({ next }) => {
  const now = Math.floor(new Date().getTime() / 1000);
  if (timeReset <= now) {
    await complain.deleteMany({});
    timeReset = now + 100;
  }
  next();
});

app.use((req, _, next) => {
  Object.keys(req.body).map((e) => {
    req.body[e] = sanitize(req.body[e]);
  });
  next();
});

app.use(async (req, res, next) => {
  const token = req.cookies["cook-token"] || undefined;
  const options = { maxAge: 900000, httpOnly: false };

  const now = Math.floor(new Date().getTime() / 1000);

  if (!token) {
    res.cookie("cook-token", v4());
  } else {
    const data = await find.one({ "token.v4": sanitize(token) }, auth);
    if (data) {
      options.httpOnly = true;
      req.body.self = data;
      res.cookie("cook-token", data.token.v4, options);
      if (data.token.expires < now) {
        res.clearCookie("cook-token");
        delete req.body?.self;
      }
    }
  }
  next();
});

app.get("/logout", (_, res) => {
  res.clearCookie("cook-token");
  delete res.body?.self;
  return res.redirect("back");
});

// get flag
app.get("/getFlag", async (req, res) => {
  if (req.body?.self) {
    if (req.body.self.role === "admin") {
      return res.send(
        "slashroot7{forgot_set_some_filter_before-so_it_must_be_harder_right?}"
      );
    }
  }
  return res.redirect("/welcome");
});

// complain
app.get("/complain/:username", async (req, res) => {
  const username = req.params.username;
  let stringData = "";
  if (req.body?.self) {
    if (req.body.self.role === "admin") {
      stringData = `<h1>${username} Complains</h1><ol>`;
      const data = await complain.find({ username });
      if (data) {
        for (let dat of data) {
          stringData += "<li>" + dat.complain + "</li>";
        }
      } else {
        return res.send("empty");
      }
    } else {
      if (req.body.self.username !== username){
        return res.end("user not allowed!");
      }
      const complains = await find.multiple({ username }, complain);
      const action = req.query.action;
      if (action === "clear") {
        await complain.deleteMany({ username });
        return res.redirect("/welcome?success=" + 1);
      }
      stringData = `<h1>My Complains</h1><ol>`;
      if (complains) {
        for (let dComp of complains) {
          stringData += "<li>" + dComp.complain + "</li>";
        }
      } else {
        return res.send("empty");
      }
    }
  } else {
    return res.sendStatus(500);
  }
  stringData += "</ol>";
  return res.send(stringData);
});

// set complain
app.post("/complain", async (req, res) => {
  try {
    if (req.body?.self) {
      const { username, role } = req.body.self;

      if (role !== "admin") {
        let com = req.body?.complain || ""

        if (com.length > 550) {
          return res.redirect("/welcome?failed=2.2");
        }

        

        if (/fetch|XMLHttp|['",.:`]/gi.test(com)) {
          return res.redirect("/welcome?failed=2.3");
        }

        await complain.find({ username }, async (err, data) => {
          if (err) throw err;
          if (data) {
            if (data.length > 0) {
              await complain.deleteMany({ username });
              return res.end("You've given too many complaints to the admin!");
            }
          }
        }).clone()

        const crData = {
          username,
          complain: com,
        };

        await complain.create(crData);

        runBot(username).catch(async (err) => {
          console.log(err);
          await complain.deleteMany({ username });
        });
      } else {
        return res.redirect("/");
      }

      return res.redirect("/welcome?success=" + 2);
    }
    return res.redirect("/welcome");
  } catch (err) {
    // return res.status(500).end(err);
    console.log(req.body.self);
    return res.status(200).json({error:err});
  }
});

app.get("/", (req, res) => {
  if (req.body?.self) {
    return res.redirect("/welcome");
  }
  return res.render("index");
});

app.get("/register", (_, res) => {
  return res.render("regis", { msg: false });
});

app.post("/register", async (req, res) => {
  if (req.body?.name && req.body?.username && req.body?.password) {
    const check = await find.one({ username: req.body.username }, auth);
    if (!check) {
      auth.create(
        {
          name: req.body.name,
          username: req.body.username,
          password: req.body.password,
        },
        (err) => {
          if (err) return res.send(err);
        }
      );
      return res.render("regis", { msg: 1 });
    }
    return res.render("regis", { msg: 2 });
  }
  return res.render("regis", { msg: 3 });
});

app.post("/login", async (req, res) => {
  const { username, password } = req.body;
  let err = "Empty fields are not allowed!";

  if (username && password) {
    const update = {
      token: {
        v4: req.cookies["cook-token"],
        expires: Math.floor(new Date().getTime() / 1000) + 84000,
      },
    };

    const data = await find.oneUpdate({ username, password }, update, auth);
    if (data) {
      return res.redirect("/welcome");
    }
    err = "Invalid username or password!";
  }
  return res.render("index", { err });
});

app.get("/welcome", async (req, res) => {
  if (req.body?.self) {
    const { name, role } = req.body.self;
    const msg = req.query?.success || req.query?.failed;
    return res.render("welcome", { role, name, msg });
  }
  return res.redirect("/");
});

app.use((_, res) => res.sendStatus(404));
const port = 21204;
app.listen(port, () => console.log(`listening on port ${port}`));
