def main() -> None:
    # print("=== INICIO ===")
    # consultar = True

    # while consultar:
    #     try:
    #         edad = int(input("Ingresa tu edad:\n"))
    #         consultar = False
    #     except ValueError:
    #         print("Debe ingresar un número. Intente nuevamente.")

    # print(f"Su edad es {edad}")
    # print("=== FIN ===")

    print("=== INICIO ===")
    intentos = 0
    
    while intentos <= 3:
        try:
            edad = int(input("Ingresa tu edad:\n"))
            divisor = int(input("Ingrese número para dividir su edad:\n"))
            resultado = edad / divisor
            
        except ValueError:
            print("Debe ingresar un número. Intente nuevamente.")
        except ZeroDivisionError:
            print("El N° por el cual desea dividir no puede ser cero")
        except Exception as e:
            print(f"ERROR: {e}")
        else:
            print(f"El resultado es: {resultado}")
            break
        finally:
            intentos += 1
            print(f"Intento {intentos} finalizado.\n")
        

    print("=== FIN ===")

if __name__ == "__main__":
    main()