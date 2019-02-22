from flask import Flask
from.api.Blueprint_one import item
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.register_blueprint(user,url_prefix="/api/v2/item")