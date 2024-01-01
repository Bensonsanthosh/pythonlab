import csv 
with open("emv.csv","r") as e:
     data=csv.reader(e)
     for i in data:
        print(i)
