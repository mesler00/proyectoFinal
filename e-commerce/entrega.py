db = {}
def registro():
    user = input("Ingrese nombre de usuario: ")
    if (user in db): 
        print('el usuario ingresado ya esta registrado')
    else:
        print('Username disponible')
        db[user] = input("Ingrese contraseña: ")
        print('usuario registrado con exito')
    return

def inicio_sesion():
    user= input('ingrese su nombre de usuario')
    if (user in db):
        pas = input('ingrese contraseña:')
        if (pas == db[user]):
            print ('inicio de sesion exitosa')
        else: 
            print ('la contraseña ingresa es incorrecta')
    else: 
        print ('el usuario ingresado no esta registrado')
    return

def pre_entrega ():
    while(True):
        print('Elija una opcion')
        print ('1: registro')
        print ('2: inicio de sesion')
        print ('3: exit')
        op= input ('ingrese la opcion elegida:')
        if (op == '1'):
            registro()
        elif (op == '2'):
            inicio_sesion()
        elif (op == '3'):
            return 

pre_entrega()
        


