#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""programa super-senzill per saber la IP a partir del nom de la web"""

import socket

def resolve(host):
    return socket.gethostbyname(host)

host = raw_input('Enter a valid website: ')
try:
    ip = resolve(host)
    print host, 'IP is: ', ip
except:
    print host, 'is not a valid website'
