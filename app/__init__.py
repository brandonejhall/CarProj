from flask import Flask

#initialize Flask application
def career_app():
    app = Flask('__name__')

    from app.student_user.routes import student

    app.register_blueprint(student)
    return app