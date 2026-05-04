# 💣 Ejercicio 2: Sabotaje M-COM en Battlefield 6 (Estilo Rango / Cascadas)
# Estás infiltrado en la base enemiga y tienes que hackear la estación M-COM para que tu patrulla pueda avanzar. El sistema de la bomba tiene un código dinámico y solo te da 3 intentos antes de bloquearse y alertar al enemigo.

# Requerimientos del programa:

# Generación: El sistema genera un código secreto aleatorio entre 1 y 50.

# El Glitch: Si el número generado es par (codigo % 2 == 0), el sistema de seguridad le resta 1 automáticamente para volverlo impar.

# Protección: Obligatorio el try/except general.

# Intento 1: Pide ingresar el código. Usa el guardia de seguridad (if envolvente) para validar que el número esté entre 1 y 50. Si está fuera de rango, imprime "Error de tipeo. Alarma activada." y termina. Si está en rango:

# Si adivina: "M-COM Desactivada. Buen trabajo."

# Si falla: Imprime "Código erróneo" y avisa si el código secreto es mayor o menor.

# Intento 2: Pide un nuevo número.

# Si adivina: "M-COM Desactivada. Buen trabajo."

# Si falla: "Código erróneo", avisa si es mayor o menor, y usa la función abs() para imprimir la advertencia: "Peligro: El pulso está a [distancia] dígitos de detonar".

# Intento 3: Último intento de hackeo.

# Si adivina: "M-COM Desactivada. Buen trabajo."

# Si falla: "Misión Fallida. El código era [código]".

from random import randint

codigo = randint(1,50)
if codigo % 2 == 0:
    codigo = codigo - 1
try:
    intento1 = int(input("Ingrese el código \n"))
    if intento1 > 0 and intento1 <= 50:
        if intento1 == codigo:
            print("M-COM Desactivada. Buen trabajo")
        else:
            print("Código erróneo")
            if codigo > intento1:
                print("El código es mayor")
            else:
                print("El código es menor")
            intento2 = int(input("Ingrese el código \n"))
            if intento2 == codigo:
                print("M-COM Desactivada. Buen trabajo")
            else:
                print("Código erróneo")
                if codigo > intento2:
                    print("El código es mayor")
                else:
                    print("El código es menor")
                distancia = abs(codigo - intento2)
                print(f"Peligro: El pulso está a {distancia} dígitos de detonar")
                intento3 = int(input("Ingrese el código \n"))
                if intento3 == codigo:
                    print("M-COM Desactivada. Buen trabajo")
                else:
                    print(f"Misión Fallida. El código era {codigo}")
    else:
        print("Número debe estar dentro del rango 1-50")
except:
    print("Valor debe ser un número")