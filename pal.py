from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/pal.json',"EseQb9zPM1nPjv8i6Hw9./yI1KGKbiV0aal1vgp3PMq.8NrBEd+rImkfNSsl3mAaS7obY6rLFwktIjMoRqtHIkM=")