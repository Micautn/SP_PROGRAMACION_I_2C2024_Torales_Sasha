path_vehiculos = 'VEHICULOS.json'
class Vehiculo:
    identificacion = 0
    def __init__(self,Marca:str,Modelo:str,Anio:int,Color:str,Patente,Propietario:str) -> None:
        Vehiculo.identificacion +=1
        self.Marca = Marca
        self.Modelo = Modelo
        self.Anio = Anio
        self.Color = Color
        self.Patente = Patente
        self.Propietario = Propietario
        self.ID = Vehiculo.identificacion
    def __str__(self) -> str:
        return f'[{self.ID}] - Marca: {self.Marca} - Anio: {self.Anio} - Color: {self.Color} - Patente: {self.Patente} - Propietario: {self.Propietario}'
    def parse_json(self) -> dict:
        return {
            "ID": self.ID,
            "Marca": self.Marca,
            "Modelo": self.Modelo,
            "Anio": self.Anio,
            "Color": self.Color,
            "Patente": self.Patente,
            "Propietario": self.Propietario
        }  