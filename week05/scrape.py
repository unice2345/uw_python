"""
scrape.py
Screen-scraping demo: open a page, find and print the first anchor element
"""

import urllib2

#url = 'http://www.baidu.com'
url = 'https://docs.python.org/2/howto/urllib2.html'
page = urllib2.urlopen(url).read()
start = page.find('<a ')
print page[start:start+60]
