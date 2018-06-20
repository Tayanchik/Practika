import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

print("Оберіть одиниці вимірування: ")
print("1. кг та м")
print("2. фунти та дюйми")
choice = input("Оберіть цифру(1/2): ")

if choice == '1':
   a = float(input("Введіть зріст у метрах: "))
   b = float(input("Введіть масу в кілограмах: "))
   print(b/a**2)
elif choice == '2':
   c = float(input("Введіть зріст в дюймах: "))
   d = float(input("Введіть масу у фунтах: "))
   print(703*(d/c**2))
printTimeStamp("Дорошенко і Старова")
