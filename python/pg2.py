import csv
with open("b.csv",'r') as f:
	data=csv.reader(f)
	for i in data:
		print(i)


