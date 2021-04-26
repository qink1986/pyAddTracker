'''
Author: qink-dell
Date: 2021-04-03 10:26:42
LastEditors: qink-dell
LastEditTime: 2021-04-26 12:09:17
Description: 
'''

import subprocess
import os
import sys, getopt
import urllib.request
from getpass import getpass

class Torrent(object):
    tid = ''
    name = ''
    status = ''
    def __init__(self, tid, status, name):
        self.tid = tid
        self.status = status
        self.name = name
    
def getTorrent(user,password,host,filePath):
    if user:
        command = f'"{filePath}" "{host}" --auth={user}:{password} -l'
    else:
        command = f'"{filePath}" "{host}" -l'
    lstTorrents = ''

    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
    if ret.returncode == 0:
        lstTorrents = extractTorrents(ret.stdout)
    else:
        print(ret.stderr)
    return lstTorrents
    
def extractTorrents(torrentMsg):
    lstTorrents = []
    titleDict = {}
    torrentMsg = torrentMsg.split("\n")
    for line in torrentMsg:
        info = [i for i in line.strip(" ").split(" ") if i != ""]
        if len(info) > 0 and info[0] in ('ID'):
            for titie in info:
                titleDict[titie] = line.find(titie)
            continue
        if len(info) > 0 and len(titleDict) > 0 and info[0] != 'Sum:':
                lstTorrents.append(Torrent(line[0:titleDict['Done']].strip(" "), line[titleDict['Status']:titleDict['Name']].strip(" "), line[titleDict['Name']:].strip(" ")))
    return lstTorrents

