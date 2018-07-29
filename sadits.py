from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/sadits.json',"EtPEZziu57nHwDnKsau5.KrPt8yQdP/+TF5zhsG0CDq.1Iu2993ohL4ZrX97K5jlFBU8F+KFF4XbOiLwDdbgx3o=")