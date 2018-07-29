# -*- coding: utf-8 -*-
from Dit.linepy import *
from akad.ttypes import *
import time,json,os,sys,ast,humanize,subprocess
from datetime import datetime, timedelta, date

try:
    line = LINE('peki.n1@yahoo.com','memek.mu1',appName='IOSIPAD\t7.14.0\tANBOT\tTools\t10.12.0')
except:
    line = LINE()
#line = LINE('AUTHTOKEN')

line.log("Auth Token : " + str(line.authToken))
squareChatMid= ['m6355594d3dbfc490ebcfbd49546d5c33','m8753b6f1191852bb6b46bf93ebbb257a','md9ed3dadf378673f23c26423f16d0123','m88673ee2a47094eb714724f84aa1c53c']
# Initialize OEPoll with LINE instance
oepoll = OEPoll(line)

wait = {'setTime':{},'readPoint':{},'ROM1':{},'msg.id':'','tagall':{}}

def sendMention(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@ADIT GANTENG "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:
                    if h.count('U0') % 2 == 0:slen = len(textx)-(h.count('U0')//2);elen = (len(textx)-(h.count('U0')//2)) + 13
                    elif h.count('U0') % 3 == 0:slen = len(textx)-(h.count('U0')//3);elen = (len(textx)-(h.count('U0')//3)) + 13
                    else:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        line.sendSquareMessage(to, textx,{'AGENT_LINK': 'line://ti/p/~meguminthemirror','AGENT_ICON': '','AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def anulurk(msg,wait):
        to = msg.to
        moneys = {}
        for a in wait["setTime"][to].items():
            moneys[a[1]] = [a[0]] if a[1] is not None else idnya
        sort = sorted(moneys)
        sort = sort[0:]
        k = len(sort)//100
        for a in range(k+1):
            if a == 0:no= a;msgas = '╭「 Lurkers 」─'
            else:no = a*100;msgas = '├「 Lurkers 」─'
            h = []
            for i in sort[a*100 : (a+1)*100]:
                h.append(moneys[i][0])
                no+=1
                a = '{}'.format(humanize.naturaltime(datetime.fromtimestamp(i)))
                if no == len(sort):msgas+='\n│{}. @!\n╰    「 {} 」'.format(no,a)
                else:msgas+='\n│{}. @!\n│    「 {} 」'.format(no,a)
            try:
                sendMention(to, msgas,'', h)
            except Exception as e:print(e)
susi = []
while True:
    try:
        for asw in squareChatMid:
            try:
                eventsSquareChat=oepoll.singleFetchSquareChat(squareChatMid=asw)
                for e in eventsSquareChat:
                    if e.payload.notifiedMarkAsRead != None:
                        pp = e.payload.notifiedMarkAsRead
                        if pp.squareChatMid not in wait['tagall']:wait['tagall'][pp.squareChatMid] = []
                        if pp.sMemberMid in wait['tagall'][pp.squareChatMid]:pass
                        else:wait['tagall'][pp.squareChatMid].append(pp.sMemberMid)
                        try:
                            if pp.squareChatMid in wait['readPoint']:
                                if wait['readPoint'][pp.squareChatMid]:
                                    if pp.sMemberMid in wait['ROM1'][pp.squareChatMid]:
                                        wait['setTime'][pp.squareChatMid][pp.sMemberMid] = time.time()
                                    else:
                                        wait['ROM1'][pp.squareChatMid][pp.sMemberMid] = pp.sMemberMid
                                        wait['setTime'][pp.squareChatMid][pp.sMemberMid] = time.time()
                        except Exception as e:print(e)
                    if e.createdTime is not 0:
                        ts_old = int(e.createdTime) / 1000
                        ts_now = int(time.time())
                        if ts_old >= ts_now:
                            if e.payload.sendMessage != None:
                                payload=e.payload.sendMessage
                                msg=payload.squareMessage.message
                                msg_id=msg.id
                                receiver_id=msg._from
                                sender_id=msg.to
                                asem = [msg_id]
                                to = msg.to
                                if msg.contentType == 0:
                                    text = msg.text
                                    if text.lower() == 'renew':
                                        os.system('clear')
                                        line.sendSquareMessage(msg.to," 「 Restarting 」\nType: Restart Program\nRestarting...")
                                        python = sys.executable
                                        os.execl(python, python, * sys.argv)
                                    if text.lower() == '..':
                                        print(line.getSquareMembers(msg._from))
                                    if text.lower() == "lurk result":
                                        if to in wait['readPoint']:
                                            try:
                                                anulurk(msg,wait)
                                                wait['setTime'][to]  = {};wait['readPoint'][to] = msg.id
                                            except Exception as e:print(e);line.sendSquareMessage(msg.to,'╭「 Lurkers 」─\n╰ None')
                                        else:line.sendSquareMessage(msg.to, " 「 Lurk 」\nLurk point not on♪")
                                    if msg.text.lower() == "lurk off":
                                        if msg.to not in wait['readPoint']:
                                            line.sendSquareMessage(msg.to, " 「 Lurk 」\nLurk already off♪")
                                        else:
                                            try:
                                               del wait['readPoint'][to];wait['setTime'][to] = {};wait['ROM1'][to] = {}
                                            except:
                                               pass
                                            line.sendSquareMessage(to, " 「 Lurk 」\nLurk point off♪")
                                    if msg.text.lower() == "lurk on":
                                        if to in wait['readPoint']:
                                            line.sendSquareMessage(to, " 「 Lurk 」\nLurk already set♪")
                                        else:
                                            try:
                                                del wait['readPoint'][to];del wait['setTime'][to]
                                            except:
                                                pass
                                            wait['readPoint'][to] = msg.id;wait['setTime'][to]  = {};wait['ROM1'][to] = {};wait['msg.id'] = msg.id
                                            line.sendSquareMessage(to, " 「 Lurk 」\nLurk point set♪")
                                    if text.lower() == 'tagall':
                                        for a in wait['tagall'][msg.to]:
                                            h = line.getSquareMemberRelation('sc3e2d4f85535b7a50a4e21a821023e4f', a).relation.state
                                            if int(h) == 2:wait['tagall'][msg.to].remove(a)
                                        k = len(wait['tagall'][msg.to])//200
                                        for aa in range(k+1):
                                            if aa == 0:dd = '╭「 {} 」─'.format('Mention');no=aa
                                            else:dd = '├「 {} 」─'.format('Mention');no=aa*200
                                            msgas = dd
                                            for i in wait['tagall'][msg.to][aa*200 : (aa+1)*200]:
                                                no+=1
                                                if no == len(susi):msgas+='\n╰{}. @!'.format(no)
                                                else:msgas+='\n│{}. @!'.format(no)
                                            try:
                                                sendMention(to=msg.to, text=msgas,ps='', mids=wait['tagall'][msg.to][aa*200 : (aa+1)*200])
                                            except Exception as e:print(e)
            except:
                pass
    except Exception as e:
    	line.log("[FETCH_SQUARE] Fetch square chat error: " + str(e))