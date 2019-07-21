from statistics import mean 
from heapq import heapify, heappop

class Socio:
    def __init__(self, nombre, edad, equipo, estado, estudios):
        self.nombre = nombre
        self.edad = edad
        self.equipo = equipo
        self.estado = estado
        self.estudios = estudios
    def mostrar(self):
        print(self.nombre,self.equipo,self.edad,self.estado,self.estudios)



def lista_socios(nombre_archivo):
    archivo = open(nombre_archivo, "r",  encoding="latin-1")
    socios = []
    for linea in archivo.readlines(): 
        datos_socio = linea.split(";")
        nombre = datos_socio[0]
        edad = int(datos_socio[1])
        equipo = datos_socio[2]
        estado = datos_socio[3]
        estudios = datos_socio[4].replace('\n','')
        socio = Socio(nombre, edad, equipo, estado, estudios)
        socios.append(socio)
    return socios
    

def promedio_edad(socios,equipo):
    edades_hinchas = [hincha.edad for hincha in socios if hincha.equipo == equipo]
    return round(mean(edades_hinchas),2)


def casados_universitarios(socios,cantidad):
    casados_uni = []
    for socio in socios:
        if 'Casad' in socio.estado and socio.estudios == 'Universitario':
            #no asumo genero
            casados_uni.append((socio.edad, socio.nombre, socio.equipo))
    #De no quererse repetidos deberia usar el tipo set
    heapify(casados_uni)
    #Van a estar ordenados por edad en caso de empate nombre y como ultimo equipo
    for i in range(cantidad):
        edad, nombre, equipo = heappop(casados_uni)
        print(nombre,equipo,edad)


def nombres_comunes(socios, equipo,cantidad):
    hinchas = []
    for socio in socios:
        if socio.equipo == equipo: 
            hinchas.append(socio)
    #Esta vez no uso heapify ya que la cantidad de nombres distintos deberia ser mucho mas chico
    nombres = {}
    for hincha in hinchas:
        if hincha.nombre in nombres.keys():
            nombres[hincha.nombre] += 1
        else:
            nombres[hincha.nombre] = 1
    nombres_comunes = sorted(nombres.items(), key=lambda x: x[1])[-cantidad:]
    for elem in nombres_comunes:
        print(elem[0])


def equipos_mas_grandes(socios):
    equipos = {}
    for socio in socios:
        if socio.equipo in equipos.keys():
            equipos[socio.equipo]['sum_edades'] += socio.edad
            equipos[socio.equipo]['edad_min'] = min(socio.edad, equipos[socio.equipo]['edad_min'])
            equipos[socio.equipo]['edad_max'] = max(socio.edad,equipos[socio.equipo]['edad_max'])
            equipos[socio.equipo]['cant_socios'] += 1
        else:
            equipo = {}
            equipo['sum_edades'] = socio.edad
            equipo['edad_min'] = socio.edad
            equipo['edad_max'] = socio.edad
            equipo['cant_socios'] = 1
            equipos[socio.equipo] = equipo
    equipos = sorted(equipos.items(), reverse=True ,key=lambda tupla_equipo: tupla_equipo[1]['cant_socios'])
    for equipo in equipos:
        print("Nombre del Equipo: {0}".format(equipo[0]))
        print("Cantidad Socios: {0}".format(equipo[1]['cant_socios']))
        print("Edad Maxima: {0}".format(equipo[1]['edad_max']))
        print("Edad Minima: {0}".format(equipo[1]['edad_min']))
        print("Edad promedio: {0}".format(round( equipo[1]['sum_edades'] / equipo[1]['cant_socios'] , 4)))  
        print()             


   
def ej1():
    print(len(socios))
    print('\n')


def ej2():
    equipo = "Racing"
    print(promedio_edad(socios, equipo))
    print('\n')


def ej3():
    cantidad = 100
    casados_universitarios(socios, cantidad)
    print('\n')


def ej4():
    equipo = "River"
    cantidad = 5
    nombres_comunes(socios, equipo, cantidad)
    print('\n')


def ej5():
    equipos_mas_grandes(socios)




if __name__ == "__main__":
    socios = lista_socios("socios.csv")
    ejercicios = {'1': ej1, '2': ej2, '3': ej3, '4': ej4, '5': ej5}
    while(True):
        print("Insertar numero segun corresponda:")
        print("1. Cantidad total de personas registradas")
        print("2. El promedio de edad de los socios de Racing")
        print("3. Personas casadas universitarias(ordenadas por edad)")
        print("4. Los 5 nombres mas comunes en hinchas de River")
        print("5. Equipos por cantidad de socios y sus datos(de mayor a menor)")
        print("Otra numero. Cerrar el programa ")
        opcion = input()
        try:
            ejercicios[opcion]()
        except:
            break



    