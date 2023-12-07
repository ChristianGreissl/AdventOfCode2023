
with open(r'C:\Users\Nutzer\Desktop\VM_Projekte\AdventOfCode2023\Day4.txt') as f:
    puzzle = f.read().split("\n")

sol = 0

for card in puzzle:
    cards, numbers = card.split(":")

    left , right  = numbers.split("|")

    left_num = left.split(" ")
    right_num = right.split(" ")

    l = []
    r = []
    for ele in left_num:
        if ele == " ":
            continue
        if ele == "":
            continue
        l.append(int(ele)) 
    for ele in right_num:
        if ele == " ":
            continue
        if ele == "":
            continue
        r.append(int(ele)) 
    l.sort()
    r.sort()       
    print(l, r )
    hit = -1
    for x in l:
        for y in r:
            if (x==y):
                hit += 1
    if hit == -1:
        continue
    hits = 2**hit 
    print(hits)
    sol += hits
print(sol)       