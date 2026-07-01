# Sentencias Condicionales (IF / ELIF / ELSE)

print('--- Estructura IF / ELSE ---')


password = '1234'
if len(password) > 6:
    if len(password) <= 20:
        print('Password aceptado!!')
    else:
        print('Error: El password es muy largo')
else:
    print('Error: El password ingresado es muy corto')



if password == '12345':
    print('Acceso concedido')
else:
    print('Acceso denegado')



# Estructura con ELIF

valor_str = '0'
valor = int(valor_str)

if valor == 0:
    print('Este número es cero')
elif valor % 2 == 0:
    print('Este es un número par')
else:
    print('Este es un número impar')

print('\n\n')

edad = 27
tiene_entrada = True

if (edad >= 18) and (tiene_entrada):
    print('Puede ingresar')
else:
    print('No puede ingresar')


# Otra forma de escribir parecido a estructura de IF / ELIF / ELSE
if valor == 0: print('Este número es cero')
if valor % 2 == 0: print('Este es un número par')
if valor % 2 != 0: print('Este es un número impar')