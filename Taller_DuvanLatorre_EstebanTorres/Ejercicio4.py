res = 0

while res <= 100:
    print("Digite número: ")
    num = int(input())
    t = num + res
    res = t
    print("La suma es: ", res)

print ("La suma sobrepaso el limite de 100")
