# none functional

current=""
files={}

#formating data
with open("data.txt", "r") as f:
    temp = f.readlines()
    lines= [line[:-1] for line in temp]
    del temp

#algorithm
for line in lines:
    if line[0] == "$" and line.split(" ")[1] == "cd":
        if line.split(" ")[2] != "..":
            if line.split(" ")[2] in files.keys():
                pass #will do something
            else:
                if current == "": files[line.split(" ")[2]] = {} 
                else: files[current][line.split(" ")[2]] = {}
                current=line.split(" ")[2]

print(files)