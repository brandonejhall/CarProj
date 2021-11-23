from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#initialize Flask application
app = Flask('__name__')
    
app.config.from_object(Config)
#WebForm Protection
app.config['SECRET_KEY'] = 'you-will-never-guess'
    
#Blueprint registrating
from app.student_user.routes import student
app.register_blueprint(student)

#database intialization
db = SQLAlchemy(app)

migrate = Migrate(app, db)
    
