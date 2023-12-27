with open(r"C:\Users\Nutzer\Desktop\VM_Projekte\AdventOfCode2023\ChristianGreissl\Day2.txt") as f:
    puzzle_input = f.read().split("\n")


condition = { 'red': 12, 'green': 13 , 'blue': 14 }

def partOne(puzzle_input):

    solution = []
    for ele in puzzle_input:
        valid = True
        id_ , line  = ele.split(":")
        id = id_.replace("Game", "")
        id = int(id)
        print(id_)
        for event in line.split(";"):
            for balls in event.split(","):
                number, color = balls.split()
                if int(number) > condition.get(color, 0):
                    valid = False
        if valid:
                solution.append(id)
    

    print(sum(solution))
  

      
 


def partTwo():
    solution = []
    for ele in puzzle_input:
        valid = True
        id_ , line  = ele.split(":")
        id = id_.replace("Game", "")
        id = int(id)
        print(id_)
        for event in line.split(";"):
            for balls in event.split(","):
                number, color = balls.split()
                if int(number) > condition.get(color, 0):
                    valid = False
        


partOne(puzzle_input)



