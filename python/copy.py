s=open("stud.txt","r")
o=open("odd.txt","w")
e=open("even.txt","w")
content=s.readlines()
print("Contents of the files are:")
print(content)
for i in range(len(content)):
      if i%2==0:
            e.write(content[i])
      else:
            o.write(content[i])
s.close()
o.close()
e.close()        

