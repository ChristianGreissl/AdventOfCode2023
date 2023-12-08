

with open (r'C:\Users\Nutzer\Desktop\VM_Projekte\AdventOfCode2023\ChristianGreissl\test.txt') as f:
    operations = f.readline()
    rest = [line for line in f.read().split("\n") if line]



operations_list = [char for char in operations if char != "\n"]
i = rest.index("AAA%")
for ele in rest:
    if ele[0:3] == "AAA":
        print(ele, )

for i in range(len(rest)):
    operator = operations_list[i]
    map_anweisung = rest[i]









print(operations_list, rest)
