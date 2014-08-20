# Scraper to collect entries from R-bloggers

from bs4 import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 
import re


page_to_scrape = 'http://www.r-bloggers.com/page/2/'

# Open webpage
req = urllib2.Request(page_to_scrape, headers = {"User-Agent" : "Magic Browser"})
webpage = urllib2.urlopen(req)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

# Extract petitions on page
post_entries = soup.findAll("div", attrs={'id':re.compile('^post')})

#class="entry"><a href="http://www.r-bloggers.com/model-building-with-the-iris-data-set-for-big-data/" title="Model building with the iris data set for Big Data">
test1 = post_entries[1]
print test1
print "*********"
temp_url = test1.find("div", attrs={'class' : 'entry'})
print temp_url
print "**********************"
temp_url2 = temp_url.find("a").get("href")
print temp_url2
#is_post = []
#post_date = []
#post_author = []
#post_url = []
#post_titles = []