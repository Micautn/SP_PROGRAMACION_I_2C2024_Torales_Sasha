path_empleados = 'EMPLEADOS.csv'
class Empleado:
    identificacion = 0
    def __init__(self, apellido_nombre,salario:float,dni:int,telefono):
        Empleado.identificacion +=1
        self.apellido_nombre= apellido_nombre
        self.salario = salario
        self.telefono = telefono
        self.dni = dni
        self.id = Empleado.identificacion

    def __str__(self):
        return f"[{self.id}] - Apellido y nombre: {self.apellido_nombre} - D.n.i: {self.dni} - salario: {self.salario} - Telefono: {self.telefono}"
    def parse_csv(self):
        return f"{self.id};{self.apellido_nombre};{self.dni};{self.salario};{self.telefono}"