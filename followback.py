import json

# open and save files
with open("followers.json", "r") as f:
    followers = json.load(f)
with open("following.json", "r") as f:
    following = json.load(f)

# create empty sets
followers_set = set()
following_set = set()

# save a set of all followers
for person in followers["relationships_followers"]:
    person = person["string_list_data"][0]["value"]
    followers_set.add(person)

# save a set of all following
for person in following["relationships_following"]:
    person = person["string_list_data"][0]["value"]
    following_set.add(person)

# find the difference between the lists
not_following = following_set.difference(followers_set)

# print the users not following back
print(str(len(not_following)) + " are not following you back.")
not_following = sorted(not_following)
for username in not_following:
    print("@" + username)
