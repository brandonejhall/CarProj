from flask import Blueprint, render_template

student = Blueprint('student',__name__,template_folder='templates')

@student.route('/', methods = ['GET'])
def index():
    return render_template('index.html')