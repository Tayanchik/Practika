import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


summ = 0
summ_num = 0
try:
    while True:
        num = int(input("Введіть будь-яке число: "))
if num == 0:
    print("Введіть 0, щоб завершити програму: ")
        break
    summ += 1
    summ_num += num
except:
    print("Ти ввів перший 0")

print("Середнє значення = " + str(summ_num / summ))

printTimeStamp("Дорошенко і Старова")
