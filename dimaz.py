from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/dimaz.json',"EsskTmKYEx2tGFQdzArf.8chI+jrWQyuJ80iogofxJW.CyQS3c+qwOlEKYCPJXl+AVYsyIepVtLn8bNZsHiBbHA=")