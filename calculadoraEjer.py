while True:
    print("-----Calculadora-----")
    print("     a-Sumar")
    print("     b-Resta")
    print("     c-Salir")
    menu = input("Sleccione la opcion: ")
    if menu == "a":
        x = int(input("ingrese el primer numero "))
        y = int(input("ingrese el segundo numero "))
        print(f"La suma de ", x, " y ", y, "es ", x+y) 
    elif menu == "b":
        x = int(input("ingrese el primer numero "))
        y = int(input("ingrese el segundo numero "))
        print(f"La resta de ", x, " menos ", y, "es ", x-y) 
    elif menu == "c";
        print("Hasta Luego!")
        break