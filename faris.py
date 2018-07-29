from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/faris.json',"Et7n7Si0nOGNUxx8RtD0.dlM1pJ6wV5W6JnBeTUGuua.JaDdMnFuEq8CSm8RDh/709T5taKgqV2GEJAwH2/kop4=")