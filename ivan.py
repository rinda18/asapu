# -*- coding: utf-8 -*-
from Dit.linepy import *
from datetime import datetime, timedelta, date
from bs4 import BeautifulSoup
from akad.ttypes import *
from multiprocessing import Pool, Process
import time,random,sys,json,codecs,urllib,urllib3,requests,threading,glob,os,subprocess,multiprocessing,re,ast,shutil,calendar,tempfile,string,six,timeit
from random import randint

mulas = time.time()
try:
    cl = LINE('Et1cmvAsw4sPpYIDFCNf.vHMGDT0SW7g5aNnhGgXWNW.EQR+QWlmDtHblpSmDM5En3P/lOR5xHoUzAP6qvDaC9k=')
except:
    cl = LINE()
clientPoll = OEPoll(cl)
groupParam = ""
def crot(targ):
    cl.kickoutFromGroup(groupParam,[targ])
def bot(op):
    global groupParam
    if op.type == 25:
        msg = op.message
        text = msg.text
        msg_id = msg.id
        to = msg.to
        saya = msg._from
        if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
            if msg.toType == 0:
                if saya != cl.getProfile().mid:
                    to = saya
                else:
                    to = msg.to
            elif msg.toType == 1:
                to = msg.to
            elif msg.toType == 2:
                to = msg.to
            if msg.contentType == 0:
                if text.lower().startswith('mayhem'):
                    a = []
                    b = cl.getGroup(msg.to)
                    for i in b.members:
                        if i.mid not in [saya]:
                            a.append(i.mid)
                    cl.sendMessage(msg.to," 「 Mayhem 」\nMayhem is STARTING♪\n'abort' to abort♪""")
                    cl.sendMessage(msg.to," 「 Mayhem 」\n %i victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/" % len(a))
                    for target in a:
                        groupParam = msg.to
                        try:
                            p = Pool(40)
                            p.map(crot,a)
                            p.close()
                            p.terminate()
                            p.join
                            Refresh()
                        except Exception as error:
                            p.close()
                            return
                if text.lower().startswith('hmm '):
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                            groupParam = msg.to
                            try:
                                p = Pool(40)
                                p.map(crot,targets)
                                p.close()
                                p.terminate()
                                p.join
                                Refresh()
                            except Exception as error:
                                p.close()
                                return

while True:
    try:
      ops = clientPoll.singleTrace(count=50)
      if ops is not None:
          for op in ops:
            bot(op)
            clientPoll.setRevision(op.revision)
    except Exception as error:
        print(error)