def getTracker():
    try:
        url = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt"
        with urllib.request.urlopen(url) as f:
            trackers = [i.strip("'") for i in str(f.read())[1:].split("\\n") if i not in ("","'")]
    except:
        trackers = ['udp://tracker.opentrackr.org:1337/announce', 
                    'http://tracker.opentrackr.org:1337/announce', 
                    'udp://tracker.openbittorrent.com:6969/announce', 
                    'udp://exodus.desync.com:6969/announce', 
                    'udp://www.torrent.eu.org:451/announce', 
                    'udp://tracker.torrent.eu.org:451/announce', 
                    'udp://tracker.tiny-vps.com:6969/announce', 
                    'udp://retracker.lanta-net.ru:2710/announce', 
                    'udp://open.stealth.si:80/announce', 
                    'udp://valakas.rollo.dnsabr.com:2710/announce', 
                    'udp://opentracker.i2p.rocks:6969/announce', 
                    'udp://opentor.org:2710/announce', 
                    'http://opentracker.i2p.rocks:6969/announce', 
                    'udp://tracker.moeking.me:6969/announce', 
                    'udp://ipv4.tracker.harry.lu:80/announce', 
                    'udp://explodie.org:6969/announce', 
                    'http://explodie.org:6969/announce', 
                    'udp://zephir.monocul.us:6969/announce', 
                    'udp://wassermann.online:6969/announce', 
                    'udp://vibe.community:6969/announce', 
                    'udp://us-tracker.publictracker.xyz:6969/announce', 
                    'udp://udp-tracker.shittyurl.org:6969/announce', 
                    'udp://u.wwwww.wtf:1/announce', 
                    'udp://tsundere.pw:6969/announce', 
                    'udp://tracker2.dler.org:80/announce', 
                    'udp://tracker1.bt.moack.co.kr:80/announce', 
                    'udp://tracker0.ufibox.com:6969/announce', 
                    'udp://tracker.zerobytes.xyz:1337/announce', 
                    'udp://tracker.zemoj.com:6969/announce', 
                    'udp://tracker.v6speed.org:6969/announce', 
                    'udp://tracker.uw0.xyz:6969/announce', 
                    'udp://tracker.theoks.net:6969/announce', 
                    'udp://tracker.swateam.org.uk:2710/announce', 
                    'udp://tracker.skyts.net:6969/announce', 
                    'udp://tracker.shkinev.me:6969/announce', 
                    'udp://tracker.nrx.me:6969/announce', 
                    'udp://tracker.nighthawk.pw:2052/announce', 
                    'udp://tracker.loadbt.com:6969/announce', 
                    'udp://tracker.lelux.fi:6969/announce', 
                    'udp://tracker.edkj.club:6969/announce', 
                    'udp://tracker.dler.org:6969/announce', 
                    'udp://tracker.blacksparrowmedia.net:6969/announce', 
                    'udp://tracker.army:6969/announce', 
                    'udp://tracker.altrosky.nl:6969/announce', 
                    'udp://tracker.0x.tf:6969/announce', 
                    'udp://tr2.ysagin.top:2710/announce', 
                    'udp://tr.cili001.com:8070/announce', 
                    'udp://torrentclub.online:54123/announce', 
                    'udp://t3.leech.ie:1337/announce', 
                    'udp://t2.leech.ie:1337/announce', 
                    'udp://t1.leech.ie:1337/announce', 
                    'udp://retracker.sevstar.net:2710/announce', 
                    'udp://retracker.netbynet.ru:2710/announce', 
                    'udp://qg.lorzl.gq:2710/announce', 
                    'udp://public.tracker.vraphim.com:6969/announce', 
                    'udp://public.publictracker.xyz:6969/announce', 
                    'udp://public-tracker.zooki.xyz:6969/announce', 
                    'udp://open.publictracker.xyz:6969/announce', 
                    'udp://newtoncity.org:6969/announce', 
                    'udp://nagios.tks.sumy.ua:80/announce', 
                    'udp://mts.tvbit.co:6969/announce', 
                    'udp://movies.zsw.ca:6969/announce', 
                    'udp://mail.realliferpg.de:6969/announce', 
                    'udp://inferno.demonoid.is:3391/announce', 
                    'udp://free.publictracker.xyz:6969/announce', 
                    'udp://free-tracker.zooki.xyz:6969/announce', 
                    'udp://fe.dealclub.de:6969/announce', 
                    'udp://engplus.ru:6969/announce', 
                    'udp://edu.uifr.ru:6969/announce', 
                    'udp://drumkitx.com:6969/announce', 
                    'udp://discord.heihachi.pw:6969/announce', 
                    'udp://cutiegirl.ru:6969/announce', 
                    'udp://code2chicken.nl:6969/announce', 
                    'udp://cdn-2.gamecoast.org:6969/announce', 
                    'udp://cdn-1.gamecoast.org:6969/announce', 
                    'udp://camera.lei001.com:6969/announce', 
                    'udp://bubu.mapfactor.com:6969/announce', 
                    'udp://bt2.archive.org:6969/announce', 
                    'udp://bt1.archive.org:6969/announce', 
                    'udp://bioquantum.co.za:6969/announce', 
                    'udp://bclearning.top:6969/announce', 
                    'udp://app.icon256.com:8000/announce', 
                    'udp://admin.videoenpoche.info:6969/announce', 
                    'https://w.wwwww.wtf:443/announce', 
                    'https://trakx.herokuapp.com:443/announce', 
                    'https://tracker.tamersunion.org:443/announce', 
                    'https://tracker.sloppyta.co:443/announce', 
                    'https://tracker.nitrix.me:443/announce', 
                    'https://tracker.nanoha.org:443/announce', 
                    'https://tracker.lelux.fi:443/announce', 
                    'https://tracker.iriseden.eu:443/announce', 
                    'https://tracker.imgoingto.icu:443/announce', 
                    'https://tracker.hama3.net:443/announce', 
                    'https://tracker.foreverpirates.co:443/announce', 
                    'https://tracker.coalition.space:443/announce', 
                    'https://tr.ready4.icu:443/announce', 
                    'https://bt.nfshost.com:443/announce', 
                    'http://vps02.net.orel.ru:80/announce', 
                    'http://vpn.flying-datacenter.de:6969/announce', 
                    'http://trk.publictracker.xyz:6969/announce', 
                    'http://tracker2.dler.org:80/announce', 
                    'http://tracker1.bt.moack.co.kr:80/announce', 
                    'http://tracker.zerobytes.xyz:1337/announce', 
                    'http://tracker.sloppyta.co:80/announce', 
                    'http://tracker.skyts.net:6969/announce', 
                    'http://tracker.noobsubs.net:80/announce', 
                    'http://tracker.nighthawk.pw:2052/announce', 
                    'http://tracker.loadbt.com:6969/announce', 
                    'http://tracker.lelux.fi:80/announce', 
                    'http://tracker.gbitt.info:80/announce', 
                    'http://tracker.dler.org:6969/announce', 
                    'http://tracker-cdn.moeking.me:2095/announce', 
                    'http://torrenttracker.nwc.acsalaska.net:6969/announce', 
                    'http://torrentclub.online:54123/announce', 
                    'http://t.overflow.biz:6969/announce', 
                    'http://rt.tace.ru:80/announce', 
                    'http://retracker.sevstar.net:2710/announce', 
                    'http://pow7.com:80/announce', 
                    'http://open.acgnxtracker.com:80/announce', 
                    'http://ns3107607.ip-54-36-126.eu:6969/announce', 
                    'http://h4.trakx.nibba.trade:80/announce', 
                    'udp://vibe.sleepyinternetfun.xyz:1738/announce', 
                    'udp://tracker4.itzmx.com:2710/announce', 
                    'udp://tracker2.itzmx.com:6961/announce', 
                    'udp://tracker.kali.org:6969/announce', 
                    'udp://tracker.filemail.com:6969/announce', 
                    'udp://tr.bangumi.moe:6969/announce', 
                    'udp://open.lolicon.eu:7777/announce', 
                    'udp://concen.org:6969/announce', 
                    'udp://bt.firebit.org:2710/announce', 
                    'udp://anidex.moe:6969/announce', 
                    'http://tracker4.itzmx.com:2710/announce', 
                    'http://tracker3.itzmx.com:6961/announce', 
                    'http://tracker2.itzmx.com:6961/announce', 
                    'http://tracker.bt4g.com:2095/announce', 
                    'http://t.acg.rip:6699/announce', 
                    'http://open.acgtracker.com:1096/announce', 
                    'http://bt.100.pet:2710/announce']
    return trackers

