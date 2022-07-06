from p1 import doctor
class Especialidades(doctor):
    def __init__(self,nombre):
        self.nombre = nombre
    def doctores_segun_especielidad(self, lista_doctores):
        return lista_doctores.sort()
    

        
    