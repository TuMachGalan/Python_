# creacion de txt para agregar los usuarios
ruta = "C:/Users/54266/Desktop/Programacion/python/clase 11"
f = open(ruta + "/usuarios.txt", "a")
f.close()
import itertools

f = open(ruta + "/usuarios.txt", "r")
users = f.read().split(":")
users.pop()
user_list_iter = iter(users)
user_list_dict_object = itertools.zip_longest(user_list_iter, user_list_iter, fillvalue=None)
user_db = dict(user_list_dict_object)
f.close()

# crear usuario
def crearuser():
    usuario = input("Escriba Nombre de usuario: ")
    passw = input("Escriba su contraseña: ")
    ruta = "C:/Users/54266/Desktop/Programacion/python/clase 11"
    f = open(ruta + "/usuarios.txt", "a")
    f.write(f"{usuario}:{passw}:")
    f.close()


def iniciar():
    try:
            usuario = input("Nombre de usuario:")
            passw = input("Contraseña:")
            if usuario in user_db:
                pass
            if passw in user_db[usuario] and passw == user_db[usuario]:
                print("Inicio Correctamente")
            else: print("contraseña incorrecta")
    except KeyError:
        print("Este usuario No existe")
        iniciar()

# Menu
print(
    "Bienvenido \n Ingrese un numero para realizar una operacion \n 1_ Crear Usuario \n 2_ Iniciar sesión \n 3_ Ver Usuarios \n 4_ Salir")
while True:
    try:
        a = int(input("Ingrese un numero: "))
    except Exception as error:
        print(f"ha ocurrido un error: {error}")
    else:
        if a < 5:
            break
        else:
            print("Ingrese un numero de lista")
if a == 1:
    crearuser()
elif a == 2:
    iniciar()
elif a == 3:
    print(user_db)

