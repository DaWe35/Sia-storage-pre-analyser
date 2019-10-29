# !/usr/bin/python
import os
import statistics

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

def human_readable_size(size, decimal_places=3):
    for unit in ['byte','KB','MB','GB','TB','PB','EB']:
        if size < 1000.0:
            break
        size /= 1000.0
    return f"{size:.{decimal_places}f} {unit}"

def avg(lst):
	try:
		return sum(lst) / len(lst)
	except:
		return 'N/A'



print('Please input a folder to calculate size:')
while True:
	folder = input()
	if os.path.isdir(folder):
		break
	else:
		print('Folder not found, please enter a valid path:')

file_sizes = []

for root, dirs, files in os.walk(folder, topdown=True):
	for name in files:
		file_absolute = os.path.join(root, name)
		size = getSize(file_absolute)
		file_sizes.append(size)





disk_size = 0
sia_size = 0
small_files = 0
large_files = 0
small_file_list = []
large_file_list = []

for size in file_sizes:
	disk_size += size
	if size < 41943040: #40 MiB
		sia_size += 41943040
		small_files += 1
		small_file_list.append(size)
	else:
		sia_size += size
		large_files += 1
		large_file_list.append(size)
	# print(name, '-', size)




print(len(file_sizes), 'file scanned from', folder)
print('Size on disk:', human_readable_size(disk_size))
print('Size on Sia: ', human_readable_size(sia_size))
print()
print('Small files (less than 40 MiB):', small_files, '- average:', human_readable_size(avg(small_file_list)))
print('Large files (greater than 40 MiB):', large_files, '- average:', human_readable_size(avg(large_file_list)))
print('Average file size:', human_readable_size(avg(file_sizes)))
print('Median:', human_readable_size(statistics.median(file_sizes)))
