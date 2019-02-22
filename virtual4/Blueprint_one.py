from flask import Blueprint

item = Blueprint('item', __name__, template_folder='templates')

@user.route('/')

def show():
    return "I am a blueprint"

