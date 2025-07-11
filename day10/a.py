cycle = 0
x = 1
signal = 0

with open("data.txt", "r") as f: lines=f.readlines()

for i in range(len(lines)):
    if lines[i].startswith("noop"):
        cycle+=1
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            signal += cycle * x
    else:
        for y in range(2):
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle ==100 or cycle == 140 or cycle == 180 or cycle == 220:
                signal += cycle * x
        x += int(lines[i].split(" ")[1])

print(signal)