print ("Digite el número del cual quiere visualizar el factorial: ")
x = int(input())
i = 1
while x >= 1:
    i = x * i
    x = x - 1

print ("El resultado es: " , i)