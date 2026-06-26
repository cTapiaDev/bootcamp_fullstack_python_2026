
# 1. Lista Heterogénea
# Mantiene el orden de inserción y permite datos duplicados.
alumnos_matriculados = ["Camila", "Antonio", "Felipe", "Antonia", "Antonio"] # Arreglo de Datos
print(f"Lista Base de Alumnos: {alumnos_matriculados}")

# 2. Indexación
print(f"Primer Alumno (índice 0)    : {alumnos_matriculados[0]}")
print(f"Tercer Alumno (índice 2)    : {alumnos_matriculados[2]}")

print(f"Último Alumno (índice -1)   : {alumnos_matriculados[-1]}")
print(f"Penúltimo Alumno (índice -2): {alumnos_matriculados[-2]}\n")

# 3. Mutabilidad: Modificación Directa
alumnos_matriculados[1] = "Juan"
print(f"Lista modificada (índice 1 cambiado): {alumnos_matriculados}")

# 4. Operación de Inserción
# .append() añade un elemento al final de la lista.
alumnos_matriculados.append("Daniela")
print(f"Append: {alumnos_matriculados}")

# .insert() me permite seleccionar el índice y desplaza al resto
alumnos_matriculados.insert(2, "Vicente")
print(f"Insert: {alumnos_matriculados}\n")

# 5. Operaciones de Eliminación
# .pop() remueve y retorna el último elemento de la lista.
alumno_egresado = alumnos_matriculados.pop()
print(f"Elemento removido con pop(): {alumno_egresado}")
print(f"Lista actualizada: {alumnos_matriculados}\n")

alumnos_matriculados.insert(2, "Antonio")
print(f"Doble Antonio: {alumnos_matriculados}")

# .remove() elimina la primera ocurrencia de un dato específico.
alumnos_matriculados.remove("Antonio")
print(f"Remove: {alumnos_matriculados}")

# 6. Función de Diagnóstico de Listas
longitud = len(alumnos_matriculados)
print(f"\nCantidad actual de alumnos: {longitud}")