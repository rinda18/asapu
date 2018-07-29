from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/mekaku.json',"EtpMf4jchy403OSTEYo6.PDbdajMSOpGkuiWqQ+Pk5G.ZE6L0+t5t0/vNkcMnN2DJKIdHITCv8TPh1EZSnNqyX4=")