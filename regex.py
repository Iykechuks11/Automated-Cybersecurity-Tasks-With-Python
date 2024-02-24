import re

# There are many functions/methods in the re module. ex: findall()

# Basics of regular expressions
ts = re.findall("ts", "tsnow, tshah, bmoreno")
bm = re.findall("bm", "tsnow, tshah, bmoreno")

# print(ts)
# print(bm)

# Symbols for character types '\w' or '.
all = re.findall('.', 'h32rb1_7')
print(all)

# SIngle digits
singleDigits = re.findall('\d', 'h32rb1_7')
print(singleDigits)

# Indicate a specific number of repetitions
repetition = re.findall("\d{3}", "h32rb17 k825t0m c2994eh")
print(repetition) # ['825', '299']

more = re.findall("\d{1,3}", "h32rb17 k825t0m c2994eh")

print(more) # ['32', '17', '825', '0', '299', '4']


# Constructing a pattern
pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))