from datetime import datetime

hora_actual = lambda: datetime.now().strftime('%H:%M:%S')

def main() -> None:
    ruta_log = "sistema.log"

    # Modo 'w': Escritura Destructiva
    with open(ruta_log, "w") as log_w:
        log_w.write(f"[{hora_actual()}] SISTEMA INICIADO\n")
    print("Archivo creado y sobreescrito")

    # Modo 'a+': Append y lectura
    with open(ruta_log, "a+") as log_a:
        log_a.write(f"[{hora_actual()}] NUEVO EVENTO REGISTRADO\n")
        log_a.seek(0)
        print(log_a.read())

    # Modo 'r+': Actualización
    with open(ruta_log, "r+") as log_r:
        contenido_previo = log_r.read()
        log_r.write(f"[{hora_actual()}] ACTUALIZACIÓN VÍA R+\n")
        log_r.seek(0)
        print("Contenido final:")
        print(log_r.read())

if __name__ == "__main__":
    main()