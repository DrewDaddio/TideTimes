import tweepy
import time
import sys

#sys.path.insert(0, 'C:\Users\Drew\PycharmProjects\TideTimes2/')

import config
import webSite

message = print("Carlsbad, CA tide times - High tide will be at:" + webSite.high + '. Low tide will be at:' + webSite.low)

con = config.API_Key
con_s = config.API_Secret

acc = config.Access
acc_s = config.Access_Secret


auth = tweepy.OAuthHandler(con, con_s)
auth.set_access_token(acc, acc_s)
api = tweepy.API(auth)

api.update_status(message)
run = time.sleep(1800) #Tweet every 30 minutes