from dit import LineBot
import json,threading,subprocess
def login(resp, auth):
    bot = LineBot(resp, auth)
w1 = login('protect/@Ａｌ!.json',"EtL9sl4NalBxFLZBFgqe.8z3xzSZpaY6UpMbZlM4/tG.+y/IjM3zjjTEeKtBe/p41oQvmCgWe/WlgkV93RwfaeI=")