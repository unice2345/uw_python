"""
github-api.py

Demonstrate getting and using JSON formatted data from GitHub
Based on example at ...

Here we retrieve the names of all of one particular user's repositories,
that can also be viewd on the page at https://github.com/jon-jacky
"""

import urllib2
import json
from pprint import pprint

# this user has several repos. URL here is a GitHub API call
url = 'https://api.github.com/users/unice2345'
#url = 'https://github.com/unice2345'
handle = urllib2.urlopen(url)
data = json.load(handle)

pprint(data) # show all the data for all the repos
print        # leave some space
print


# We see data is a big dictionary with one key, u'repositories'
# whose value is a list of dictionaries, one for each repo
# in each of these dictionaries, look up repo name at key u'name'


pprint(data[u'repos_url'])
print
print

handle = urllib2.urlopen(data[u'repos_url'])
data = json.load(handle)
pprint(data)
print
print 


names = [ r[u'name'] for r in data ]
pprint(names)
