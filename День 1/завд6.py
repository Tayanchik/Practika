import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = float(input("Введіть вартість їжі: "))
print("Чайові: ", a*0.14)
print("Податок: ", a*0.18)
print("Загальна сума: ", a+(a*0.14)+(a*0.18))
printTimeStamp("Дорошенко і Старова")
