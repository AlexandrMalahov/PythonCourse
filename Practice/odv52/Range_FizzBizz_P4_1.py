"""
Напишите программу, которая выводит на экран числа от 1 до 100. При этом вместо чисел,
кратных трем, программа должна выводить слово Fizz, а вместо чисел, кратных пяти —
слово Buzz. Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz.
"""
x = range(1, 101)

def check(x):
    for i in x:
        if i % 3 == 0:
            i = 'Fizz'
        elif i % 5 == 0:
            i = 'Buzz'
        elif i % 15 == 0:
            i = 'FizzBuzz'
        print(i)
check(x)
