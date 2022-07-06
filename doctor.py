import cirugias
class Doctor:
    def __init__(self, nombre, edad, especialidad,sala):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        self.asignar_sala = sala
        
    def agendar(self,horas_agendadas):
        print(horas_agendadas)
        fecha = input('Ingrese una fecha: ')
        hora = input('Ingrese una hora: ')
        sala = input('Ingrese una sala: ')
        especialidad_sala = input('Ingrese la especialidad o el doctor al que está asignada la sala: ')
        for i in horas_agendadas:
            if i[0] == fecha:
                print('Voy a revisar la hora')
                if i[1]==hora:
                    print('Tiene que reagendar')
                    horas_agendadas.pop()
                else:
                    print('Puedo a esa hora')
            if i[2]==sala and i[1]==hora and i[0]==fecha:
                print('Tiene que reangendar')
                horas_agendadas.pop()
            else:
                print('Queda agendado')
        return horas_agendadas
    
  
            
horas_agendadas = [('20/20/01','16:30','B56','Corazon'), ('20/21/22','15:30','C89','Cabeza')]
doctor1 = Doctor('Manuel','21','Corazon','Ninguna')
doctor1.agendar(horas_agendadas)
