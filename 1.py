print('Введите имя')
name = input()
print('Введите фамилию')
surname = input()
print('Введите год рождения')
date = int(input())
print(name, surname, date, sep = '_')
name, surname = surname, name
date = date + 60
print(name, surname, date, sep = '_') 