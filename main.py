#!/usr/bin/env python3
from Model.sumadora import Sumadora

import view

while True:
    #view.tabla()
    view.tabla_H()
    Sumadora.main()
    e = input("Nueva Operacion(y/n); default(y).\n>_").lower()
    if e == "n": break
    view.refescar()