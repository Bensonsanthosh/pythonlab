#write a program to open a file and read its contents
f=open("pg1.txt","w")
f.write("Oops i deleted the content")
f.close()
f=open("pg1.txt","r")
print(f.read())
