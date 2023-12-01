
import re 
with open(r"C:\Users\Nutzer\Desktop\VM_Projekte\AdventOfCode2023\ChristianGreissl\Day1.txt") as f:
    inputsstring = f.read().split("\n")




def partOne(inputs):
    solutions= []
    for ele in inputs:
        
        temp = (re.sub("[^0-9]", "", ele))
        print("Ele ist " +  ele + "   Temp ist " + temp)
        if len(temp)>=3:
            solutions.append(int(temp[0]+temp[-1]))
            print(solutions[-1])
            continue
        temp = int(temp)
        if( temp <10):
            solutions.append(temp*10+temp)
            print(solutions[-1])
        else:
            solutions.append(temp)
            print(solutions[-1])

    print(sum(solutions))
    solution = sum(solutions)
    return solution

 

def partTwo(inputs):
    transformed = []

    ele = ""
    for elee in inputs:
        for char in elee: 
     
            ele += char
            ele=  ele.replace("one", "1ne")
            ele=  ele.replace("two","2wo")
            ele=  ele.replace("three", "3hree")
            ele=  ele.replace("four","4our")
            ele=  ele.replace("five", "5ive")
            ele=  ele.replace("six","6ix")
            ele=  ele.replace("seven", "7even")
            ele=  ele.replace("eight","8ight")
            ele=  ele.replace("nine","9ine")       
        transformed.append(ele)
        ele = ""

    return transformed

transformed = partTwo(inputsstring)
print(transformed)
partOne(transformed)