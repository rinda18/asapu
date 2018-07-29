from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/deni.json',"Esx2Qoirqrj6zpSdZbaf.bOX8nyp7/gSpRWAVs2MCxW.ud/AtYHvKakfkDtCWFc6mxLrIT2OqXB1KXRKjFsx0yg=")