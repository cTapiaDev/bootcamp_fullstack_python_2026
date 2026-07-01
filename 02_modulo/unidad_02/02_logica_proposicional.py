# Lógica Proposicional (AND, OR, XOR)

print('--- Operador "AND" ----')
# AND es False a menos que AMBAS pruebas sean True
edad = 27
duracion_pololeo = 3

mayor_y_pololeando = (edad > 18) and (duracion_pololeo > 0) # True and True = True
print(f'¿Mayor de 18 AND pololeando? -> {mayor_y_pololeando}')

print('\n--- Operador "OR" ---')
# OR es True si AL MENOS UNA prueba es verdadera
duracion_uni = 6
exp_laboral = 4

# Postulación: Se requiere una carrera que dure al menos 6 años o experiencia mayor a 5
puede_postular = (duracion_uni >= 6) or (exp_laboral > 5) # True or False = True
print(f'¿Cumple requisito de Uni (>=6) OR exp (>5)? -> {puede_postular}')

print('\n--- Operador "^" (Exclusivo) ---')
# ^ es verdadero SOLO si A y B tienen resultados distintos
menor_28 = edad < 28 # True
exp_menor_3 = exp_laboral < 3 # False

aplica_beneficio_exclusivo = menor_28 ^ exp_menor_3
print(f'¿Cumple condición (menor_28 XOR exp_menor_3)? -> {aplica_beneficio_exclusivo}')