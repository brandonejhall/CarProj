from flask import Blueprint, render_template
from app.models import Appointments


student = Blueprint('student',__name__,template_folder='templates')


from app.student_user.forms import BookingForm

@student.route('/', methods = ['GET','POST'])
def index():
    form = BookingForm()
    if form.validate_on_submit():
        booking = Appointments()
    return render_template('index.html',title ='Sign In', form=form)