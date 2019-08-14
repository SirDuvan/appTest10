#Duvan Latorre Zapata
#Function1: multiplicación solicitando 2 números en consola

#libreria
import os

#funciones
def clac(a,b):
    n3 = a*b
    return n3
#Main
os.system("cls")
n1 = int(input("Press number 1: "))
n2 = int(input("Press number 2: "))

print("El resultado de la multiplicación es: ",clac(n1,n2))



