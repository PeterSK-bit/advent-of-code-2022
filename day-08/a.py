visible=0
lines=[]

with open("data.txt", "r") as f:
    for i in range(99):
        lines.append(f.readline().replace("\n",""))

for i in range(1, len(lines) -1):
    for j in range(1, len(lines[0]) -1):
        column = []
        for k in range(len(lines)):
            column.append(lines[k][j])
        if max(lines[i][:j]) < lines[i][j] or max(lines[i][j+1:]) < lines[i][j] or max(column[:i]) < lines[i][j] or max(column[i+1:]) < lines[i][j]:
            visible += True
            
print(visible - 4 + (len(lines) + len(lines[0])) *2)