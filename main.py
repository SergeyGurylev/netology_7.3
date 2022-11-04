file_names = ['1.txt', '2.txt', '3.txt']
entries = {}

for file_name in file_names:
    with open(file_name) as file:
        strings = file.readlines()
        entries[len(strings)] = {'file_name': file_name, 'strings': strings}

file = open('result.txt', 'wt')
for key in sorted(entries.keys()):
    file.write(entries[key]['file_name']+'\n')
    file.write(str(key)+'\n')
    for string in entries[key]['strings']:
        file.write(string.strip()+'\n')

file.close()
