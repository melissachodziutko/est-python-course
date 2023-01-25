import os
'''I took these straight off of google, i'll tell you what to do with them, but you have to apply your knowledge as to 
where and what you're changing. And if you don't have the knowledge, then practice googling :)'''

#Write "my name is (your name)" to the given file
f = open("demofile2.txt", "a")
f.write("See you soon!")
f.close()
#make sure you close the file at the end of every section

#print the first line of the file
f = open("demofile.txt", "r")
print(f.read(5))
f.close()

#this one won't work if you're doing an online compiler, but you can still practice
#create a new file called "info.txt"
f = open("myfile.txt", "x")

#now remove the file
os.remove("myfile.txt")

#challenge: create a file, write information to the file, and then search inside the file for a keyword
