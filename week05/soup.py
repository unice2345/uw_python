"""
print anchors
Demonstrate screen scraping with BeautifulSoup.

"""

import urllib2
import re
from pprint import pprint
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen('https://github.com/unice2345/uw_python/tree/master/week04').read()

soup = BeautifulSoup(page)

anchors = soup.findAll('a')

#find all the anchor tags that link to external web pages
externals = soup.findAll('a', attrs={'href':re.compile('http.*')})

pythonfiles = soup.findAll('a', attrs={'href':(lambda a: a and a.endswith('.py'))})
print pythonfiles
