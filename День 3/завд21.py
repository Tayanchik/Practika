import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

t = open("Gucci.txt", 'a')
t.write("Gucci gang, Gucci gang!")

t.close()
printTimeStamp("Дорошенко і Старова")
