from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/aris.json',"EtZETCCJGR0ph0fzn20b.tAuuu6HhpsukESu3Ow756W.e6GYQ+dcKNfX9TSXclmd1aTqWW+IzNqx53j4dev8yMc=")