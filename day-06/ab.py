#for part 1 use 4 instead of 14 in marked places 

with open("data.txt", "r") as f:
    line = f.readline()

for i in range(len(line) - 4):
    x = line[i:i + 14]
    count = 1

    for j in range(14):#4
        for k in range(j+1, 14):#4
            if(x[j] == x[k]): 
                count += 1
    if count == 1:
        print(i + 14)#4
        quit()