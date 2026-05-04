# 🍕 Ejercicio 1: Sistema de Pedidos Nocturnos (Estilo Clínica / Cálculos)
# Tienes que programar la terminal de autoservicio para una pizzería. El sistema debe calcular el total a pagar dependiendo de las opciones elegidas y aplicar validaciones estrictas.

# Requerimientos del programa:

# Protección: Todo el código principal debe estar dentro de un try/except.

# Validación de edad: Primero, pregunta la edad del cliente. Si la edad es menor a 18 o mayor a 100, imprime "Error: Edad no válida o cliente menor de edad" y el programa termina (todo lo demás debe ir tabulado adentro si pasa esta prueba).

# Selección de Pizza: Si la edad es correcta, pide ingresar la opción de pizza:

# Opción 1: Chicken BBQ ($12.000)

# Opción 2: Canadian Bacon ($10.000)

# Opción 3: De La Casa ($14.000)

# Si ingresa un número que no sea 1, 2 o 3, imprime "Error: Opción inválida" y termina.

# El Agregado: Pregunta si desea agregar Palitos de Ajo (Ingresar 1 para Sí, 2 para No).

# Si es 1, se le suman $3.000 al total. Si es 2, se suman $0.

# Salida Final: Limpia la pantalla (puedes usar el os.system("cls") que aprendiste) e imprime la boleta con el tipo de pizza seleccionada, si lleva agregado, y el Total a Pagar definitivo.

import os
os.system("cls")

try:
    nombre = input("Ingrese su nombre \n")
    edad = int(input("Ingrese su edad \n"))
    if edad >= 18 and edad <= 100:
        pizza = int(input("Seleccione su pizza \n 1. Chicken BBQ \n 2. Canadian Bacon \n 3. De la Casa \n"))
        if pizza > 0 and pizza <= 3:
            if pizza == 1:
                tipo_pizza = "Chicken BBQ"
                precio = 12000
            elif pizza == 2:
                tipo_pizza = "Canadian Bacon"
                precio = 10000
            elif pizza == 3:
                tipo_pizza = "De la Casa"
                precio = 14000
            else:
                print("Error: Opción inválida")
            agregado = int(input("Desea agregar Palitos de Ajo? \n 1. Si \n 2. No \n"))
            if agregado == 1 or agregado == 2:
                if agregado == 1:
                    palitos = 3000
                    palitos_str = "Si"
                elif agregado == 2:
                    palitos = 0
                    palitos_str = "No"
                valor = precio + palitos
                os.system("cls")
                print(f"Nombre cliente: {nombre}")
                print(f"Pizza a llevar: {tipo_pizza}")
                print(f"Lleva Palitos de Ajo: {palitos_str}")
                print(f"Total a pagar: ${valor}")
            else:
                print("Valor debe ser 1 o 2")
        else:
            print("Valor debe ser entre 1 a 3")
    else:
        print("Error: Edad no válida o cliente menor de edad")
except:
    print("Valor debe ser numérico")