from google.auth.transport import Request
from googleapiclient.discovery import build
import urllib
from urllib.parse import urlparse


key= 'AIzaSyAtVn2x_uZnGcdEX5o-Ldz6PTR4vrKc61Y'

youtube = build('youtube', 'v3', developerKey=key)


inputedUlr=input("Url:")
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

# request = youtube.channels().list(part='statistics',id='UCCezIgC97PvUuR4_gbFUs5g')

# response= request.execute()





# print(response3)
# print(response2)
# print("")
# print(response)

# r1={'kind': 'youtube#channelListResponse', 'etag': 'UP4ZEYGyDsSgomjZSy7d7EGCd8s', 'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 'items': [{'kind': 'youtube#channel', 'etag': 'IzmdETOaIxT81D8Xfn9NgKnUhR0', 'id': 'UCCezIgC97PvUuR4_gbFUs5g', 'statistics': {'viewCount': '66527322', 'subscriberCount': '869000', 'hiddenSubscriberCount': False, 'videoCount': '230'}}]}

r2={'kind': 'youtube#videoListResponse', 'etag': 'dJG7b74pZSrgbQCifEhwqDvzD_4', 'items': [{'kind': 'youtube#video', 'etag': 'Zd9-dETqifKmkorLi_aVb91SKnw', 'id': 'fJJyrfkda4w', 'statistics': {'viewCount': '6444', 'likeCount': '44', 'favoriteCount': '0', 'commentCount': '11'}}], 'pageInfo': {'totalResults': 1, 'resultsPerPage': 1}}

