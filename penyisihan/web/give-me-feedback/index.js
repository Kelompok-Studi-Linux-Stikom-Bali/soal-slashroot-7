import express from "express";
import { runBot } from './bot.js';
import path from "path";
import { fileURLToPath } from "url";
import bodyParser from "body-parser";

const app = express()
const port = 3000

app.set('view engine', 'ejs');
app.use( bodyParser.json() );       
app.use(bodyParser.urlencoded({     
  extended: true
})); 

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.set('views', path.join(__dirname, 'views'));

app.get('/', (req, res) => {
    res.render('index');
})
app.get('/feedback', (req, res) => {
    res.render('feedback',{message: req.query?.message});
})
app.post('/feedback', (req, res) => {
    if(req.body?.feedback !== null){
        runBot(req.body?.feedback);
    }
    res.redirect('/feedback?message='+req.body?.feedback);
})
app.get('/gallery', (req, res) => {
    res.render('gallery');
})

app.get('/test', (req, res) => {
    runBot();
    res.send('a')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})