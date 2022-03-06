from distutils.log import debug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'

db.init_app(app)
from .ytBackend import main
app.register_blueprint(main)


if __name__=="__main__":
    app.run(debug=True)