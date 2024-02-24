import re

# Load file
usernames = 'user_ids.txt'

# Open and read file
with open(usernames, 'r') as file:
    get_users = file.read()


usernames = get_users.split() # divided into a list of separate usernames

print(usernames)

usersnames_starting_with_j = re.compile(r'j\w+')

found = re.findall(usersnames_starting_with_j, get_users)

print(found)