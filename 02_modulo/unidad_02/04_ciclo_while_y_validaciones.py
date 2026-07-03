import time
import getpass

# While
# Nos mantenemos dentro del ciclo mientras la condición sea True
segundos_restantes = 5

print('Iniciando despliegue en servidor...')
while segundos_restantes > 0:
    print(f'Despliegue en: {segundos_restantes}...')
    # time.sleep(1)
    segundos_restantes -= 1

print('¡Despliegue completado!')

# --- Acumular Datos ---
archivos_a_procesar = 4
archivos_procesados = 0
peso_total_acumulado = 0

# while archivos_procesados < archivos_a_procesar:
#     peso_archivo = float(input(f'Ingrese el peso del archivo {archivos_procesados + 1} (en MB): '))
#     peso_total_acumulado += peso_archivo
#     archivos_procesados += 1

# print(f'Resumen: Se procesaron {archivos_procesados} archivos.')
# print(f'Peso total acumulado en el servidor: {peso_total_acumulado:.2f} MB\n')

# --- Validaciones ---

rol_usuario = input('Ingrese su rol para continuar (admin / user / invitado):\n> ')

while rol_usuario != 'admin' and rol_usuario != 'user' and rol_usuario != 'invitado':
    print('¡Error!: Rol no reconocido en el sistema')
    rol_usuario = input('Por favor, ingrese un rol válido (admin / user / invitado):\n> ')

print(f'Rol {rol_usuario} aceptado. Cargando interfaz...\n')

# --- Autenticación con getpass ---
PASSWORD_SISTEMA = "Bastion2026"
intentos_fallidos = 0
max_intentos = 3

clave_ingresada = getpass.getpass('Ingrese la contraseña de la Capital:\n> ')

while clave_ingresada != PASSWORD_SISTEMA and intentos_fallidos < (max_intentos - 1):
    intentos_fallidos += 1
    intentos_restantes = max_intentos - intentos_fallidos
    print(f'Contraseña Incorrecta. Te quedan {intentos_restantes} intento(s)')
    clave_ingresada = getpass.getpass('Intenta nuevamente:\n> ')

if clave_ingresada == PASSWORD_SISTEMA:
    print('Acceso concedido!!')
else:
    print('¡¡Sistema Bloqueado!!')