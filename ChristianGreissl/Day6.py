import math 


with open(r'C:\Entwicklung\Python\AdventOfCode2023\ChristianGreissl\Day6.txt') as f:
    inputs = f.read().split("\n")

time = [int(x) for x in inputs[0].split(" ") if x != "" and x != "Time:"]
distance = [int(x) for x in inputs[1].split(" ") if x != "" and x != "Distance:"]

def gettimes(timelist, distancelist):
    wins =  0 
    winlist= []

    j = 0
    for time in timelist:
    
        distance = distancelist[j]
        for i in range(time):
     
            sol = (time -i) * i 

            if sol > distance:
              
                wins += 1
            
              
        winlist.append(wins)
         
        
        wins = 0 
        j += 1
    return math.prod(winlist)
#print(gettimes(time, distance))
#print(gettimes([71530, 48938466], [940200, 261119210191063]))
def parttwo(time, distance):
    # time= 71530
    # distance= 940200
    for i in range(time):
        diff = time-i
        sol =  diff *i
        if ( sol > distance):
            print(i, time -i)
            print("solution ist " , time-i-i +1)
            break
parttwo(48938466, 261119210191063)