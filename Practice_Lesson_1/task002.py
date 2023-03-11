# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

a = 5
array = []
max = 0

for i in range(a):
    z = int(input("Введите число:"))
    array.append(z)
    if array[i] > max:
        max = array[i]
    
 
print (array)
    

print ("Max value =", max)

