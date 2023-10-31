import mongoose from "mongoose";
import conn from "./conn.js";

const authSchema = new mongoose.Schema({
    username: String,
    password: String,
    name: String,
    token: {
        v4: String,
        expires: Number
    },
    role: {
        type: String,
        default: "user"
    }
})

const complainSchema = new mongoose.Schema({
    username: String,
    complain: String
})

export const auth = (() => {
    return conn.model("auths",authSchema);
})()
export const complain = (() => {    
    return conn.model("complains",complainSchema);
})()