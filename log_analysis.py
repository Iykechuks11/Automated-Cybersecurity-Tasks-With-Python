import re

# Path to the log file
log_file_path = 'example_log_file.log'

# Regular expression pattern to match lines with ERROR
error_pattern = re.compile(r'ERROR')

# Open and read the log file
with open(log_file_path, 'r') as file:
    for line in file:
        if error_pattern.search(line):
            print(line.strip())

