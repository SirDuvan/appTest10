'''Duvan Latorre - Esteban Torres'''
from random import randint, uniform, random

def ra():
    a = randint(1,6)
    return a

players = []
points = []

'''def basico():
    i = 1
    suma = 0  

    while (suma <= 2):
        i = 1
        while (i <= jg):   
            print("")     
            print("Jugador ", i, ": Presione enter para jugar")
            players.append(i)
            key = input()
            d1 = ra()
            d2 = ra()
            print("Dado 1: " , d1 , " Dado 2: " , d2)
            r = d1 + d2
            
            print("Avanza: ", r , " Espacios")
            print("")
     
            points.insert(i,r)
        
              
            for j in points:
                suma = suma + j
                print(points.count(suma)) 
            i = i + 1'''


   


    
        
def basico():
    if(jg == 2):
        sum1 = 0
        sum2 = 0
        
        while((sum1 or sum2) <= 20):
            print("Jugador 1 Presione enter para jugar.")
            key = input()
            d1 = ra()
            d2 = ra()
            print("Dado 1: " , d1 , " Dado 2: " , d2)
            r1 = d1 + d2
            sum1 = r1 + sum1
            print("Alcanzo la posición: ", sum1)
            if(sum1 >= 20):
                print("¡¡¡Felicitaciones al jugador 1!!!")
                break
                        
                            
                                    

            print("Jugador 2 Presione enter para jugar")
            key = input()
            d3 = ra()
            d4 = ra()
            print("Dado 1: " , d3 , " Dado 2: " , d4)
            r2 = d3 + d4
            sum2 = r2 + sum2
            print("Alcanzo la posición: ", sum2)

            if(sum2 >= 20):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break              
        
    elif(jg == 3):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        
        while((sum1 or sum2 or sum3) <= 20):
            print("Jugador 1 Presione enter para jugar.")
            key = input()
            d1 = ra()
            d2 = ra()
            print("Dado 1: " , d1 , " Dado 2: " , d2)
            r1 = d1 + d2
            sum1 = r1 + sum1
            print("Alcanzo la posición: ", sum1)
            if(sum1 >= 20):
                print("¡¡¡Felicitaciones al jugador 1!!!")
                break
                            

            print("Jugador 2 Presione enter para jugar")
            key = input()
            d3 = ra()
            d4 = ra()
            print("Dado 1: " , d3 , " Dado 2: " , d4)
            r2 = d3 + d4
            sum2 = r2 + sum2
            print("Alcanzo la posición: ", sum2)

            if(sum2 >= 20):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
                    
            print("Jugador 3 Presione enter para jugar")
            key = input()
            d5 = ra()
            d6 = ra()
            print("Dado 1: " , d5 , " Dado 2: " , d6)
            r3 = d5 + d6
            sum3 = r3 + sum3
            print("Alcanzo la posición: ", sum3)

            if(sum3 >= 20):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
            
    else:
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        while((sum1 or sum2 or sum3 or sum4) <= 20):
            print("Jugador 1 Presione enter para jugar.")
            key = input()
            d1 = ra()
            d2 = ra()
            print("Dado 1: " , d1 , " Dado 2: " , d2)
            r1 = d1 + d2
            sum1 = r1 + sum1
            print("Alcanzo la posición: ", sum1)
            if(sum1 >= 20):
                print("¡¡¡Felicitaciones al jugador 1!!!")
                break
                            

            print("Jugador 2 Presione enter para jugar")
            key = input()
            d3 = ra()
            d4 = ra()
            print("Dado 1: " , d3 , " Dado 2: " , d4)
            r2 = d3 + d4
            sum2 = r2 + sum2
            print("Alcanzo la posición: ", sum2)

            if(sum2 >= 20):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
                    
            print("Jugador 3 Presione enter para jugar")
            key = input()
            d5 = ra()
            d6 = ra()
            print("Dado 1: " , d5 , " Dado 2: " , d6)
            r3 = d5 + d6
            sum3 = r3 + sum3
            print("Alcanzo la posición: ", sum3)

            if(sum3 >= 20):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
                    
            print("Jugador 4 Presione enter para jugar")
            key = input()
            d7 = ra()
            d8 = ra()
            print("Dado 1: " , d7 , " Dado 2: " , d8)
            r4 = d7 + d8
            sum4 = r4 + sum4
            print("Alcanzo la posición: ", sum4)

            if(sum4 >= 20):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break            

