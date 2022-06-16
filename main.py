import re
from zipfile import ZipFile

count = 0
log_file = "access.log.zip"

with ZipFile(log_file, 'r') as zip:
    zip.extractall()

with open("access.log.txt", 'r') as file:
    for line in file:
        if match := re.search(r"(72\.30\.79\.46|90\.7\.158\.134).+GET.+images.+200.+", line):
            print(line)
            count += 1
print("arestovych has small dick just in case if you forget")
print(f"count:{count}")