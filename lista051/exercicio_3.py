'''3) Desenvolver um programa que apresente os quadrados dos números inteiros de 15 a 200.'''
import math

cont = 15
while (cont <= 200):
    print(f"O contador elevado a 2 é = {(math.pow(cont,2)):.0f}")
    cont = cont+ 1