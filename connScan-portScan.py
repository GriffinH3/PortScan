"""
Connection Scan and Port Scan functions.

Attempts to resolve an IP address to a hostname. 
Enumerate through each individual port attempting to connect using the connScan.
"""

import optparse
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print('[+]%d/tcp closed' % tgtPort)
        connSkt.close()
    
    except:
        print('[+]%d/tcp closed' % tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    
    except:
        print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: ' + tgtIP)
        setdefaulttimeout(1)

    except:
        print('\n[+] Scan Results for: ' + tgtIP)
        setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print('Scanning Port' + tgtPort)
        connScan(tgtHost, int(tgtPort))
