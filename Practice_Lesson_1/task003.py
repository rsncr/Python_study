# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

print ('Enter value for N:')
n = int(input())

print(list(range(-n,n+1)))