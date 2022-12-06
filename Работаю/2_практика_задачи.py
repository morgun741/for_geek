#import math
#"""Level easy"""
#"""Задача-1"""
#fabrics = ["silk", "velvet", "leather", "wool"]
#materials = ["wool", "wood", "metal", "silk"]
#for i in range(len(fabrics)):
    #if fabrics[i] in materials:
        #fabrics.remove(str(fabrics[i]))
        #print(fabrics)
#"""Задача-2"""
#i = 0
#while i < len(fabrics):
    #if fabrics[i] in materials:
        #fabrics.remove(fabrics[i])
        #print(fabrics)
    #i += 1
#"""Задача-3"""
#digits = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#numbers = []
#for i in range(len(digits)):
    #if digits[i] % 2 == 0:
        #numeral_1 = digits[i] / 4
        #numbers.append(numeral_1)
    #else:
        #numeral_2 = digits[i] * 2
        #numbers.append(numeral_2)
#print(digits)
#print(numbers)
#"""Level normal"""
#"""Задача-1"""
#digits = [4, 5, 6, 7, 8, -9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -81, 121]
#extracted_roots = []
#supportive_list = []
#i = 0
#while i < len(digits):
    #if digits[i] > 0:
        #root = math.sqrt(digits[i])
        #if root % 1 == 0 :
           #extracted_roots.append(int(root))
    #i += 1
#print(extracted_roots)
#Level hard
#Задача-1
#mport string
#text = input()
#lst_letters = list(string.ascii_letters)
#x = 0
#for i in range(len(lst_letters)):
    #if lst_letters[i] in text:
        #a = text.count(lst_letters[i])
        #x += a
#print(x)
#Задача-2
text_1 = input()
text_2 = input()
lst_1 = text_1.split(sep=None)
lst_2 = text_2.split(sep=None)
print(lst_1, lst_2)