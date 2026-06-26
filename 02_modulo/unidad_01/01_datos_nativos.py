print("Hola Mundo!")

# 1. Declaración de Variables
nombre_usuario = 'Juanito'      # str (String / Cadena de texto)
edad_usuario = 31               # int (Integer / Entero)
estatura_metros = 1.82          # float (Float / Decimal)
es_instructor = True            # bool (Boolean / True o False)

# 2. Inspección de Tipos de Variables con type()
print(f"La variable 'nombre_usuario' es de tipo: {type(nombre_usuario)}")
print(f"La variable 'edad_usuario' es de tipo: {type(edad_usuario)}")
print(f"La variable 'estatura_metros' es de tipo: {type(estatura_metros)}")
print(f"La variable 'es_instructor' es de tipo: {type(es_instructor)}")

# 3. Mutabilidad de Variables (Las variables cambian de tipo dinámicamente)
dato_flexible = "Soy un texto"
print(f"\nValor inicial: {dato_flexible} -> Tipo: {type(dato_flexible)}")

dato_flexible = 42
print(f"Valor reasignado: {dato_flexible} -> Tipo: {type(dato_flexible)}")

# 4. Interacción con usuario mediante input()
print("\n--- Captura de Datos ---")
# Los datos capturas por input() siempre son de tipo 'str', independientemente de lo escrito
ciudad = input("Por favor, ingrese su ciudad de origen:\n> ")
fecha_nacimiento_str = input("Ingrese su año de nacimiento (Ej: 1995):\n> ")

print("\nDatos recibidos:")
print(f"Ciudad: {ciudad} -> Tipo: {type(ciudad)}")
print(f"Año: {fecha_nacimiento_str} -> Tipo: {type(fecha_nacimiento_str)}")

# 5. Formateo en Multilinea
print("\n--- Resumen del Perfil ---")
print(f"""
    Ficha Técnica del Alumno
    --------------------------
    Nombre      : {nombre_usuario}
    Edad        : {edad_usuario}
    Estatura    : {estatura_metros} m
    Reside en   : {ciudad}    
    """)
