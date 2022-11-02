# Librerias
import os
import time

# Funciones Globales
def cuenta_regresiva():
    numero = 3
    print("\nRegresando al menu en: ")
    for i in range(numero):
        print(numero)
        time.sleep(1)
        numero-=1
        if numero == 0:
            print(numero)
            os.system("cls")


def back_menu():
    time.sleep(1.5)
    cuenta_regresiva()


def menu():
    while True:
        print("\n")
        print("""
            --- Menu ---
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Division
            5. Residuo
            6. Salir
        """)
        time.sleep(.5)
        n1 = int(input("Digite un valor para el numero 1: "))
        n2 = int(input("Digite un valor para el numero 2: "))

        opc = int(input("\nSeleccione una opcion: "))
        
        if opc == 1:
            suma(n1,n2)
            back_menu()
        elif opc == 2:
            resta(n1,n2)
            back_menu()
        elif opc == 3:
            producto(n1,n2)
            back_menu()
        elif opc == 4:
            division(n1,n2)
            back_menu()
        elif opc == 5:
            residuo(n1,n2)
            back_menu()
        elif opc == 6:
            break
        else:
            print("Esa opcion no es correcta")
            back_menu()

# Funciones Logicas
def suma(a,b):
    s = a+b
    return print(f"\n --> El resultado de la suma es: {s}")


def resta(a,b):
    r = a-b
    return print(f"\n --> El resultado de la resta es: {r}")


def producto(a,b):
    p = a*b
    return print(f"\n --> El resultado de la multiplicacion es {p}")


def division(a,b):
    d = a/b
    return print(f"\n --> El resultado de la division es: {d}")


def residuo(a,b):
    m = a%b
    return print(f"\n --> El resultado del residuo es: {m}")

# Funcion Main
def main():
    menu()
    print("Programa finalizado")


if __name__ == '__main__':
    main()