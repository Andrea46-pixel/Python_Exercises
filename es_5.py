#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydoc import doc


while True:
    n1 = int(input("Inserisci n1: "))
    n2 = int(input("Inserisci n2: "))
    if n1>0 and n2>0 and n2>n1:
        break
    print("Valori non accettabili. Requisiti:\nn1>0, n2>0, n2>n1")

for numeri in range(n1, n2+1, 1):
    print(numeri)
