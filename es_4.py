#!/usr/bin/env python
# -*- coding: utf-8 -*-

input = int(input("Inserisci un numero: "))

print(f"Numeri pari fino a {input}")

if input>0:
    for numeri in range(input+1):
        if(numeri%2 ==0):
            print(numeri)
else: 
    print("N deve essere maggiore di 0")