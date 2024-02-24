name = 'john'
code = 'encrypted'

print(name.upper())
print(code.index('c'))


# Slice
device_id = "u899v381w363"

# Concatenate two lists
new_users = ['admin', 'Ben']
approved_users = ['admin', 'John']
users = new_users + approved_users

# print(users)

# Remove element from list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'John']
my_list.remove(9)
my_list.remove('John')
my_list.append('Bola')
# print(my_list)

# Split
with open('user_ids.txt', 'r') as f:
    file_text = f.read()

usernames = file_text.split()
print(usernames)

