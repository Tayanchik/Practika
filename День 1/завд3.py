import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть тиск у кПа: "))

print("Тиск у фунтах на квадратний дюйм: ",a*0.14505367 , "фт/дм2")
print("Тиск у міліметрах ртутного стовпчика: ",a*7.500638 , "мм рт. ст.")
print("Тиск у атмосферах: ",a*0.00986923 , "атм")
printTimeStamp("Дорошенко і Старова")
