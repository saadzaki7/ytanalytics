from flask import Blueprint, jsonify, request
from flask.wrappers import Request
from google.auth.transport import Request
from googleapiclient.discovery import build
import urllib
from urllib.parse import urlparse
from . import db
from .models import Movie


main = Blueprint('main',__name__)

@main.route('/')
def hello():
    return "Hello to the World!"

@main.route('/search')
def add_movies():
    
    urlTest=request.args.get('url')
    key= 'AIzaSyAtVn2x_uZnGcdEX5o-Ldz6PTR4vrKc61Y'

    youtube = build('youtube', 'v3', developerKey=key)
    inputedUlr=urlTest
    VidId=(((urllib.parse.parse_qsl(inputedUlr))[0])[1])


    request2= youtube.videos().list(part='statistics', id=VidId)
    vidStat= request2.execute()

    request3=youtube.videos().list(part='snippet', id=VidId)
    vidSnippet= request3.execute()

    # How to extract channelid from video
    channelId = ((((vidSnippet['items'])[0])['snippet'])['channelId'])

    request4= youtube.channels().list(part='statistics',id=channelId)
    channelStat=request4.execute()

    # How to get channel thumbnail photo
    request5= youtube.channels().list(part='snippet',id=channelId)
    channelSnippet=request5.execute()

    ans= {
    "Title:": (((((vidSnippet['items'])[0])['snippet'])['title'])),
    "Channel Name:": (((((vidSnippet['items'])[0])['snippet'])['channelTitle'])),
    "Thumnail Link (medium size):": (((((((vidSnippet['items'])[0])['snippet']))['thumbnails'])['medium'])['url']),
    "Video Views:": (((vidStat['items'][0])['statistics'])['viewCount']),
    "Likes:":(((vidStat['items'][0])['statistics'])['likeCount']),
    "Comments:":(((vidStat['items'][0])['statistics'])['commentCount']),
    "Channel Views:": (((channelStat['items'][0])['statistics'])['viewCount']),
    "Subscribers:": (((channelStat['items'][0])['statistics'])['subscriberCount']),
    "# of Video:": (((channelStat['items'][0])['statistics'])['videoCount']),
    "Channel Photo Link (medium size):":((((((channelSnippet['items'])[0])['snippet'])['thumbnails'])['medium'])['url']),
    "Country:":((((((channelSnippet['items'])[0])['snippet'])['country'])))
    }
    new_movie= Movie(title=ans["Title:"], videoNum=ans["# of Video:"],
    channelName= ans["Channel Name:"],
    channelPhoto = ans["Channel Photo Link (medium size):"],
    channelViews = ans["Channel Views:"],
    comments = ans["Comments:"],
    country= ans["Country:"],
    likes= ans["Likes:"],
    subscribers = ans["Subscribers:"],
    thumbnail= ans["Thumnail Link (medium size):"],
    videoViews= ans["Video Views:"]
    )
    db.session.add(new_movie)
    db.session.commit()

    return 'Done', 201
    
@main.route('/movies')
def movies():
    movie_list= Movie.query.all()
    movies=[]

    for movie in movie_list:
        movies.append({'title': movie.title, 'videoNum' : movie.videoNum,
        'channelName': movie.channelName,
        'channelPhoto': movie.channelPhoto,
        'channelViews': movie.channelViews,
        'comments': movie.comments,
        'country': movie.country,
        'subscribers': movie.subscribers,
        'thumbnail': movie.thumbnail,
        'videoViews': movie.videoViews})

    if (len(movies)>1):
        hold=movies[-1]
        movies=hold

    return jsonify({'movies':movies})