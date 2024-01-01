#write a program to create a file with content welcome to mits
f=open("pg1.txt","w")
f.write("Welcome to MITS")
f.close()
f=open("pg1.txt","r")
print(f.read())
