### To run this script:
###     python -c 'import decoraters; print decoraters.elapsed_time()'

import time
import urllib2

def download_webpage():
    url = 'http://linuxacademy-static-blogpost.s3-website-us-east-1.amazonaws.com/'
    response = urllib2.urlopen(url, timeout = 60)
    return response.read()

def elapsed_time():
    t0 = time.time()
    webpage = download_webpage()
    t1 = time.time()
    print "Elapsed time %s\n" % (t1 - t0)