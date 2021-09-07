class Calculadora:
    def __init__(self, numero1, numero2):
        self.num1=numero1
        self.num2=numero2
    def suma(self):
        return self.num1 + self.num2
    def resta(self):
        return self.num1 - self.num2
    def multiplicacion(self):
        multi = self.num1*self.num2
        print('{}*{}={}'.format(self.num1,self.num2,multi))
    def division(self):
        return self.num1 / self.num2

class calEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1,numero2)
    def multiplicacion(self): # aplicar polimorfismo
        return self.num1 * self.num2
    def exponente(self):
        return self.num1 ** self.num2
    def valorAbsoluto(self,numero):
        if numero < 0:
            numero = numero*-1
        return numero

class calCientifica(Calculadora):
    PI=3.1416
    def __init__(self,numero1,numero2):
        super().__init__(numero1,numero2)
    def circunferencia(self):
        pass
    def areaCirculo(self):
        pass
    def areaCuadrado(self):
        pass

#n1 = int(input('Ingrese n1: '))
#n2 = int(input('Ingrese n2: '))
#cal=Calculadora(n1,n2)
#cal.multiplicacion()

#calEst = calEstandar(4,8)
#x=calEst.multiplicacion()#
#y=x*5+2#
#print(calEst.multiplicacion())