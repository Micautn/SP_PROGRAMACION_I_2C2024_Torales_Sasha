path_reparaciones = 'REPARACIONES.CSV'
class Reparacion:
    identificacion = 1000
    def __init__(self, descripcion, coste ):
        Reparacion.identificacion +=1
        self.descripcion = descripcion
        self.id = Reparacion.identificacion
        self.coste = coste
    def __str__(self):
        return f"id: {self.id} - Descripción: {self.descripcion} - Coste: {self.coste}"
    def parse_csv(self):
        return f"{self.id}/{self.descripcion}/{self.coste}"