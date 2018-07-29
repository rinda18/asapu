from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/hendra.json',"EtS7vwQ730VXGGu4CCz5.YNkPcGC5L3sZws6OyWZ6Lq.todeksoUlU7YRRis3oYaaNw+K5z5pZrNfU/QCkzTt+E=")