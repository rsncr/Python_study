# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным

print('Enter value for weekday from 1 to 7')
a = int(input())

if 5 < a < 8:
    print('The day is a weekend')
else:
    print('The day is a working day')
if a > 7:
    print('Error. Enter value for weekday from 1 to 7')
