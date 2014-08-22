import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker
import csv
import time


#Connect to the local database, can use :memory: to just try it out in memory
engine = sqlalchemy.create_engine('sqlite:////Users/michelletorres/Documents/scrapes.db', echo=False)

Base = declarative_base() 

#Define some schemas
class Post(Base):
  __tablename__ = "scrapes"
  
  id = Column(Integer, primary_key=True)
  is_post = Column(String)
  date = Column(String)
  url = Column(String)
  title = Column(String)
  
  author_id = Column(Integer, ForeignKey("authors.id"))
  
  def __init__(self, is_post, date, url, title, author=None):
    self.is_post = is_post
    self.title = title
    self.date = date
    self.url = url
    self.author = author
    
  def __repr__(self):
    return "Post '%s' written in %s. " % (self.title, self.date)


class Author(Base):
  __tablename__ = "authors"
  
  id = Column(Integer, primary_key=True)
  name = Column(String)
  all_posts = relationship("Post", backref="author")
  
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "Post by %s" % (self.name)


Base.metadata.create_all(engine) 

Post.__table__  
Author.__table__


#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

##################### CSV FILES

# Create the entries

entries_post = []
authors_names = []

with open('r-bloggers_info.csv', 'rb') as f:
  reader = csv.reader(f)
  firstline = True
  for row in reader:
    if firstline:    #skip first line
      firstline = False
      continue
    temp_post = Post(row[0],row[1], row[3], row[4])
    authors_names.append(row[2])
    entries_post.append(temp_post)
    session.add(temp_post)

session.commit()

# Create the authors
authors_list_pre = set(authors_names)
authors_list = list(authors_list_pre)
print authors_list
new_authors_list = [] 
for i in authors_list:
  temp_author = Author(i)
  new_authors_list.append(temp_author)

print new_authors_list

for i in range(len(entries_post)):
  for author in new_authors_list:
    if authors_names[i] == author.name:
      entries_post[i].author = author
    else:
      pass

print entries_post[1]
print entries_post[1].author

    count_tweets.append(row[1])

