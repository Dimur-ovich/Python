
from itertools import count
from sys import argv

file_name, start, end = argv

st = int(start)
ed = int(end)

for el in count(st):
	if el > ed:
		break
	else:
		print(el)