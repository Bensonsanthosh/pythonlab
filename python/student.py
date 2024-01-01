import csv 
with open("ben.csv","r") as e:
     data=csv.reader(e)
     for i in data:
             print(i)
