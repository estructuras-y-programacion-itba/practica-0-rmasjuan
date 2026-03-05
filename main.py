# Tu implementacion va aqui
def hola_mundo():
    return "hola_mundo"


def main():
    # Aqui ejecutas tus soluciones
    print(hola_mundo())


# No cambiar a partir de aqui
if __name__ == "__main__":
    main()

#cambio

print("cambio")


import random

#Juego Generala 

#5 dados + 2 jugadores

#TURNOS 
#3 turnos, cada turno 5 dados 
def tirada_dados(cantidad):
    dados = []
    for dado in range(0, cantidad):
        dados.append(random.randint(1,6)) 
    return dados

tirada = tirada_dados(5)

def jugar_turno(jugador, planilla):
    cantidad = 0
    dados = 5
    tirada = tirada_dados(dados)
    while cantidad < 3:
        print(tirada)
        continuar = input("Queres cambiar los dados (si/no)")
        if continuar == "no":
            cantidad = 3
        else:
            cantidad += 1
            cambios = input("Que posiciones queres cambiar (0, 1, 2, 3, 4)")
            indices = [int(i) for i in cambios.split() if i.isdigit()]
            for i in indices:
                if 0 <= i < len(tirada):
                    tirada[i] = random.randint(1,6)
                    
        tirada.sort()
        print("tu tirada final es:", tirada)
    return tirada

jug = 1
opciones = ["1", "2", "3", "4", "5", "6", "E", "F", "P", "G"]
plantilla =[]

jugar_turno(jug, plant)

def llenar_plantilla(tirada;plantilla):
    tirada.sort()
    cantidades = [0,0,0,0,0]
    for i in tirada:
        cantidades[i-1] += 1
    for i in cantidades:
        