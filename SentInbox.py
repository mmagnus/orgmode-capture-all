#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import argparse
import sys


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

    url, err = exe('cd /Users/magnus/workspace/PocketSnippets && osascript as.applescript')
    #https://support.apple.com/en-gb/HT208050
    print(url)

    import os

    with open('/Users/magnus/geekbook/notes/inbox.org', 'a') as f:
                                       #30 or full
        f.write('* ' + t.split('\n')[0][:] + ' :senttoinbox:\n') # 30 of the first line
        f.write(t + '\n')
        f.write(url + '\n')
        import datetime
        x = datetime.datetime.now()
        f.write(x.strftime("[%Y-%m-%d %a %H:%M]\n"))
    
    url = 'inbox added'
    t = ''
    os.system("osascript -e 'display notification "" with title\"" + url + '' + t + "\"'")
