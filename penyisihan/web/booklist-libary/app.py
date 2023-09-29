from flask import Flask
from flask import request
import jwt
import json

app = Flask(__name__)

key = 'foo_444aa86e85a753b76fbd9eda8383e159_bar'

@app.route("/")
def home():
    HTMLFile = open('index.html','r')
    return HTMLFile.read()

@app.route("/api/login", methods=['POST'])
def login():
    payload = request.form
    if(str(payload.get('username')) == 'user' and str(payload.get('password')) == 'user123'):
        return jwt.encode({'admin': False},key,algorithm='HS256')
    return "invalid credentials"

@app.route("/api/book/list")
def bookList():
    result = []
    token = request.headers.get('Authorization')
    try:
        decodeData = jwt.decode(jwt=token,key=key,algorithms=["HS256"])
        booklistData = open('booklist.json','r')
        flag = open('flag.json','r')
        result.extend(json.loads(booklistData.read()))
        if(decodeData['admin']):
            result.extend(json.loads(flag.read()))
        return result
    except:
        return "Error"


if __name__ == "__main__":
    app.run(debug=True)