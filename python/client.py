#!/usr/bin/env python2.7
import os
import sys

from omi import *


def main(argv=None):
    be = BookEnd('main')
    for i in range(len(argv)):
        BookEndPrint('args[' + str(i) + ']: "' + argv[i] + '"')
    if len(argv) == 4:
        try:
            path = os.path.split(os.path.realpath(argv[0]))[0] + '/' + argv[1]
            port = int(argv[2])
            client = Client(path, port, argv[3])
            client.run()
        except:
            e = sys.exc_info()[0]
            sys.stderr.write('Unhandled exception: ' + str(e) + '\n')
            raise
    else:
        sys.stderr.write('Usage: client.py [SOCKET_ID] [PROVIDER]\n')


if __name__ == '__main__':
    sys.exit(main(sys.argv))
