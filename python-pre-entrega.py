ruta = "C:/Users/54266/Desktop/Programacion/python/clase 11"
def Usuarios_reg():
    f = open(ruta + "/BaseDeDatos.txt", "r")
    datos = list(f.read().split(":"))
    datos.pop()
    print(datos)
def Login():
    f = open(ruta + "/BaseDeDatos.txt", "r")
    datos = list(f.read().split(":"))
    datos.pop()
    usuarios = []
    passw = []
    for clave, valor in enumerate(datos):
        if (clave % 2 == 0):
            usuarios.append(valor)
    for clave, valor in enumerate(datos):
        if (not clave % 2 == 0):
            passw.append(valor)
    user_db = dict(zip(usuarios,passw))
    try:
        usuario = input("Nombre de usuario:")
        if usuario in user_db:
            pass
        passw = input("Contraseña:")
        if passw in user_db[usuario] and passw == user_db[usuario]:
            print("Inicio Correctamente")
        else:
            print("contraseña incorrecta")
            Login()
    except KeyError:
            print("Este usuario No existe")
            Login()
def Checkeo(user):
    f = open(ruta + "/BaseDeDatos.txt", "r")
    datos = list(f.read().split(":"))
    datos.pop()
    f.close()
    return user not in datos
def Registro():
    print("\n\n\n Bienvenido al registro\nrellene los siguientes campos:")
    user = input("Usuario: ")
    if Checkeo(user):
        passw = input("Contraseña: ")
        print(f"Recuerde su usuario es : {user}, y su contraseña es : {passw}")
        f = open(ruta + "/BaseDeDatos.txt", "a")
        f.write(f"{user}:{passw}:")
        f.close()
    else:
        print("Este Usuario ya existe")
def Inicio():
    print("""
Inicio del programa.........
seleccione una opcion:
1_ Inicio De sesion
2_ Crear un nuevo usuario
3_ Ver usuarios registrados
4_ Finalizar programa
        """)
    while True:
        try:
            a = int(input("Ingrese un numero: "))
        except Exception as error:
            print(f"ha ocurrido un error: {error}")
        else:
            break
    if a == 1:
        Login()
    elif a == 2:
        Registro()
    elif a == 3:
        Usuarios_reg()
    elif a == 4:
        print("El Programa finalizo correctamente")
    else:
        print("Ingrese un numero de lista")
        Inicio()


Inicio()

