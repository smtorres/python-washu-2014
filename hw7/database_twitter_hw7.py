import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker
import csv
import time


#Connect to the local database, can use :memory: to just try it out in memory
engine = sqlalchemy.create_engine('sqlite:////Users/michelletorres/Documents/twitter.db', echo=False)

Base = declarative_base() 


#############################################
################# TWITTER ###################
#############################################



class Followers(Base):
  __tablename__ = "followers"
  
  id = Column(Integer, primary_key=True)
  user = Column(String)
  num_followers = Column(Integer)
  
  def __init__(self, user, num_followers):
    self.user = user
    self.num_followers = num_followers
    
  def __repr__(self):
    return "User %s has %s followers. " % (self.user, self.num_followers)


class Tweets(Base):
  __tablename__ = "tweets"
  
  id = Column(Integer, primary_key=True)
  user = Column(String)
  num_tweets = Column(Integer)
  
  def __init__(self, user, num_tweets):
    self.user = user
    self.num_tweets = num_tweets
    
  def __repr__(self):
    return "User %s has %s tweets. " % (self.user, self.num_tweets)

Session = sessionmaker(bind=engine)
session = Session()

with open('target_twitter.csv', 'rb') as g:
	reader2 = csv.reader(g)
	firstline = True
	for row in reader2:
		if firstline:    #skip first line
			firstline = False
			continue
		temp_user = Followers(row[0], row[1])
		#session.add(temp_user)

print temp_user


with open('followed_twitter_count.csv', 'rb') as f:
	reader = csv.reader(f)
	firstline = True
	for row in reader:
		if firstline:    #skip first line
			firstline = False
			continue
		temp_user = Tweets(row[0], row[1])
		session.add(temp_user)

session.commit()





