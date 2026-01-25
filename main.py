#!/usr/bin/env python3
from Model.sumadora import Sumadora

import view

while True:
    view.printHeader()
    #view.tabla()
    view.tabla_H()
    Sumadora.main()
    e = input("Nueva Operación(y/n); default(y).\n>_").lower()
    if e == "n": break
    view.refrescar()