import re

# Version 1.0:
# Email log stored as a strin
email_log = """Email received June 2016 from sam@gmail.com
            Email received from Google Cloud google@gmail.com
            Email rejected from apple apple@gmail.com."""

# We use the findall() method, which returns a list of matches to  a regex pattern
emails = re.findall('\w+@\w+\.\w+', email_log)
print(emails)

# Version 2.0:

# Load the practice file
file = 'regex_practice_file.txt'

# Open the file
with open(file, 'r') as file:
    content = file.read()

# Example 1.0: Find all a
all_a = re.findall(r'\w+a', content)

# Example 2.0: Find all email addresses in content
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
email = email_pattern.findall(content)

print(email)
# print(all_a)