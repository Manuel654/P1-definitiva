
class Paciente:
    def __init__(self,nombre,especialidad_buscada):
        self.nombre = nombre
        self.epecialidad_buscada = especialidad_buscada
    
    def pedir_hora(self, horas_agendadas):
        print(horas_agendadas)
        fecha = input('Ingrese una fecha: ')
        hora = input('Ingrese una hora: ')
        sala = input('Ingrese una sala: ')
        especialidad_sala = input('Ingrese la especialidad o a el doctor que busca: ')
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