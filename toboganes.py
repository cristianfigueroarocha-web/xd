edad = int(input("Ingresa tu edad: "))

if edad <= 6:
    print("Zona infantil")
elif edad >= 7 and edad <= 11:
    print("Toboganes medianos")
elif edad >= 12 and edad <= 17:
    print("Adulto")
elif edad >= 18:
    print("Acceso total")