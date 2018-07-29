from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/ali.json',"EsZxVyS4rBs9tF5Ah19e.8z3xzSZpaY6UpMbZlM4/tG.XptFMErmZ+oHhgk7joc3zf+n+ndBQGKUzND7CyOa5Qo=")