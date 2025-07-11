x, counter, monitor = 1, 0, []

with open("data.txt", "r") as f: lines=f.readlines()

for i in range(len(lines)):
    loop = 1 if lines[i][0:4] == "noop" else 2
    for j in range(loop):
        if x-1 == counter or x == counter or x+1 == counter:
            monitor.append("#")
        else:
            monitor.append(".")
        counter += 1
        if counter >= 40:
            counter = 0
    if loop == 2:
        x += int(lines[i].split(" ")[1])

#printing monitor
for i in range(len(monitor)):
    if i%40 == 0:
        print()
    print(monitor[i],end="")