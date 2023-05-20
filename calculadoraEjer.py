while True:
    print("-----Calculadora-----")
    print("     a-Sumar")
    print("     b-Salir")
    menu = input("Sleccione la opcion: ")
    if menu == "a":
        x = int(input("ingrese el primer numero "))
        y = int(input("ingrese el segundo numero "))
        print(f"La suma de ", x, " y ", y, "es ", x+y) 