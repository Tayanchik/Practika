import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть кількість штучок: "))
b = float(input("Введіть кількість штукенцій: "))

print(a*75)
print(b*112)
print((a*75)+(b*112))
printTimeStamp("Дорошенко і Старова")
