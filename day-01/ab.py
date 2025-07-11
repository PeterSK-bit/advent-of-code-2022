with open ("data.txt", 'r') as f:
    lines=f.readlines()

elf = 0
elfs = []

for line in lines:
    if line!="\n":
        elf+=int(line)
    else:
        elfs.append(elf)
        elf=0
elfs.append(elf)

elfs=sorted(elfs, reverse=True)
print(elfs[0]) #part 1
print(elfs[0]+elfs[1]+elfs[2]) #part 2