from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.register_blueprint(user,url_prefix="/api/v1/user")