#!/usr/bin/python
import sys
import os
import getopt

from common import *
import config
import smux

def usage():
    help = '''
    Usage: clustercli.py [options]

    Options:
    
        -h, --help           Prints this help
        -s, --serverlist     Comma-separated list of servers, if not given, the list of
                             servers will be read from config.py
        -d, --desynch        Keep tmux panes desynchonized (i.e., each pane executes its
                             own command). Default is false.
    '''
    print help

def main(argv):
    serverlist = ''
    desynch = False
    try:
        opts, args = getopt.getopt(argv, 'hs:d', ['serverlist=', 'desynch'])
    except getopt.GetoptError as err:
        print err
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-s', '--serverlist'):
            serverlist = arg
        elif opt in ('-d', '--desynch'):
            desynch = True
    servers = []
    if len(serverlist) == 0: # read server list from config.py
        hosts = config.hosts
        for host in config.hosts:
            servers.append(["ssh %s" %(host[0])])
    else:
        hosts = serverlist.split(',')
        for host in hosts:
            servers.append(["ssh %s" %(host)])
    if desynch:
        smux.create(len(servers), servers)
    else: # synchronized panes
        smux.create(len(servers), servers, executeBeforeAttach=lambda : smux.tcmd("setw synchronize-panes on"))
        
if __name__ == "__main__":
    main(sys.argv[1:])
