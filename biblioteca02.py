class Ingresso():
    def __init__(self, valor):
        self.valor=valor()

    def imprime(self):
        print(f"o valor do ingressoé {self.valor}")

class Vip (Ingresso):
    def __init__(self,valor):
        super ().__init__(valor)
        self.valor*=1.5
    def imprime(self):
        print(f"o valor do Vip é {self.valor}")