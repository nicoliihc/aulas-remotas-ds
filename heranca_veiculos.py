# heranca_veiculos.py

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def mostrar(self):
        super().mostrar()
        print("Número de portas:", self.portas)


carro1 = Carro("Hyundai", "Tucson", 4)
carro1.mostrar()
