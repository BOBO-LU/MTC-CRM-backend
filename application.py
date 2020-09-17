from flask import Flask, request, render_template
from flask_cors import CORS
from sqltest import insert, insert_test
from config import DefaultConfig
import os
import logging
app = Flask(__name__)


logging.basicConfig(filename='flasklog.log', filemode='w')

app.config["DEBUG"] = True


logging.debug('start app')
try:
    CORS(app)
except Exception as e:
    logging.error('cors: ', e)

logging.debug('start cors')

try: 
    DBCONFIG = os.environ["ConnectionString"]
except Exception as e:
    DBCONFIG = DefaultConfig()
    logging.error("dbconfig")

logging.debug('get conneection string: ', DBCONFIG)


@app.route("/")
def hello():
    logging.debug('start hello')
    loggind.debug("DBCONFIG: ", DBCONFIG)
    return DBCONFIG


@app.route('/courselist', methods=['POST'])
def connectDB():
    logging.info('start connect DB')
    logging.debug(request.data.decode('utf-8'))
    logging.debug(type(request.data))
    try:
        insert(DBCONFIG)
    except Exception as e:
        logging.debug('connectDB error: ', e)
    logging.info('finish DB')
    return "connect db"

@app.route('/test', methods=['POST'])
def connectDBtest():
    logging.info('start connect DB test')
    logging.debug(request.data.decode('utf-8'))
    logging.debug(type(request.data))
    try:
        insert_test(DBCONFIG)
    except Exception as e:
        logging.debug('connectDB error: ', e)
    logging.info('finsih DB test')
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