def intermedio():
    if(jg == 2):
        sum1 = 0
        sum2 = 0
        
        while((sum1 or sum2) <= 30):
            print("Jugador 1 Presione enter para jugar.")
            key = input()
            d1 = ra()
            d2 = ra()
            print("Dado 1: " , d1 , " Dado 2: " , d2)
            r1 = d1 + d2
            sum1 = r1 + sum1
            print("Alcanzo la posición: ", sum1)
            if(sum1 >= 30):
                print("¡¡¡Felicitaciones al jugador 1!!!")
                break
                        
                            
                                    

            print("Jugador 2 Presione enter para jugar")
            key = input()
            d3 = ra()
            d4 = ra()
            print("Dado 1: " , d3 , " Dado 2: " , d4)
            r2 = d3 + d4
            sum2 = r2 + sum2
            print("Alcanzo la posición: ", sum2)

            if(sum2 >= 30):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break              
        
    elif(jg == 3):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        
        while((sum1 or sum2 or sum3) <= 30):
            print("Jugador 1 Presione enter para jugar.")
            key = input()
            d1 = ra()
            d2 = ra()
            print("Dado 1: " , d1 , " Dado 2: " , d2)
            r1 = d1 + d2
            sum1 = r1 + sum1
            print("Alcanzo la posición: ", sum1)
            if(sum1 >= 30):
                print("¡¡¡Felicitaciones al jugador 1!!!")
                break
                            

            print("Jugador 2 Presione enter para jugar")
            key = input()
            d3 = ra()
            d4 = ra()
            print("Dado 1: " , d3 , " Dado 2: " , d4)
            r2 = d3 + d4
            sum2 = r2 + sum2
            print("Alcanzo la posición: ", sum2)

            if(sum2 >= 30):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
                    
            print("Jugador 3 Presione enter para jugar")
            key = input()
            d5 = ra()
            d6 = ra()
            print("Dado 1: " , d5 , " Dado 2: " , d6)
            r3 = d5 + d6
            sum3 = r3 + sum3
            print("Alcanzo la posición: ", sum3)

            if(sum3 >= 30):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
            
    else:
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        while((sum1 or sum2 or sum3 or sum4) <= 30):
            print("Jugador 1 Presione enter para jugar.")
            key = input()
            d1 = ra()
            d2 = ra()
            print("Dado 1: " , d1 , " Dado 2: " , d2)
            r1 = d1 + d2
            sum1 = r1 + sum1
            print("Alcanzo la posición: ", sum1)
            if(sum1 >= 30):
                print("¡¡¡Felicitaciones al jugador 1!!!")
                break
                            

            print("Jugador 2 Presione enter para jugar")
            key = input()
            d3 = ra()
            d4 = ra()
            print("Dado 1: " , d3 , " Dado 2: " , d4)
            r2 = d3 + d4
            sum2 = r2 + sum2
            print("Alcanzo la posición: ", sum2)

            if(sum2 >= 30):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
                    
            print("Jugador 3 Presione enter para jugar")
            key = input()
            d5 = ra()
            d6 = ra()
            print("Dado 1: " , d5 , " Dado 2: " , d6)
            r3 = d5 + d6
            sum3 = r3 + sum3
            print("Alcanzo la posición: ", sum3)

            if(sum3 >= 30):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
                    
            print("Jugador 4 Presione enter para jugar")
            key = input()
            d7 = ra()
            d8 = ra()
            print("Dado 1: " , d7 , " Dado 2: " , d8)
            r4 = d7 + d8
            sum4 = r4 + sum4
            print("Alcanzo la posición: ", sum4)

            if(sum4 >= 30):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break            


