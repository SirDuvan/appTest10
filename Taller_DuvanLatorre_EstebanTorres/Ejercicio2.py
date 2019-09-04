i = 3
num1 = 0
num2 = 1
suma = 0

print("1 : ",num1)
print("2 : ",num2)
    
while i <= 20:
   suma = num1 + num2
   print(i,": ",suma)
   num1=num2
   num2=suma
   i = i+1
