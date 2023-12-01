# AOfC_Day_01

import csv

class Game:
    def __init__(self, organisation, name, year):
        self.organization = organisation
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.organization}({self.name}))"

class Renna:
    def __init__(self, calories):
        self.calories = calories



game_01 = Game("GDI", "AdventOfCode", 2023)



# print(game_01.organization, ': ', game_01.name, game_01.year)
# print(game_01)

#fileContent = open("EliseoAntonini\Data\input.txt", "r")
# print(fileContent.read())

#for data in fileContent:
#    print(data[3])

#fileContent.close()

'''
with open('EliseoAntonini\Data\input_feed.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
'''
'''
switch = Switch()
case_1 = lambda : "Eins"
case_2 = lambda : "Zwei"
case_3 = lambda : "Drei"
'''

with open('EliseoAntonini\Data\Calorie_Counting.txt', 'r') as calorieCount_file:
    csv_reader = csv.reader(calorieCount_file, delimiter=",")
    renna_1 = Renna(0)

    #renna_2 = Renna(0)
    #renna_3 = Renna(0)
    #renna_4 = Renna(0)
    #renna_5 = Renna(0)

    dict = {
      0: 'renna_1',
      1: 'renna_2',
      2: 'renna_3',
      3: 'renna_4',
      4: 'renna_4' 
      }

    
#def CountNumberOfAnimals():
   
    countNoData = 0
    for line in calorieCount_file.read().split('\n'):
            if (line) == '':
                countNoData += 1
                print(countNoData)
    


'''
    print('Total number of renne:', countNoData + 1)
    for line in calorieCount_file.read().split('\n'):
        countNoData += 1    
        if (line) != '': 
            renna_1.calories += int(line);
        else:
            continue
'''