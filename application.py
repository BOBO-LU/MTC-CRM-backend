from flask import Flask
from flask_cors import CORS
# from sqltest import insert
# from config import DefaultConfig

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/p', methods=['POST'])
def connectDB():
    print('connect db')
    # print(request.data)
    return "connect db"
