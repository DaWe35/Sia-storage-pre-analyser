# !/usr/bin/python
import os
import statistics

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

def human_readable_size(size, decimal_places=3):
	if size == 'NaN':
		return 'NaN'
	for unit in ['byte','KB','MB','GB','TB','PB','EB']:
		if size < 1000.0:
			break
		size /= 1000.0
	return f"{size:.{decimal_places}f} {unit}"

def avg(lst):
	try:
		return sum(lst) / len(lst)
	except:
		return 'NaN'



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



print('Size on')
print('    Disk:', human_readable_size(disk_size))
print('    Sia: ', human_readable_size(sia_size))
print()
print('Lost space: ', human_readable_size(sia_size-disk_size))
print('    +' + str(int(sia_size/disk_size*100)-100) + '% empty space used for scaling files up to 40MiB')
print()
print('Too small files:', small_files)
print('    Average:', human_readable_size(avg(small_file_list)))
print()
print('Larger files:', large_files)
print('    Average:', human_readable_size(avg(large_file_list)))
print()
print('All files:', len(file_sizes))
print('    Average:', human_readable_size(avg(file_sizes)))
print('    Median:', human_readable_size(statistics.median(file_sizes)))