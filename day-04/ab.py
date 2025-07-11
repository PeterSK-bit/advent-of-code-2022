with open("data.txt", "r") as f:
    inputs = f.readlines()

overlaped=0

for line in inputs:
    a, c = line.split(",")
    a, b = a.split("-")
    c, d = c.split("-")
    #part 1
    if int(a)<=int(c) and int(b)>=int(d) or int(c)<=int(a) and int(d)>=int(b):
    #part 2
    #if int(a)>=int(c) and int(a)<=int(d) or int(c)>=int(a) and int(c)<=int(b):
        overlaped += 1

print(overlaped)