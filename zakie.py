from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/zakie.json',"EtrpQu59QPFAzWDYfai4.yAOMXfpjVLzxa+KVcUGLfa.Ijl2auh0bI8NPBoWtsBWzMnlW7A8VHpzCQW05Z760J8=")