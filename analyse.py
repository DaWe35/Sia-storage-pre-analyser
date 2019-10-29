# !/usr/bin/python
import os

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

def human_readable_size(size, decimal_places=3):
    for unit in ['byte','KB','MB','GB','TB','PB','EB']:
        if size < 1000.0:
            break
        size /= 1000.0
    return f"{size:.{decimal_places}f} {unit}"



print('Please input a folder to calculate size:')
while True:
	folder = input()
	if os.path.isdir(folder):
		break
	else:
		print('Folder not found, please enter a valid path:')

disk_size = 0
sia_size = 0
file_number = 0

for root, dirs, files in os.walk(folder, topdown=True):
	for name in files:
		file_number += 1
		file_absolute = os.path.join(root, name)
		size = getSize(file_absolute)
		disk_size += size
		if size < 41943040: #40 MiB
			sia_size += 41943040
		else:
			sia_size += size
		print(name, '-', size)


print(file_number, ' files are scanned from ', folder)
print('Size on disk:', human_readable_size(disk_size))
print('Estimated size on Sia:', human_readable_size(sia_size))