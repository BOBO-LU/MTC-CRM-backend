from flask import Flask, request, render_template
from flask_cors import CORS
from sqltest import insert, insert_test
from config import DefaultConfig
import os
app = Flask(__name__)



# app.config["DEBUG"] = True


# print('start app')
# try:
#     CORS(app)
# except Exception as e:
#     print('cors: ', e)

# print('start cors')

# try: 
#     DBCONFIG = os.environ["ConnectionString"]
# except Exception as e:
#     DBCONFIG = DefaultConfig()
#     print("dbconfig")

# print('get conneection string: ', DBCONFIG)


# @app.route("/")
def hello():
    print('start hello')
    print("DBCONFIG: ", DBCONFIG)
    return DBCONFIG


# @app.route('/courselist', methods=['POST'])
# def connectDB():
#     print('start connect DB')
#     print(request.data.decode('utf-8'))
#     print(type(request.data))
#     try:
#         insert(DBCONFIG)
#     except Exception as e:
#         print('connectDB error: ', e)
#     print('finish DB')
#     return "connect db"

# @app.route('/test', methods=['POST'])
# def connectDBtest():
#     print('start connect DB test')
#     print(request.data.decode('utf-8'))
#     print(type(request.data))
#     try:
#         insert_test(DBCONFIG)
#     except Exception as e:
#         print('connectDB error: ', e)
#     print('finsih DB test')
#     return "connect db"

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
