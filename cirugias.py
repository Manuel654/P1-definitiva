import doctor
class Cirugias:
    def __init__(self):
        self.tipo = input('Ingrese el tipo de cirugia: ')
        self.paciente = input('Ingrese el nombre y apellido del paciente: ')
        self.fecha = input('Ingrese la fecha de la operación: ')
        self.sala = input('Ingrese la sala en la que ocurrirá la operación: ')

    def registrar_cirugia(self):
        registro_cirugias={}
        registro_cirugias[self.paciente]=self.fecha,self.tipo,self.sala
        return registro_cirugias
cirugia1=Cirugias()
cirugia1.registrar_cirugia()
