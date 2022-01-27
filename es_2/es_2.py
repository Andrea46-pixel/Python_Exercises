#!/usr/bin/env python
# -*- coding: utf-8 -*-

input = int(input("Inserisci un numero"))

if input>0:
    for numero in range(input):
        print(numero)
else: 
    print("N deve essere maggiore di 0")

