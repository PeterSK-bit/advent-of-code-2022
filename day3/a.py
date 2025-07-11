with open("data.txt", "r") as f:
    rucksacks = f.readlines()

score = 0
points = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

for rucksack in rucksacks:
    c1, c2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for i in points:
        if(c1.find(i) != -1 and c2.find(i) != -1):
            score += points.index(i) + 1

print(score)    