import random

pool = [n for n in range(1, 42)]

def sacar_numero(posicion):
    global pool

    elegido = random.choice(pool) # Elegir un número al azar
    pool.remove(elegido)
    print(f"El {posicion} es {elegido}")
    # print(pool)

print("--- Iniciando Sorteo ---")
sacar_numero("primer número")
sacar_numero("segundo número")
sacar_numero("tercer número")
sacar_numero("cuarto número")
sacar_numero("quinto número")
sacar_numero("sexto número")

elegido_comodin = random.choice(pool)
pool.remove(elegido_comodin)
print(f"El comodín número es {elegido_comodin}")
print(pool)