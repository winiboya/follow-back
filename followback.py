import json

# open and save files
with open("followers.json", "r") as f:
    followers = json.load(f)
with open("following.json", "r") as f:
    following = json.load(f)

# create empty lis
followers_list = []
not_following = []

# save a list of all followers
for person in followers["relationships_followers"]:
    person = person["string_list_data"][0]["value"]
    followers_list.append(person)

# check in following for people who are not followers
for person in following["relationships_following"]:
    person = person["string_list_data"][0]["value"]
    # add to a list of people who are not following back
    if (person not in followers_list):
        not_following.append(person)

# print the users not following back
print(str(len(not_following)) + " are not following you back.")
not_following.sort()
for username in not_following:
    print("@" + username)
