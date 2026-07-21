# Actividad 3 - Fuerza Bruta Alfabética
# Explicación:
# Utilizaremos fuerza bruta para determinar cuántos intentos son necesarios para encontrar combinaciones.
# Intentará todas las combinaciones de letras posibles, en orden alfabético, letra por letra.

from string import ascii_lowercase
import time

print(f"Abecedario: {ascii_lowercase}")

intentos = 0
password_encontrado = ''

password_oculto = input("\nIngrese la contraseña a buscar: ").strip().lower()

print("\nIniciando ataque de fuerza bruta...")
time.sleep(1)

for letra_secreta in password_oculto:

    for letra_prueba in ascii_lowercase:
        intentos += 1

        print(f"Probando combinación: {password_encontrado}{letra_prueba} (Intento {intentos})", end="\r")
        time.sleep(0.05)

        if letra_prueba == letra_secreta:
            password_encontrado += letra_prueba
            break

print(f"\nLa contraseña fue forzada en {intentos} intentos")
print(f"Contraseña encontrada: {password_encontrado}")