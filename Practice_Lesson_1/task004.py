# Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.

print ('Enter fractional value:')
n = float(input())

n2 = int(n * 10 % 10)

print(n2)