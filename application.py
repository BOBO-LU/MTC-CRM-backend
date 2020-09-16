from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/p', methods=['POST'])
def connectDB():
    print('connect db')
    return "connect db"

# from flask import Flask, request, render_template
# from flask_cors import CORS
# from sqltest import insert
# from config import DefaultConfig

# app = Flask(__name__)
# app.config["DEBUG"] = True
# CORS(app)

# CONFIG = DefaultConfig()


# @app.route('/', methods=['GET'])
# def home():

#     print('get')
#     # insert(CONFIG)
#     return "<h1>Hello Flask!</h1>"


# @app.route('/p', methods=['POST'])
# def connectDB():
#     print('connect db')
#     # print(request.data)
#     return "connect db"

# # if __name__ == "__main__":
# #     app.run()
