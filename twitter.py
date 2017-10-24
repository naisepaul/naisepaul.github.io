from watson_developer_cloud import VisualRecognitionV3
import json
from os.path import join, dirname
from os import environ
import urllib

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey='VHxFZvc25TzwHny9DJoXSRHPs'
csecret='gATpmrGr60ULBA2dErHUFMUsSLPFL06S9O99lHlxqArh83WgIp'
atoken= '826773320100102145-3zKgNs64oujlfR7LEDnzTldsPaR5Ve3'
asecret='h273vNnjbNqPe8xxpUyHVo252CHYoIVilRD2aFP3qj3LJ'

#key_word=raw_input("Enter The Key Word to Search : ")

class listener(StreamListener):
    def on_data(self,data):
        #print data
        profile_picture= data.split('"profile_image_url":"')[1].split('","profile_image_url_https":"')[0]
        for char in '[\]':
           profile_picture = profile_picture.replace(char, "")

       # print profile_picture
        visual_recognition = VisualRecognitionV3(api_key='54ffffe0834d6b4c548eec9c8f47eee1994e2b5a',version='2016-05-20')

        print(json.dumps(visual_recognition.detect_faces(images_url=profile_picture), indent=2))
        #x=(json.dumps(visual_recognition.detect_faces(images_url=profile_picture), indent=2))

        #y=json.loads(x)

       # print y["images"]["faces"]["gender"]
        '''for item in y:
            if item['gender'] is None: print "NA"
            else:  print item['gender']'''
        return True
    def on_error(selfself,status):
        print status

auth =OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream= Stream(auth,listener())
twitterStream.filter(track=['dublin'])



