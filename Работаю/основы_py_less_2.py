# форматирование с помощью % и %s(string), %d(decimal), %f(float), где % означает забрать данные из какой-либо
# переменной, а буквы означают тип данного в переменной.
a = 'collection'
b = 'cup'
c = 'money'
#d = '{%s|%s|%s}' % (a, b, c)
#print(d)
#w = '{{{}|{}|{}}}'.format(a, b, c) # данный способ позволяет интерпретатору самому разобраться c тимпом переменной
#q = '{{{2}|{1}|{0}}}'.format(a, b, c) #  также можно выставить необходимое расположение значений
#print(w)
#x = f"{a}----{b}----{c}" #самое удобное форматирование
#print(x)
# относительно массивов
#print(m*3) # пример дублирования массива
#print(m + [6, 7, 8]) # сложение двух массивов, вычитание не известно
# работа с replace
#s = "How i want to go in America, Europe, Ucraine"
#g = s.replace("How", "a lot of")
#print(g)
#c = a.replace(str(a[1]), 4)
#print(c)
#работаю с множествами
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
s = {1, }.intersection()