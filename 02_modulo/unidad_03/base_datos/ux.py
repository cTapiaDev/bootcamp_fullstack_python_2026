import os
import sys
import time

def limpiar_pantalla() -> None:
    """Limpia la consola según el sistema operativo"""
    comando = 'cls' if sys.platform == 'win32' else 'clear'
    os.system(comando)

def pausar(segundos: float = 1.0) -> None:
    """Detiene el tiempo del sistema"""
    time.sleep(segundos)

def mostrar_encabezado(modulo: str) -> None:
    limpiar_pantalla()
    print("=" * 50)
    print(f" SISTEMA POS CORP - {modulo.upper()}".center(50))
    print("=" * 50)

def animacion_procesando(mensaje: str, repeticiones: int = 3) -> None:
    print(f"\n{mensaje}", end="")
    for _ in range(repeticiones):
        sys.stdout.flush()
        pausar(0.3)
        print(".", end="")
    print("\n")