import mongoose from "mongoose";
mongoose.pluralize(null);

export default (() => {
  return mongoose.createConnection(
    "mongodb://root:a4b53c60efc39e8dee2babae77d8d81351df545149db32fec48730a9f4c33d7f@mongo:27018/app?connectTimeoutMS=1000&authSource=admin",
    (err) => (!err ? console.log("sukses") : console.log("error", err))
  );
})();
