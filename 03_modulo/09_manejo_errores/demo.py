import re
from errores import HoraError, LargoTextoError
from reunion import Reunion

def main() -> None:
    titulo = None
    hora = None
    time_re = r"^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$"

    while True:
        try:
            if titulo is None or len(titulo) > 150:
                titulo = input("\nIngrese título de la reunión (Max. 150 caracteres);\n")
                if len(titulo) > 150:
                    raise LargoTextoError("Título excede máximo de caracteres", titulo, 150)

            if hora is None or re.search(time_re, hora) is None:
                hora = input("Ingrese hora de la reunión (Formato: HH:MM:SS):\n")
                if re.search(time_re, hora) is None:
                    raise HoraError("Formato de hora debe ser HH:MM:SS")

        except Exception as e:
            print(f"\n[ERROR CAPTURADO] {e}")
            continue

        else:
            break

    reunion_creada = Reunion(titulo, hora)
    print("\nReunión creada correctamente.")
    print(f"-> {reunion_creada.titulo} a las {reunion_creada.hora}")

if __name__ == "__main__":
    main()