with open("data.txt", 'r') as f:
    lines=f.readlines()

score = 0
values = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    }

key = {
    "A": "Y",
    "B": "Z",
    "C": "X",
    "D": "Y",
    }

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n',"")
    a, b=lines[i].split(" ")
    if b == "X":
        score+=values[key[chr(ord(a)+1)]]
    elif b == "Y":
        score += values[chr(ord(a)+23)] + 3
    else:
        score += values[key[a]] + 6
        
print(score)