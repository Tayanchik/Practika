import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть об'єм контейнера: "))
b = float(input("Введть к-ть контецнерів: "))
if a <= 1:
    print((b*a)*0.1, "$")
elif a>= 1:
    print((a*b)*0.25, "$")

print(((b*a)*0.1)+((a*b)*0.25), "$")
printTimeStamp("Дорошенко і Старова")
