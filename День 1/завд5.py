import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

a = input("Введіть ваше ім'я: ")

print("Привіт",a,"!")
printTimeStamp("Дорошенко і Старова")
