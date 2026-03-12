#open function
f = open("demofile.txt")
print(f.read()) 

#open a file on different location
f = open("D:\\myfiles\welcome.txt")
print(f.read()) 

#using the with statement
with open("demofile.txt") as f:
    print(f.read()) 

#close files
f = open("demofile.txt")
print(f.readline())
f.close() 

#read only parts of the file
with open("demofile.txt") as f:
    print(f.read(5)) 

#read lines
with open("demofile.txt") as f:
    print(f.readline())

#read two lines of the file
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline()) 

#loop through the file line by line
with open("demofile.txt") as f:
    for x in f:
        print(x) 
