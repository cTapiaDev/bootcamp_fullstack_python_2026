# Actividad 1 - Filtrado Compacto con Interfaz de Consola
# Explicación:
# El objetivo es devolver un informe resumido que exponga los meses que superan un cierto umbral.

ventas_anuales = {
    "Enero": 15000, "Febrero": 22000, "Marzo": 12000,
    "Abril": 17000, "Mayo": 81000, "Junio": 13000,
    "Julio": 21000, "Agosto": 41200, "Septiembre": 25000,
    "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000
}

ejecutando = True

while ejecutando:
    entrada = input("Ingrese el umbral de ventas a filtrar (escriba 'salir' para terminar): ")

    if entrada == 'salir':
        print("Cerrando sistema...")
        ejecutando = False
    else:

        if entrada.isnumeric():
            umbral = int(entrada)
            resultado = {mes: valor for mes, valor in ventas_anuales.items() if valor > umbral}

            print(f"\nMeses que superaron el umbral de {umbral}:")
            if len(resultado) > 0:
                print(resultado)
            else:
                print('Ningún mes superó el umbral.')

        else:
            print("ERROR: Por favor ingrese solo números enteros.")