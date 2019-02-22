from flask import Blueprint

course = Blueprint('course', __name__, template_folder='templates')

course_list =['INF320', 'COS350', 'COS224',]


@course.route('/')

#def show():
   # return "I am a blueprint" 

def course_list():
    return render_template("index.html", course = course_list)

