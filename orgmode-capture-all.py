#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
PATH_TO_INBOX='/Users/magnus/geekbook/notes/inbox.org'

import argparse
import sys
import datetime
import os


def get_parser():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    #parser.add_argument('-', "--", help="", default="")
    parser.add_argument("-v", "--verbose",
                        action="store_true", help="be verbose")
    parser.add_argument("file", help="", default="") # nargs='+')
    return parser


import subprocess

def exe(cmd):
    o = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = o.stdout.read().strip().decode()
    err = o.stderr.read().strip().decode()
    return out, err


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    t = open(args.file).read()

    import pathlib
    path = pathlib.Path(__file__).parent.resolve() # to place where the script is

    url, err = exe(f'osascript {path}/as.applescript')
    #https://support.apple.com/en-gb/HT208050
    if args.verbose: print(url)

    with open(PATH_TO_INBOX, 'a') as f:
    # add to the begining of the file
    #with open('/Users/magnus/geekbook/notes/work-curr.org', 'r+') as f:
    #    content = f.read()
    #    f.seek(0, 0)
        f.write('* ' + t.split('\n')[0][:50] + ' :senttoinbox:\n') # 30 of the first line
        f.write('\n'.join(t.split('\n')[:]))
        f.write('\n' + url + '\n')
        x = datetime.datetime.now()
        f.write(x.strftime("[%Y-%m-%d %a %H:%M]\n"))
    
    url = 'inbox added'
    t = ''
    os.system("osascript -e 'display notification "" with title\"" + url + '' + t + "\"'")
