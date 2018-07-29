from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/wiliam.json',"Etbfv3DSmdKqnrZidQv0.gRR2cJn0HwHxI8+fMKdOOa.Eq1uXMDclhdDx3mp1CKbK4ETMVfdwxmDHXiEtg/JWmg=")