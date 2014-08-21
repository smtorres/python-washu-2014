import tweepy
import csv
import time


# Create 2 .csv files to store data in case of long scripts and Twitter limits
headers = ["user", "count"]
filename = "target_twitter.csv"
readFile = open(filename, "wb")
csvwriter = csv.writer(readFile)
csvwriter.writerow(headers)

headers2 = ["user", "count_tweets"]
filename2 = "followed_twitter_count.csv"
readFile2 = open(filename2, "wb")
csvwriter2 = csv.writer(readFile2)
csvwriter2.writerow(headers2)


#First parameter is Consumer Key, second is Consumer Secret 
auth = tweepy.OAuthHandler('keys', 'keys2')
auth.set_access_token('keys', 'keys2')    
api = tweepy.API(auth)

api.rate_limit_status()

target = 'valer_si'

target_followers = api.followers_ids(target)

target_followers_followers = []

for i in target_followers:
	time.sleep(5)
	#temp_user = api.get_user(i)
	#followers_target_temp = temp_user.followers_count
	followers_target_temp = api.get_user(i).followers_count
	target_followers_followers.append(followers_target_temp)
	csvwriter.writerow([i, followers_target_temp])
	if len(target_followers_followers) % 10 == 0: print "%i of %i" % (len(target_followers_followers), len(target_followers))

print max(target_followers_followers)

#####################################################
## The most followed user that follows your target ##
#####################################################
# Id:
Max_Followed_id_a = max(target_followers_followers)
Max_Followed_id_b = target_followers_followers.index(Max_Followed_id_a)
Max_Followed_id = target_following[Max_Followed_id_b]
#Max_Followed_id = 17986973
max_followed = api.get_user(user_id= Max_Followed_id)
#Screen name
max_followed_name = max_followed.screen_name
print max_followed_name
# @Addictd2Success
# Number of followers
max_followed_number_followers = max_followed.followers_count
print max_followed_number_followers
#523204


#####################################################
## The most active user that your target follows. ##
#####################################################
target_following = api.friends_ids(target)
print len(target_following)

target_following_tweets = []


for i in target_following:
	time.sleep(5)
	#temp_following = api.get_user(i)
	#temp_following_count = temp_following.statuses_count
	temp_following_count = api.get_user(i).statuses_count
	target_following_tweets.append(temp_following_count)
	csvwriter2.writerow([i, temp_following_count])
	if len(target_following_tweets) % 10 == 0: print "%i of %i" % (len(target_following_tweets), len(target_following))

#Maximum Number of tweets:
Most_active_tweets = max(target_following_tweets)
#594661
pos_Most_active_id = target_following_tweets.index(Most_active_tweets)
# Id
Most_active_id = target_following[pos_Most_active_id]
print Most_active_id
#205339755
Most_active = api.get_user(user_id= Most_active_id)
# Screen name
Most_active_name = Most_active.screen_name
print Most_active_name
# 072AvialCDMX




