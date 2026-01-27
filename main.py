#!/usr/bin/env python3
from Model.sumadora import Sumadora
from rich.prompt import Prompt
from View.view import *

while True:
    refrescar()
    printHeader()
    tabla_H()
    Sumadora.main()
    e = Prompt.ask("Nueva Operación." ,choices=["y","n"]).lower()
    if e == "n": break
