class Vehiculo():

    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enMarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print(f"""Marca: {self.marca}
                \nModelo: {self.modelo}
                \nEn marcha: {self.enMarcha}
                \nAcelerando: {self.acelera}
                \nFrenando: {self.frena} 
                """)
class VElectrico(Vehiculo):
    def __init__(self,marcaVElectrico,modeloVElectrico):
        #Metodo init heredado de Vehiculo
        super().__init__(marcaVElectrico,modeloVElectrico) 
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True

class Moto(Vehiculo):
    def __init__(self,marcaMoto,modeloMoto):
        #Metodo init heredado de Vehiculo
        super().__init__(marcaMoto,modeloMoto)
        self.hacerCaballito=""

    def caballito(self):
        self.hacerCaballito="Voy haciendo el caballito"

    def estado(self):
        super().estado()
        print(self.hacerCaballito)

class MotoElectrica(Moto,VElectrico):
    
    pass
        
miMoto=MotoElectrica("Honda","CBR")
miMoto.caballito()
miMoto.estado()
miMoto.cargarEnergia()
print(miMoto.autonomia)