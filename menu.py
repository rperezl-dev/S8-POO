from calculadora import calEstandar, calCientifica
import os
class Menu:
    def __init__(self, titulo='', opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input('Elija opcion[1...{}]:'.format(len(self.opciones)))
        return opc
opc=''
while opc !='5':
    menu = Menu('Menu principal', ['1) Calculadora','2)Numeros','3) Listas','4) Cadenas','5) Salir'])
    opc = menu.menu()
    if opc == '1':
        opc1= ''
        while opc1 != '3':
            menu1= Menu('Menu Calculadora',['1) Suma','2) Resta','3) Salir'])
            opc1=menu1.menu()
            if opc1 == '1':
                    print('Suma de dos numeros')
                    n1 = int(input('Ingrese n1: '))
                    n2 = int(input('Ingrese n2: '))
                    calEst = calEstandar(n1, n2)
                    suma=calEst.suma()
                    print('{}+{}={}'.format(n1,n2,suma))

    elif opc == '2':
            menu2=  Menu('Menu Numeros',['1) Perfecto','2) Primo','3) Salir'])
            opc2=menu2.menu()
    elif opc == '3':
            print('Menu Listas')
    elif opc == '4':
            print('Menu Cadenas')
    elif opc == '5':
            print('Gracias por su visita')
    else:
            print('opcion no valida')