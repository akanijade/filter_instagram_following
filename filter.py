import json


followers_data_array = []

following_data_array = []



# appending followers.json into an array
f = open('followers.json')

followers_data = json.load(f)

for i in followers_data['relationships_followers']:
    for j in i['string_list_data']:
        followers_data_array.append(j['value'])


f.close()

# appending following.json into an array
f1 = open('following.json')

following_data = json.load(f1)

for x in following_data['relationships_following']:
    for y in x['string_list_data']:
        following_data_array.append(y['value'])

f1.close()

# printing usernames to people who didn't follow you back :')
# print("Missing values in followers list from following list:", (set(following_data_array).difference(followers_data_array)))


result = (set(following_data_array).difference(followers_data_array))

for user in result:
    print(user)
