import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

x = int(input("Введіть к-ть кубометрів: "))
money = 20
if x <= 30:
    money += x * 9.86
elif 30 < x <= 50:
    money += (30 * 9.86) + (x - 10) * 11.22
elif 50 < x <= 60:
    money += (30 * 9.86) + (20 * 11.22) + (x - 50) * 13.06
elif x > 60:
    money += (30 * 9.86) + (20 * 11.22) + (10 * 13.06) + (x - 60) * 17.89

print("Потрібно заплатити: %.2f грн" % money)



printTimeStamp("Дорошенко і Старова")

