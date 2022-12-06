#EASY

#Задание-1.

#import ast
#entry = input()
#list = ast.literal_eval(entry)
#square_list = [i**2 for i in list]
#print(square_list)

#Задание-2.

#fruits_1 = ["банан", "киви", "яблоко", "никторин"]
#fruits_2 = ["персик", "айва", "банан", "яблоко"]
#fruits_3 = [i for i in fruits_1 if i in fruits_2]
#print(fruits_3)

#Задание-3.

#import random
#some_digits = []
#while len(some_digits) <= 20:
    #i = random.randint(-20, 20)
    #some_digits.append(i)
#necessary_digits = [i for i in some_digits if i % 3 == 0 and i % 4 != 0 and i > 0 ]
#print(necessary_digits)

#Normal

#Задание-1.
import random
with open("scoreboard.txt", "a") as f:
    i = 0
    while i <= 2500:
        number = random.randint(0, 10)
        f.write(str(number))
        i+=1