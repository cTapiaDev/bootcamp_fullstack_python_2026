import json
import datetime
from usuario import Usuario

formatear_log = lambda error_msg: f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Excepción capturada: {error_msg}\n"

def main() -> None:
    usuarios_instanciados = []

    try:
        with open("usuarios.txt", "r", encoding="utf-8") as archivo_usuarios:
            for linea in archivo_usuarios:
                linea_limpia = linea.strip()

                if not linea_limpia:
                    continue

                try:
                    datos_json = json.loads(linea_limpia)
                    nuevo_usuario = Usuario(**datos_json)
                    usuarios_instanciados.append(nuevo_usuario)

                except Exception as e:
                    with open("error.log", "a+", encoding="utf-8") as archivo_error:
                        archivo_error.write(formatear_log(e))

    except FileNotFoundError:
        print("Error crítico: El archivo 'usuarios.txt' no se encuentra en el directorio.")


    print("Proceso finalizado")
    print(f"Total de usuarios instanciados: {len(usuarios_instanciados)}")

if __name__ == "__main__":
    main()