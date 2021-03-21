from flask import Flask
from app.request import get_users

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return {'user list': get_users()}
