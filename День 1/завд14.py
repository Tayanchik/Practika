import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

mounth = ["Січень", "Березень", "Травень", "Липень", "Серпень", "Жовтень", "Грудень"]
mounthl = ["Квітень", "Червень", "Вересень", "Листопад"]
mounth2 = "Лютий"

mount = input("Введіть місяць: ")

if mount == mounth2:
    mount = "28 або 29 днів"
elif mount in mounthl:
    mount = "30 днів"
elif mount in mounth:
    mount = "31 день"
else:
    print("Помилка")
print("В місяці " + str(mount))

printTimeStamp("Дорошенко і Старова")