def avanzado():
    if(jg == 2):
        sum1 = 0
        sum2 = 0
        
        while((sum1 or sum2) <= 50):
            print("Jugador 1 Presione enter para jugar.")
            key = input()
            d1 = ra()
            d2 = ra()
            print("Dado 1: " , d1 , " Dado 2: " , d2)
            r1 = d1 + d2
            sum1 = r1 + sum1
            print("Alcanzo la posición: ", sum1)
            if(sum1 >= 50):
                print("¡¡¡Felicitaciones al jugador 1!!!")
                break
                        
                            
                                    

            print("Jugador 2 Presione enter para jugar")
            key = input()
            d3 = ra()
            d4 = ra()
            print("Dado 1: " , d3 , " Dado 2: " , d4)
            r2 = d3 + d4
            sum2 = r2 + sum2
            print("Alcanzo la posición: ", sum2)

            if(sum2 >= 50):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break              
        
    elif(jg == 3):
        sum1 = 0
        sum2 = 0
        sum3 = 0
        
        while((sum1 or sum2 or sum3) <= 50):
            print("Jugador 1 Presione enter para jugar.")
            key = input()
            d1 = ra()
            d2 = ra()
            print("Dado 1: " , d1 , " Dado 2: " , d2)
            r1 = d1 + d2
            sum1 = r1 + sum1
            print("Alcanzo la posición: ", sum1)
            if(sum1 >= 50):
                print("¡¡¡Felicitaciones al jugador 1!!!")
                break
                            

            print("Jugador 2 Presione enter para jugar")
            key = input()
            d3 = ra()
            d4 = ra()
            print("Dado 1: " , d3 , " Dado 2: " , d4)
            r2 = d3 + d4
            sum2 = r2 + sum2
            print("Alcanzo la posición: ", sum2)

            if(sum2 >= 50):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
                    
            print("Jugador 3 Presione enter para jugar")
            key = input()
            d5 = ra()
            d6 = ra()
            print("Dado 1: " , d5 , " Dado 2: " , d6)
            r3 = d5 + d6
            sum3 = r3 + sum3
            print("Alcanzo la posición: ", sum3)

            if(sum3 >= 50):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
            
    else:
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        while((sum1 or sum2 or sum3 or sum4) <= 50):
            print("Jugador 1 Presione enter para jugar.")
            key = input()
            d1 = ra()
            d2 = ra()
            print("Dado 1: " , d1 , " Dado 2: " , d2)
            r1 = d1 + d2
            sum1 = r1 + sum1
            print("Alcanzo la posición: ", sum1)
            if(sum1 >= 50):
                print("¡¡¡Felicitaciones al jugador 1!!!")
                break
                            

            print("Jugador 2 Presione enter para jugar")
            key = input()
            d3 = ra()
            d4 = ra()
            print("Dado 1: " , d3 , " Dado 2: " , d4)
            r2 = d3 + d4
            sum2 = r2 + sum2
            print("Alcanzo la posición: ", sum2)

            if(sum2 >= 50):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
                    
            print("Jugador 3 Presione enter para jugar")
            key = input()
            d5 = ra()
            d6 = ra()
            print("Dado 1: " , d5 , " Dado 2: " , d6)
            r3 = d5 + d6
            sum3 = r3 + sum3
            print("Alcanzo la posición: ", sum3)

            if(sum3 >= 50):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break
                    
            print("Jugador 4 Presione enter para jugar")
            key = input()
            d7 = ra()
            d8 = ra()
            print("Dado 1: " , d7 , " Dado 2: " , d8)
            r4 = d7 + d8
            sum4 = r4 + sum4
            print("Alcanzo la posición: ", sum4)

            if(sum4 >= 50):
                print("¡¡¡Felicitaciones al jugador 2!!!")
                break            


def tablero():
    print(":::::Menú:::::")
    print("1. Nivel básico (Tablero de 20 posiciones)")
    print("2. Nivel intermedio (Tablero de 30 posiciones)")
    print("3. Nivel avanzado (Tablero de 50 posiciones)")
    print("Escoja el nivel de juego: ")
    nvl = int(input())
    if (nvl == 1):
        print("Nivel Basico")
        basico()
    elif(nvl == 2):
        print("Nivel Intermedio")
        intermedio()
    elif(nvl == 3):
        print("Nivel Avanzado")
        avanzado()     
    else:
        print("Digite una opción valida.")
        tablero()
    


print("::::Bienvenido a carrera numérica::::")
print("Digite la cantidad de jugadores: ")
jg = int(input())



if (jg < 2 ):
    print("El limite de jugadores es de 2 a 4.")
                
elif (jg > 4):
    print("El limite de jugadores es de 2 a 4.")
               
else:
    print(":::Carrera Numérica:::")
    tablero()