
from itertools import cycle
from sys import argv

file_name, count = argv

count_int = int(count)

my_list = [0,1,'end']

cnt = 0
for el in cycle(my_list):
	if cnt >= count_int:
		break
	print(el)
	cnt += 1
