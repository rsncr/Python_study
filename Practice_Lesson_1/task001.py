# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.

print ('Enter value for a:')
a = int(input())
print ('Enter value for b:')
b = int(input())

if a*a == b:
    print ("YES")
else:
    print ("NO")