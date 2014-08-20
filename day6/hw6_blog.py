# Code adapted from Matt Dickenson
# Scraper to collect entries from R-bloggers

from bs4 import BeautifulSoup
import csv 
from nltk.util import clean_html
import urllib2 
import re

# What info do we want?
headers = ["is_post", "publish_date", "author", "url", "post_title"]

# Where do we save info?
filename = "r-bloggers_info.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

# What page? (Firs: homepage)
page_to_scrape = 'http://www.r-bloggers.com'

# Open webpage
req = urllib2.Request(page_to_scrape, headers = {"User-Agent" : "Magic Browser"})
webpage = urllib2.urlopen(req)

# Parse it
soup = BeautifulSoup(webpage.read())
soup.prettify()

# Extract posts
post_entries = soup.findAll("div", attrs={'id':re.compile('^post')})

is_post = []
post_date = []
post_author = []
post_url = []
post_titles = []


# First loop is for the homepage!
for i in post_entries:
	temp_is_post = True
	temp_titles = clean_html(str(i.find("a")))
	temp_date = i.find("div", attrs={'class':'date'})
	temp_date = clean_html(str(temp_date))
	temp_author = i.find("a", attrs={'rel':'author'})
	temp_author = clean_html(str(temp_author))
	temp_url = i.find("a", attrs={'class' : 'more-link'}).get("href")
	is_post.append(temp_is_post)
	post_date.append(temp_date)
	post_author.append(temp_author)
	post_url.append(temp_url)
	post_titles.append(temp_titles)

# Scrap from 2nd page and on....
n = 1
for j in range(2, 536):

	page_to_scrape = 'http://www.r-bloggers.com/page/' + str(j) + "/"

	req = urllib2.Request(page_to_scrape, headers = {"User-Agent" : "Magic Browser"})
	webpage = urllib2.urlopen(req)

	soup = BeautifulSoup(webpage.read())
	soup.prettify()

	post_entries = soup.findAll("div", attrs={'id':re.compile('^post')})

	for i in post_entries:
		temp_is_post = False
		try:
			temp_titles = clean_html(str(i.find("a")))
			temp_date = i.find("div", attrs={'class':'date'})
			temp_date = clean_html(str(temp_date))
			temp_author = i.find("a", attrs={'rel':'author'})
			temp_author = clean_html(str(temp_author))
			temp_url = i.find("div", attrs={'class' : 'entry'})
			temp_url2 = temp_url.find("a").get("href")
			post_date.append(temp_date)
			post_author.append(temp_author)
			post_url.append(temp_url2)
			post_titles.append(temp_titles)

		except:
			temp_titles = "Null"
			temp_date = "Null"
			temp_author = "Null"
			temp_url = "Null"
			post_date.append(temp_date)
			post_author.append(temp_author)
			post_url.append(temp_url)
			post_titles.append(temp_titles)

		# Test: If the entry has a title, an author and a date THEN it is a post
		if temp_titles!="Null" and temp_author!="Null" and temp_date!="Null":
			temp_is_post = True
		is_post.append(temp_is_post)
		print temp_is_post
	n += 1
	print n #Just to know how are we doing...

# Sort from oldest to newest
index = range(len(post_titles))
index_sort = index[::-1]


# Write to the .csv file
for j in index_sort:
	csvwriter.writerow([is_post[j], post_date[j], post_author[j], post_url[j], post_titles[j]])

