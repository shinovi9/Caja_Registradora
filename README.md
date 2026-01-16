# Caja_Registradora

### Descripción del proyecto

El proyecto implementa una caja registradora digital que verifica que un usuario complete correctamente un pago. Soporta pagos en múltiples monedas y realiza conversiones automáticas hacia la moneda base para asegurar que el monto requerido se cubra de forma precisa. Está diseñado siguiendo la arquitectura MVVM para separar claramente la lógica de negocio, la presentación y la capa que conecta ambas.

---

### Arquitectura MVVM

- Model: contiene la lógica de negocio y acceso a datos (por ejemplo, la clase Tasa que carga y expone las tasas de cambio desde una fuente persistente).
- ViewModel: orquesta la lógica entre Model y View; expone estados y comandos que la vista consume.
- View: interfaz de usuario (CLI, GUI o web) que muestra el estado y recibe entradas del usuario.
- Data: almacenamiento de recursos como baseDatos_Tasas.json que alimenta la capa Model.
Esta separación facilita pruebas unitarias, mantenimiento y evolución del sistema sin acoplar la UI a la lógica de negocio.

---

### Parámetros principales

- Pago total requerido: monto que debe cubrir el usuario en la moneda base.
- Diccionario de tasas de cambio: mapea códigos de moneda a su equivalencia respecto a la moneda base. Ejemplo:

```python
{'CUP': 1.00, 'USD': 450.00, 'EUR': 490.00}
```

- Entradas de pago del usuario: secuencia de montos y monedas que el usuario introduce para completar el pago.

---

### Moneda base y conversiones

- Moneda base por defecto: CUP.
- Los pagos introducidos en otras monedas se convierten a CUP usando las tasas definidas en la capa Model (clase Tasa) y se suman al acumulado en CUP.
- Todas las comparaciones y cálculos de cambio se realizan en la moneda base para evitar inconsistencias.

---

### Flujo de trabajo

- El sistema recibe el pago total (en CUP) y carga las tasas de cambio desde la fuente de datos.
- El usuario introduce una entrada de pago indicando monto y moneda.
- El ViewModel solicita al Model (p. ej. Tasa) la conversión del monto a CUP y actualiza el acumulado.
- Si el acumulado es igual o superior al pago total, la operación finaliza y se calcula el cambio en CUP.
- Si el acumulado es menor, el sistema solicita nuevas entradas hasta completar el pago.

---

#### Estructura recomendada del proyecto

```
Caja_Registradora/
├── Data/
│   │   
│   ├── baseDatos_Tasas/
│   │   └── Tasas.json
│   └── .gitkeep
│
├── Model/
│   ├── monto.py
│   ├── pago.py
│   └── tasa.py
│
├── ViewModel/
│   └── viewmodel.py    # coordina Vista ↔ Model
│
├── View/
│   └── view.py         # interfaz CLI o futura GUI
│
├── main.py             # punto de entrada de la aplicación
├── requirements.txt
├── .gitignore
├── .gitattributes
├── LICENSE
└── README.md
```