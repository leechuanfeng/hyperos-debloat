import json

# Global debloat list
with open("debloat_list/uad_lists.json", 'r', encoding='utf-8') as f:
    data = json.load(f)


#app_package_names = list(data.keys())
app_package_names = []
for line in data:
    if 'removal' in data[line] and data[line]['removal'] == 'Recommended':
        app_package_names.append(line)

with open("debloat_list/donotuninstall.txt", 'r') as f:
    donotuninstall_lines = f.readlines()

donotuninstall = [line.strip() for line in donotuninstall_lines]

with open("debloat_list/safetouninstall.txt", 'r') as f:
    safetouninstall_lines = f.readlines()

safetouninstall = [line.strip() for line in safetouninstall_lines]


def checkDebloat(items):
    uninstall_list = []
    remaining_list = []

    for item in items:
        if item in app_package_names or item in safetouninstall:
            uninstall_list.append(item)
        else:
            remaining_list.append(item)

    final_uninstall_list = []
    for item in uninstall_list:
        if item in donotuninstall:
            remaining_list.append(item)
        else:
            final_uninstall_list.append(item)

    return final_uninstall_list, remaining_list