from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/dhil.json',"EtLttuLYwFY3rv0sSFT2.Skq32mqBkuNH3J/isSmUaG.zecPyv9EcL01sho7Pptu180jMi3L0BaYbgk1NxKhHhg=")