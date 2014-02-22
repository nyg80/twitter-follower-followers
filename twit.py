#Twitter-follower-followers

import twitter

#input your own info in these spaces
consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret=''

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                    access_token_key=access_token_key, access_token_secret=access_token_secret)

print api

#get my own user info
self_user = api.VerifyCredentials()
self_id = self_user.id
self_name = self_user.screen_name
print "got self info, getting friends..."

#get ID of every friend
get_friend_ids = api.GetFriendIDs(self_id)
friend_ids = get_friend_ids["ids"]
curs = get_friend_ids["next_cursor"]
while curs != 0:
	get_friend_ids = api.GetFriendIDs(self_id,cursor=curs)
	friend_ids += get_friend_ids["ids"]
	curs = get_friend_ids["next_cursor"]

print str(len(friend_ids))+" friends found, getting followers..."

#get the list of the ids of all followers
followers = api.GetFollowerIDs()
ids = followers["ids"]
cursor = followers["next_cursor"]
while True:
	followers = api.GetFollowerIDs(cursor=cursor)
	ids += followers["ids"]
	cursor = followers["next_cursor"]
#	print "\t cursor is "+str(cursor)
	if cursor == 0:
		break

print str(len(ids))+" followers found"

#where we will store the results
results = {}

count = 0
for friend_id in friend_ids:
	count += 1
	print "on friend #"+str(count)

	friend = api.GetUser(friend_id)
	if friend_id in ids:
		results[friend.screen_name] = "following me"
	else:
		results[friend.screen_name] = ""
		#get friend's friendIDs
		f_friends = api.GetFriendIDs(friend_id)
		f_ids = f_friends["ids"]
		#FIXME: add loop for cursor for if they follow over 5k people
		#could cause a significant slowdown though

		for f_id in f_ids:
			if f_id in ids: #if they're following self, get their screen_name & add it to the results
				f_friend = api.GetUser(f_id)
				results[friend.screen_name] = "following <a href=\"http://www.twitter.com/"+f_friend.screen_name+"\">@"+f_friend.screen_name+"</a> who follows me"
				break


# loop through the results to aggregate some stats
keys = results.keys()
cnt_no_conn = cnt_following = cnt_2nd_tier = 0
for key in keys:
	if results[key] == "":
		cnt_no_conn += 1
		results[key] = "no connection"
	elif results[key] == "following me":
		cnt_following += 1
	else:
		cnt_2nd_tier += 1

#print the results into an HTML file
filename = self_name+"_followers.html"

open_table = "<h1>People who @"+self_name+" follows on Twitter</h1>"+str(cnt_no_conn)+" with no connection<br />"+str(cnt_2nd_tier)+" follow someone who is a follower<br />"+str(cnt_following)+" following back<br /> <table><tr><td>Username</td><td>Connection</td></tr>"
close_table = "</table>"

FILE = open(filename,"w")
FILE.write(open_table)
for key in keys:
	line = "<tr><td><a href=\"http://www.twitter.com/"+key+"\">@"+key+"</a></td><td>"+results[key]+"</td></tr>"
	FILE.write(line)
FILE.write(close_table)
FILE.close()

print "see "+filename+" for the results"

