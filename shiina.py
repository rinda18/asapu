from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/shiina.json',"EtBNdHpIgnZDsBHIouF4.3XZflsnPnK5kmGHScxBjTa.eTCKODh0hPocEOK6AbkH44gYgEq37OS4uLDHLi6A2Tg=")