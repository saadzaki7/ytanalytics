from flask import Flask

from . import db

class Movie(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(50))
    videoNum = db.Column(db.Integer)
    channelName = db.Column(db.String(50))
    channelPhoto = db.Column(db.String(50))
    channelViews =db.Column(db.Integer)
    comments =db.Column(db.Integer)
    country=db.Column(db.String(50))
    likes=db.Column(db.Integer)
    subscribers=db.Column(db.Integer)
    thumbnail=db.Column(db.String(50))
    videoViews=db.Column(db.Integer)

