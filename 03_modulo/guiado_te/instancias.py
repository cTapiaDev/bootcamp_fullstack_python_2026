from te import Te

te1 = Te()
te2 = Te()

tipo1 = type(te1)
tipo2 = type(te2)

print(f"Tipo de dato de te1: {tipo1}")
print(f"Tipo de dato de te2: {tipo2}")

if tipo1 == tipo2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")