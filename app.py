import flask
from sqltest import insert
from config import DefaultConfig

app = flask.Flask(__name__)
app.config["DEBUG"] = True

CONFIG = DefaultConfig()


@app.route('/', methods=['GET'])
def home():

    print(' get ')
    insert(CONFIG)
    return "<h1>Hello Flask!</h1>"


@app.route('/', methods=['POST'])
def connectDB():
    print('connect db')
    return "connect db"


app.run()
