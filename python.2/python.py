saldo = 1000

print("\t.:menu:.")
print("1. ingresar dinero en la cuenta")
print("2. retirar dinero de la cuenta")
print("3. mostrar dinero disponible")
print("4. salir")

opcion=int(input("digite una opcion del menu:"))

if opcion==1:
    extra= float(input("cuanto dinero desea ingresar ->"))
    saldo += extra
    print(f"dinero total de la cuenta es:{saldo}")

elif opcion ==2:
    retirar=float(input("cuanto dinero desea retirar -> "))
    if retirar>saldo:
        ("no tiene suficiente saldo en su cuenta")
    else:
        saldo-= retirar
        print(f"dinero en la cuenta{saldo}")

elif opcion ==3:
    print(f"dinero en la cuenta {saldo}")

elif opcion ==4:
    print("gracias por usar el cajero automatico ")

else:
    print("error, se equivoco de opcion")
