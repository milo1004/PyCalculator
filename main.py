import math
import time
import sys
import decimal
import os
print("Welcome to Calculator")
time.sleep(1)
while True:
    print('Please enter the formula below (Please use these symbols: + - * /)(type "exit" to exit program.)')
    fx = input("Formual:")
    if fx == "exit":
        print("See you next time!")
        time.sleep(1)
        os.system('cls')
        sys.exit()
    else:
        ans = eval(fx)
        print(f"The answer is: {ans}")
        time.sleep(1)