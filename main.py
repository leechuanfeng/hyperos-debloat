import os
from debloat_checker import *

file_path = 'app.txt'

with open(file_path, 'r', encoding='utf-16') as f:
    lines = f.readlines()

items = [line.replace('package:', '', 1).strip() for line in lines]

uninstall_list, remaining_list = checkDebloat(items)
uninstall_list.sort()

# Create directory if the directory not exists
if not os.path.exists("output"):
     os.makedirs("output")
# Open the output file to write
with open("output/uninstall_list.txt", 'w') as f_out:
    # Write each item to the output file
    for item in uninstall_list:
        f_out.write('platform-tools/adb.exe shell pm uninstall --user 0 ' + item + '\n')
remaining_list.sort()
# Open the output file to write
with open("output/remaining_list.txt", 'w') as f_out:
    # Write each item to the output file
    for item in remaining_list:
        f_out.write(item + '\n')