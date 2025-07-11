with open("data.txt", 'r') as f:
    lines=f.readlines()

score = 0
values = {
    "X":1,
    "Y":2,
    "Z":3,
    }

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n',"")
    a, b = lines[i].split(" ")

    if ord(a) + 23 == ord(b):
        score += 3
    elif a == "A" and b == "Y" or a == "B" and b == "Z" or a == "C" and b == "X":
        score+=6
    score += values[b]

print(score)