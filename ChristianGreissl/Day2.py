with open(r"C:\Users\Nutzer\Desktop\VM_Projekte\AdventOfCode2023\ChristianGreissl\Day2.txt") as f:
    puzzle_input = f.read().split("\n")


condition = { 'red': 12, 'green': 13 , 'blue': 14 }

def partOne(puzzle_input):

    solution = []
    for ele in puzzle_input:
        parts = ele.split(":")
        valid = True
        gameid = parts[0]
        gameid = gameid.replace("Game", "")
        mengen = parts[1].split(";")
        print(gameid, mengen)
        for kart in mengen:
            single = kart.split(",")
            for farbe in single:
                two = farbe.split(" ")
                number = two[1]
                number = int(number)
                color = two[2]
                if(number >= 15):
                   valid = False
                   continue
                if (number == 14) and (color !="blue"):
                    valid= False
                if(number==13 and color!="green"):
                    valid = False
        if(valid):
            solution.append(gameid)


      
 


def partTwo():
    pass


partOne(puzzle_input)



