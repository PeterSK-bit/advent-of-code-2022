with open("data.txt", "r") as f:
    rucksacks = f.readlines()

score = 0
points = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
team = []

for i in range(0, len(rucksacks), 3):
    team = (rucksacks[i:i+3])
    for j in points:    
        if(team[0].find(j) != -1 and team[1].find(j) != -1 and team[2].find(j) != -1):
            score += points.index(j) + 1

print(score)