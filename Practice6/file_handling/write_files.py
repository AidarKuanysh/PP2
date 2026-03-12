#append content to the file
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
    print(f.read()) 

#overwrite existing content
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read()) 

#create a new file called "myfile.txt"
f = open("myfile.txt", "x")

