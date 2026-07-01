nombre = 'Juan'
edad = 30
n_hijos = 0
graduacion_colegio = 17
duracion_uni = 6
duracion_pololeo = 3
exp_laboral = 4

print(f"Perfil cargado: {nombre}, {edad} años, {exp_laboral} años de exp.")

# Operadores de Comparación
# Directos
es_mayor = edad >= 18
print(f"¿Es mayor de edad? -> {es_mayor}")

exp_distinta = exp_laboral != 4

tiene_hijos = n_hijos > 0
no_tiene_hijos = n_hijos == 0
print(f'¿Tiene hijos? -> {tiene_hijos}')
print(f'¿No tiene hijos? -> {no_tiene_hijos}')

me_llamo_juan = nombre == 'Juan'
print(f'¿El nombre es exactamente "Juan"? -> {me_llamo_juan}')
print(f'{type(me_llamo_juan)}')

# Comparación Indirecta
edad_grad_uni = graduacion_colegio + duracion_uni
se_graduo_tarde = edad_grad_uni >= 22
print(f'Edad estimada de graduación: {edad_grad_uni}')
print(f'¿Se graduó con 22 o más? -> {se_graduo_tarde}')