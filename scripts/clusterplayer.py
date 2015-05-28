#!/usr/bin/env python

from common import *
import cluster
import config
import sys

def usage():
    print '''

    Usage: clusterplayer.py [start|stop]

        Start or stop a ramcloud cluster based on the configuration file

    '''

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(2)
    command = sys.argv[1]
    if command == 'start':
        cluster.run(replicas = 0,
            transport = 'tcp',
            share_hosts = True,
            clean_up = False,
        )
    elif command == 'stop':
        cluster.stop()
    else:
        print 'invalid cluster command'
        usage()
        sys.exit(2)
