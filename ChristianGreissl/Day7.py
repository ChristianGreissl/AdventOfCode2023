
left = []
right = []
with open(r'C:\Users\Nutzer\Desktop\VM_Projekte\AdventOfCode2023\ChristianGreissl\test.txt') as f :
    for line in f:
        l, r = line.strip().split(" ")
        left.append(l)
        right.append(r)

left.sort()



















print(left, right)