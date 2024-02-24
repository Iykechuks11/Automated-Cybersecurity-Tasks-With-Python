# Developing a parsing algorithm

with open('doc/login_attempts.txt', 'r') as file:
    login = file.read()

usernames = login.split()
print(login)