def addTrackers(user,password,host,filePath,lstTorrents):
    if len(lstTorrents) == 0:
        return
        
    print(f'found torrents:')
    print(f'ID STATUS NAME')
    for torrent in lstTorrents:
        print(f'{torrent.tid} {torrent.status} {torrent.name}')
    print("")
    
    availableTorrents = [torrent for torrent in lstTorrents if torrent.status not in ("Stop","Finished","Seeding")]

    if len(availableTorrents) == 0:
        return

    trackers = getTracker()
    for torrent in availableTorrents:
        print(f'add trackers to {torrent.name}: ')
        for tracker in trackers:
            if user:
                command = f'"{filePath}" "{host}" --auth={user}:{password} --torrent "{torrent.tid}" -td "{tracker}"'
            else:
                command = f'"{filePath}" "{host}" --torrent "{torrent.tid}" -td "{tracker}"'
                
            try:
                ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
                if ret.returncode == 0:
                    print(f'add {tracker} -> successed!')
                else:
                    print(f'add {tracker} -> failed!')
            except:
                print(f'add {tracker} -> failed!')
        print(f'add trackers to {torrent.name} done!')
        print("")
    return

def main(argv):
    user = ''
    password = ''
    filePath = 'transmission-remote'
    host = 'localhost'
    isSetUser = False
    
    version = '0.1'
    helpMsg = 'python pyAddTracker.py -u <username> -h <host> -p <transmission_file_path>'
    try:
        opts,args = getopt.getopt(argv,"u:h:p:v",["help","version","path","user","host"])
    except getopt.GetoptError:
        print(helpMsg)
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == "--help":
            print(helpMsg)
            sys.exit()
        elif opt in ("-v", "--version"):
            print (f'pyAddTracker v{version}')
            sys.exit()
        elif opt in ("-h", "--host"):
            host = arg
        elif opt in ("-p", "--path"):
            filePath = arg
        elif opt in ("-u", "--user"):
            user = arg
            isSetUser = True

    if isSetUser:
        password = getpass()

    lstTorrents = getTorrent(user,password,host,filePath)
    addTrackers(user,password,host,filePath,lstTorrents)

if __name__ == '__main__':
    main(sys.argv[1:])