import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть температуру в градусах  Цельсія: "))

print("Температура в градусах Фаренгейта: ",(a*1.8)+32,"F")
print("Температура в градусах Кельвіна: ",a+273.15,"K")

printTimeStamp("Дорошенко і Старова")