r3={'kind': 'youtube#videoListResponse', 'etag': 'e2Dozvqtm8bSkzq9QgrIZ8BzX9I', 'items': [{'kind': 'youtube#video', 'etag': 'S5eEKDeGFprlhbrsO-axBq1vY1A', 'id': 'i_5xPDX-erE', 'snippet': {'publishedAt': '2020-11-18T14:45:02Z', 'channelId': 'UCvVZ19DRSLIC2-RUOeWx8ug', 'title': 'Extract YouTube Video Details in Python (using YouTube Data API)', 'description': 'In this Python tutorial, we are going to learn how to extract YouTube video information (title, tags, description, published date, statistics) using YouTube API (YouTube Data API).\n\nThe YouTube Data API lets your program to perform features normally you see on YouTube platform, and with YouTube Data API, we can customize our apps to automate and extraction information from YouTube.\n\n📃 Google.py Source Code: https://learndataanalysis.org/google-py-file-source-code/\n📃 Source Code: https://learndataanalysis.org/extract-youtube-video-info-using-youtube-data-api-in-python/\n📃 How to create and set up a Google Cloud project: https://youtu.be/6bzzpda63H0\n\nBuy Me a Coffee? Your support is much appreciated!\n----------------------------------------------------------------------------------------------------------------\nPayPal Me: https://www.paypal.me/jiejenn/5\nVenmo: @Jie-Jenn\nPatreon: https://www.patreon.com/JieJenn\n\nSupport my channel so I can continue making free contents\n----------------------------------------------------------------------------------------------------------------\nBy shopping on Amazon → https://amzn.to/2JkGeMD\nMore tutorial videos on my website → https://LearnDataAnalysis.org\nFollow Me on Facebook → https://www.facebook.com/Learn-Data-Analysis-101284561779059\nBusiness Inquiring: YouTube@LearnDataAnalysis.org\n\nTags:\n#YouTubeAPI #YouTubeDataAPI #Python', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/i_5xPDX-erE/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/i_5xPDX-erE/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/i_5xPDX-erE/hqdefault.jpg', 'width': 480, 'height': 360}, 'standard': {'url': 'https://i.ytimg.com/vi/i_5xPDX-erE/sddefault.jpg', 'width': 640, 'height': 480}, 'maxres': {'url': 'https://i.ytimg.com/vi/i_5xPDX-erE/maxresdefault.jpg', 'width': 1280, 'height': 720}}, 'channelTitle': 'Jie Jenn', 'tags': ['YouTubeAPI', 'YouTubeDataAPI', 'YT', 'ExtractVideoInfo', 'YouTube in Python'], 'categoryId': '27', 'liveBroadcastContent': 'none', 'defaultLanguage': 'en', 'localized': {'title': 'Extract YouTube Video Details in Python (using YouTube Data API)', 'description': 'In this Python tutorial, we are going to learn how to extract YouTube video information (title, tags, description, published date, statistics) using YouTube API (YouTube Data API).\n\nThe YouTube Data API lets your program to perform features normally you see on YouTube platform, and with YouTube Data API, we can customize our apps to automate and extraction information from YouTube.\n\n📃 Google.py Source Code: https://learndataanalysis.org/google-py-file-source-code/\n📃 Source Code: https://learndataanalysis.org/extract-youtube-video-info-using-youtube-data-api-in-python/\n📃 How to create and set up a Google Cloud project: https://youtu.be/6bzzpda63H0\n\nBuy Me a Coffee? Your support is much appreciated!\n----------------------------------------------------------------------------------------------------------------\nPayPal Me: https://www.paypal.me/jiejenn/5\nVenmo: @Jie-Jenn\nPatreon: https://www.patreon.com/JieJenn\n\nSupport my channel so I can continue making free contents\n----------------------------------------------------------------------------------------------------------------\nBy shopping on Amazon → https://amzn.to/2JkGeMD\nMore tutorial videos on my website → https://LearnDataAnalysis.org\nFollow Me on Facebook → https://www.facebook.com/Learn-Data-Analysis-101284561779059\nBusiness Inquiring: YouTube@LearnDataAnalysis.org\n\nTags:\n#YouTubeAPI #YouTubeDataAPI #Python'}, 'defaultAudioLanguage': 'en-US'}}], 'pageInfo': {'totalResults': 1, 'resultsPerPage': 1}}

r4={'kind': 'youtube#channelListResponse', 'etag': 'fcAOndd7JKxNsSHP-L-WuPnwuGQ', 'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 'items': [{'kind': 'youtube#channel', 'etag': 'wnZWi18CPahycL7Q1bs181y-fls', 'id': 'UCvVZ19DRSLIC2-RUOeWx8ug', 'statistics': {'viewCount': '10375540', 'subscriberCount': '33300', 'hiddenSubscriberCount': False, 'videoCount': '908'}}]}

r5={'kind': 'youtube#channelListResponse', 'etag': 'ENsF8wwcpiH4TYG-OyRuoZ58AMc', 'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 'items': [{'kind': 'youtube#channel', 'etag': 'BG4Hlm49LkISyi8foWLdG8jIXew', 'id': 'UCvVZ19DRSLIC2-RUOeWx8ug', 'snippet': {'title': 'Jie Jenn', 'description': 'Just an average guy who enjoys data analysis and solve business problems.\n\nAbout Me:\nI am a self-taught data analyst/application developer (my first job was working as an Accountant, and almost got my CPA, but got sidetracked to focus on learning VBA), who learned everything through books, free tutorials, forum postings, and lots of practices and mistakes. In my channel you will find tutorials for Python (Data Analytics, Pandas, PyQt5 Development, Automation Scripts, Web Scraping, Google APIs, and many other things), Excel (including VBA), SQL, and other applications/software like Salesforce, Access, Outlook, etc.\n\nFor any question, please email\nYouTube@LearnDataAnalysis.org', 'customUrl': 'jiejenn', 'publishedAt': '2007-01-01T22:30:06Z', 'thumbnails': {'default': {'url': 'https://yt3.ggpht.com/ytc/AKedOLQr39FGEavhuhXz7Mxw7JmVFPY_ZbXdV8eAECJLCD0=s88-c-k-c0x00ffffff-no-rj', 'width': 88, 'height': 88}, 'medium': {'url': 'https://yt3.ggpht.com/ytc/AKedOLQr39FGEavhuhXz7Mxw7JmVFPY_ZbXdV8eAECJLCD0=s240-c-k-c0x00ffffff-no-rj', 'width': 240, 'height': 240}, 'high': {'url': 'https://yt3.ggpht.com/ytc/AKedOLQr39FGEavhuhXz7Mxw7JmVFPY_ZbXdV8eAECJLCD0=s800-c-k-c0x00ffffff-no-rj', 'width': 800, 'height': 800}}, 'localized': {'title': 'Jie Jenn', 'description': 'Just an average guy who enjoys data analysis and solve business problems.\n\nAbout Me:\nI am a self-taught data analyst/application developer (my first job was working as an Accountant, and almost got my CPA, but got sidetracked to focus on learning VBA), who learned everything through books, free tutorials, forum postings, and lots of practices and mistakes. In my channel you will find tutorials for Python (Data Analytics, Pandas, PyQt5 Development, Automation Scripts, Web Scraping, Google APIs, and many other things), Excel (including VBA), SQL, and other applications/software like Salesforce, Access, Outlook, etc.\n\nFor any question, please email\nYouTube@LearnDataAnalysis.org'}, 'country': 'US'}}]}
# print ('Channel Views:', (((r1['items'][0])['statistics'])['viewCount'] ))
# print ('Subscribers:', (((r1['items'][0])['statistics'])['subscriberCount'] ))
# # print ('# of Video:', (((r1['items'][0])['statistics'])['videoCount'] ))


# # Video calls
# print("\n\n")
# print('Video Views:',((vidStat['items'][0])['statistics'])['viewCount'])
# print('Likes:',((vidStat['items'][0])['statistics'])['likeCount'])
# print('Comments:',((vidStat['items'][0])['statistics'])['commentCount'])




# print("Title:", (((((vidSnippet['items'])[0])['snippet'])['title'])))
# print("Channel Name:", (((((vidSnippet['items'])[0])['snippet'])['channelTitle'])))
# print("Thumnail Link (medium size):", (((((((vidSnippet['items'])[0])['snippet']))['thumbnails'])['medium'])['url']))

# # request4= youtube.channels().list(part='statistics',id=channelId)
# # response4=request4.execute()
# # print(response4)

# print ('Channel Views:', (((channelStat['items'][0])['statistics'])['viewCount']))
# print ('Subscribers:', (((channelStat['items'][0])['statistics'])['subscriberCount']))
# print ('# of Video:', (((channelStat['items'][0])['statistics'])['videoCount']))

# # How to get channel thumbnail photo
# # request5= youtube.channels().list(part='snippet',id=channelId)
# # response5=request5.execute()
# # print(response5)

# print('Channel Photo Link (medium size):',((((((channelSnippet['items'])[0])['snippet'])['thumbnails'])['medium'])['url']))
# print('Country:',((((((channelSnippet['items'])[0])['snippet'])['country']))))


ans= {
    'Title:': (((((vidSnippet['items'])[0])['snippet'])['title'])),
    "Channel Name:": (((((vidSnippet['items'])[0])['snippet'])['channelTitle'])),
    "Thumnail Link (medium size):": (((((((vidSnippet['items'])[0])['snippet']))['thumbnails'])['medium'])['url']),
    'Video Views:': (((vidStat['items'][0])['statistics'])['viewCount']),
    'Likes:':(((vidStat['items'][0])['statistics'])['likeCount']),
    'Comments:':(((vidStat['items'][0])['statistics'])['commentCount']),
    'Channel Views:': (((channelStat['items'][0])['statistics'])['viewCount']),
    'Subscribers:': (((channelStat['items'][0])['statistics'])['subscriberCount']),
    '# of Video:': (((channelStat['items'][0])['statistics'])['videoCount']),
    'Channel Photo Link (medium size):':((((((channelSnippet['items'])[0])['snippet'])['thumbnails'])['medium'])['url']),
    'Country:':((((((channelSnippet['items'])[0])['snippet'])['country'])))
}
print(ans)

anstest={'Title:': 'Learn JSON in 10 Minutes', 'Channel Name:': 'Web Dev Simplified', 'Thumnail Link (medium size):': 'https://i.ytimg.com/vi/iiADhChRriM/mqdefault.jpg', 'Video Views:': '1558086', 'Likes:': '50525', 'Comments:': '1917', 'Channel Views:': '45405184', 'Subscribers:': '764000', '# of Video:': '379', 'Channel Photo Link (medium size):': 'https://yt3.ggpht.com/ytc/AKedOLQpvSjzSCSo8ZKCjBZS7TRX7omb_kyQirh2zgEY=s240-c-k-c0x00ffffff-no-rj', 'Country:': 'US'}