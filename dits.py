from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/dits.json',"Ev7NsZpbtAStY3iwZXT3.m7QAK9mmg/fv3Yt11op1GW.ndlfVGqRprpqG64XDjtVS8Go/7Xa+eWUzobUAWvthyk=")