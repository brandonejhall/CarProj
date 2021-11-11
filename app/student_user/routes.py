from flask import Blueprint

student = Blueprint('student',__name__)

@student.route('/', methods = ['GET'])
def index():
    return 'working!'