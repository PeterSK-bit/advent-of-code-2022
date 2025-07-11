#in data.txt the creates are modified to lines without [] and indexes

crates=[]
with open("data.txt", "r") as f:
    for line in range(9):
        crates.append(f.readline().replace("\n","").split(" "))
        #crates[line]=crates[line][::-1]

    commands=f.readlines()

for i in range(len(commands)):
    commands[i]=commands[i].split(" ")

for i in commands:
    n, frm, to = int(i[1]), int(i[3]) -1 ,int(i[5]) -1
    #part 1
    crates[to] += reversed(crates[frm][-n:]) 

    #part 2
    #crates[to] += crates[frm][-n:]
    crates[frm] = crates[frm][:-n]

for column in crates:
    print(column[-1], end="")