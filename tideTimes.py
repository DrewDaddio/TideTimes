from twython import Twython
import time
import sys

sys.path.insert(0, 'C:/users/Drew/PycharmProjects/TideTimes2/')

import config
import webSite


con = config.API_Key
con_s = config.API_Secret

acc = config.Access
acc_s = config.Access_Secret

twitter = Twython(con, con_s, acc, acc_s)

#def post():
#    while True:
#        twitter.update_status(status = message)
#        time.sleep(1800)  # Tweet every 30 minutes

#post()

beaches = webSite.beaches


def post():
    while True:
        for i, (k, v) in enumerate(beaches.items()):
            twitter.update_status(status=(v+k))
            time.sleep(600)

post()