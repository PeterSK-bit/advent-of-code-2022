lines=[]
maximum=0

def getColumn(array, x):
    temp = []
    for i in range(len(array)):
        temp.append(array[i][x])
    return temp

with open("data.txt", "r") as f:
    for i in range(99):
        lines.append(f.readline().replace("\n",""))

for i in range(len(lines)):
    for j in range(len(lines[0])):
        column = getColumn(lines, j)
        x1, x2, y1, y2 = 0, 0, 0, 0
        for a in column[i+1:]:
            if a < lines[i][j]: y2 += True
            else:
                y2 += True
                break
        for b in reversed(column[:i]):
            if b < lines[i][j]: y1 += True
            else:
                y1 += True
                break
        for c in lines[i][j+1:]:
            if c < lines[i][j]: x1 += True
            else:
                x1 += True
                break
        for d in reversed(lines[i][:j]):
            if d < lines[i][j]: x2 += True
            else:
                x2 += True
                break
        if maximum < x1*x2*y1*y2: maximum = x1*x2*y1*y2
print(maximum)