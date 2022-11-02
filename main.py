# Librerias
import os
import time


def menu():
    while True:
        print("""
            --- Menu ---
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Division
            5. Residuo
            6. Salir
        """)

        opc = int(input("\tSeleccione una opcion: "))
        n1 = int(input("Digite un valor para el numero 1: "))
        n2 = int(input("Digite un valor para el numero 2: "))
        
        if opc == 1:
            suma(n1,n2)
        elif opc == 2:
            resta(n1,n2)
        elif opc == 3:
            producto(n1,n2)
        elif opc == 4:
            division(n1,n2)
        elif opc == 5:
            residuo(n1,n2)
        elif opc == 6:
            break
        else:
            print("Esa opcion no es correcta")


def suma(a,b):
    s = a+b
    return print(f"El resultado de la suma es: {s}")


def resta(a,b):
    r = a-b
    return print(f"El resultado de la resta es: {r}")


def producto(a,b):
    p = a*b
    return print(f"El resultado de la multiplicacion es {p}")


def division(a,b):
    d = a/b
    return print(f"El resultado de la division es: {d}")


def residuo(a,b):
    m = a%b
    return print(f"El resultado del residuo es: {m}")


def main():
    menu()
    print("Programa finalizado")


if __name__ == '__main__':
    main()