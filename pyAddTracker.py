'''
Author: qink-dell
Date: 2021-04-03 10:26:42
LastEditors: qink-dell
LastEditTime: 2021-04-04 00:02:22
Description: 
'''

import subprocess
import os
import sys, getopt
import requests
from getpass import getpass

class Torrent(object):
    tid = ''
    name = ''
    status = ''
    def __init__(self, tid, name, status):
        self.tid = tid
        self.name = name
        self.status = status
    
def getTorrent(user,password,host,filePath):
    command = f'"{filePath}" "{host}" --auth={user}:{password} -l'
    lstTorrents = ''

    ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
    if ret.returncode == 0:
        lstTorrents = extractTorrents(ret.stdout)
    else:
        print(ret.stderr)
    return lstTorrents
    
def extractTorrents(torrentMsg):
    lstTorrents = []
    for line in torrentMsg.strip(" ").split("\n"):
        info = [i for i in line.strip(" ").split(" ") if i != ""]
        if len(info) > 0 and info[0] not in ('ID','Sum:'):
            lstTorrents.append(Torrent(info[0], info[-1], info[-2]))
    return lstTorrents

def getTracker():
    url = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt"
    f = requests.get(url)
    with open("trackers_all.txt", "wb"):
        trackers = [i.strip("'") for i in str(f.content)[1:].split("\\n") if i not in ("","'")]
    os.remove("trackers_all.txt")
    return trackers

def addTrackers(user,password,host,filePath,lstTorrents,trackers):
    for torrent in lstTorrents:
        if torrent.status not in ("Stop","Finished","Seeding"):
            for tracker in trackers:
                command = f'"{filePath}" "{host}"  --auth={user}:{password} --torrent "{torrent.tid}" -td "{tracker}"'
                ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
                if ret.returncode == 0:
                    print(f'add tracker {tracker} to {torrent.name} successed')
                else:
                    print(f'add tracker {tracker} to {torrent.name} failed')
            print(f'add tracker {tracker} to {torrent.name} done')

def main(argv):
    filePath = 'transmission-remote'
    user = 'admin'
    password = 'admin'
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
    trackers = getTracker()
    addTrackers(user,password,host,filePath,lstTorrents, trackers)

if __name__ == '__main__':
    main(sys.argv[1:])