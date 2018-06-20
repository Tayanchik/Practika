import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

lit = input("Введіть букву: ")

if lit == 'a':
   print ("введена буква – голосна")

elif lit == 'e':
   print ("введена буква – голосна")

elif lit == 'i':
   print ("введена буква – голосна")

elif lit == 'o':
   print ("введена буква – голосна")

elif lit == 'u':
    print ("введена буква – голосна")

elif lit == 'y':
   print ("введена буква інколи y – голосна, а інколи")

else:
   print("введена буква - приголосна")
printTimeStamp("Дорошенко і Старова")
