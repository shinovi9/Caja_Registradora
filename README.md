# Caja_Registradora

## Descripción del proyecto

El proyecto consiste en desarrollar un sistema de caja registradora digital que verifique que un usuario complete correctamente un pago. La aplicación soporta múltiples monedas y realiza conversiones automáticas hacia la moneda base del sistema para asegurar que el monto requerido se cubra de forma precisa.

---

Parámetros principales

- Pago total requerido: monto que debe cubrir el usuario.  
- Diccionario de tasas de cambio: mapea códigos de moneda a su equivalencia respecto a la moneda base. Ejemplo:  
  `python
  {'CUP': 1.00, 'USD': 450.00, 'EUR': 490.00}
  `  
- Entradas de pago del usuario: secuencia de montos y monedas que el usuario introduce para completar el pago.

---

Moneda base y conversiones

- La moneda base por defecto es CUP.  
- Cuando el usuario introduce un pago en otra moneda, el sistema convierte ese monto a CUP usando la tasa correspondiente del diccionario y lo suma al acumulado en CUP.

---

Flujo de trabajo

1. El sistema recibe el pago total y el diccionario de tasas.  
2. El usuario introduce una entrada de pago (monto y moneda).  
3. El sistema convierte la entrada a CUP y la añade al acumulado.  
4. Si el acumulado es igual al pago total, la operación finaliza.  
5. Si el acumulado es menor, el sistema solicita nuevas entradas hasta alcanzar o superar el pago total.