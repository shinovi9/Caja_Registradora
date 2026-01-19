#!/usr/bin/env python3
from pago import Pago

while True:
    Pago.bandeja()
    e = input("Nueva Operacion(y/n); default(y).\n>_").lower()
    if e == "n": break