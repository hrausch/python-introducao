class FormaBidimensional:

    nome=''
    
    def area(self):
        pass

    def perimetro(self):
        pass


class Quadrado(FormaBidimensional):

    lado = 0

    def area(self):
        print('lado ao quadrado = ', (self.lado * self.lado) )

    def perimetro(self):
        print('4 * l')

class Circulo(FormaBidimensional):

    raio = 0

    def area(self):
        print('pi * r * r = ', (3.14 * self.raio * self.raio)) 

    def perimetro(self):
        print('2 * pi * r = ', (2 * 3.14 * raio) )


obj1 = Circulo()
obj1.raio = int( input('Digite o raio') )
obj1.area()

obj2 = Quadrado()
obj2.lado = 5
obj2.area()