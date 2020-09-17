from flask import Flask, request, render_template
from flask_cors import CORS
from sqltest import insert, insert_test
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

DBCONFIG = os.environ["ConnectionString"]

@app.route("/")
def hello():
    return DBCONFIG


@app.route('/courselist', methods=['POST'])
def connectDB():
    print(request.data.decode('utf-8'))
    print(type(request.data))
    insert(DBCONFIG)
    return "connect db"

@app.route('/test', methods=['POST'])
def connectDBtest():
    print(request.data.decode('utf-8'))
    print(type(request.data))
    insert_test(DBCONFIG)
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
