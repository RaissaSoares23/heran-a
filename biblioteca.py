class Animal ():
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer (self):
        print (f"O {self.nome} foi comer...")

class Gato (Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def miar(self):
        print (f'O {self.nome} foi miando...')

class Cachorro (Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f'O {self.nome} está latindo...')

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def Mugir (self):
        print(f'O {self.nome} está mugindo')

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calculaArea (self,base,altura):
        self.area=base*altura
        print(f"A area do retangulo é {self.area}")
    def calculaPeriometro(self,base,altura):
        self.perimmetro=(base*altura)*2
        print(f"O perimetro do retangulo é {self.perimetro}")


#class Triangulo():
  #  def calculaArea(self):
  #  def calculaPeriometro(self):