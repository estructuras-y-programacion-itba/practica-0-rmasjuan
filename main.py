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

'falta agregar algo que priorize y no permita anotar dos cosas en una misma tirada.'

#5 dados + 2 jugadores

#TURNOS 
#3 turnos, cada turno 5 dados 
def tirada_dados(cantidad):
    dados = []
    for dado in range(0, cantidad):
        dados.append(random.randint(1,6)) 
    return dados


def jugar_turno():
    cantidad = 0
    dados = 5
    tirada = tirada_dados(dados)
    while cantidad < 3:
        tirada.sort()
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
    return tirada, cantidad


def llenar_plantilla(tirada,plantilla,cant,jugador):
    tirada.sort()
    stop = False

    # Contamos cada 'i' en el rango del 1 al 6
    cantidades = [tirada.count(i) for i in range(1, 7)]
    print(cantidades) 

    if stop == False:
        for i in range(0,len(cantidades)):
            if cantidades[i] == 5:
                print("GENERALA")
                if plantilla[jugador][9] == 0:
                    si = input("queres anotar esto? ")
                    if si == "si":
                        plantilla[jugador][9] = 1
                        stop == True
                    if cant == 1:
                        puntos[jugador] += 80
                    else:
                        puntos[jugador] += 50

                elif plantilla[jugador][i] == 0:
                    print("Ya completaste la generala, anotamos", opciones[i])
                    si = input("queres anotar esto? ")
                    if si == "si":
                        plantilla[jugador][i] = 1
                        stop == True
                        puntos[jugador] += 5*(i+1)
                
                else:
                    print("no podemos anotar nada")

    if stop == False:
        for i in range(0,len(cantidades)):
            if cantidades[i] == 4:
                print("POKER")
                if plantilla[jugador][8] == 0:
                    si = input("queres anotar esto? ")
                    if si == "si":
                        plantilla[jugador][8] = 1
                        stop == True
                        puntos[jugador] += 40
                elif plantilla[jugador][i] == 0:
                    print("Ya completaste el poker, anotamos", opciones[i])
                    si = input("queres anotar esto? ")
                    if si == "si":
                        plantilla[jugador][i] = 1
                        stop == True
                        puntos[jugador] += 4*(i+1)
                else:
                    print("no podemos anotar nada")

    if stop == False:
        for i in range(0,len(cantidades)):
            if cantidades[i] == 3:
                for otro in range(0,len(cantidades)):
                    if cantidades[otro] == 2:
                        print("FULL")
                        if plantilla[jugador][7] == 0:
                            si = input("queres anotar esto? ")
                            if si == "si":
                                plantilla[jugador][7] = 1
                                stop = True
                                puntos[jugador] += 30
                            
                        elif plantilla[jugador][i] == 0 and plantilla[jugador][otro] == 0:
                            print("Ya completaste la full")
                            op = int (input("queres completar 3 dados o 2 dados?"))
                            plantilla[jugador][op-1] = 1
                            stop == True
                            puntos[jugador] += op*(i+1)
                            
                        elif plantilla[jugador][i] == 0:
                            print("Ya completaste la full, anotamos: ", opciones[i])
                            si = input("queres anotar esto? ")
                            if si == "si":
                                    plantilla[jugador][i] = 1
                                    stop == True
                                    puntos[jugador] += 3*(i+1)
                        else:
                            print("no podemos anotar nada")

    if stop == False:
        cont = 0
        for i in range(0,len(cantidades)):
            if cantidades[i] == 1:
                cont += 1
            elif cont != 5:
                cont = 0 
        if cont == 5:
            print("ESCALERA")
            si = input("queres anotar esto? ")
            if si == "si":
                plantilla[jugador][6] = 1
                stop == True
                puntos[jugador] += 20
    
    if stop == False:
        for i in range(0,len(cantidades)):
            if cantidades[i] == 2:
                print("DOBLE ", opciones[i])
                if plantilla[jugador][i] == 0:
                    si = input("queres anotar esto? ")
                    if si == "si":
                        plantilla[jugador][i] = 1
                        stop == True
                        puntos[jugador] += 2*(i+1)
                else:
                    print("no anotamos nada")

    if stop == False:
        for i in range(0,len(cantidades)):
            if cantidades[i] == 1:
                print("UN ", opciones[i])
                if plantilla[jugador][i] == 0:
                    primer = input("queres anotar esto? ")
                    if primer == "si":
                        plantilla[jugador][i] = 1
                        stop == True
                        puntos[jugador] += 1*(i+1)
                else:
                    print("no anotamos nada")

    print(plantilla[jugador])


def juego_final(jugadores,plantilla):
    print("Bienvenido a la GENERALA")
    empezar = 0
    completo = [0,0]
    juego = True
    while empezar != "1":
        empezar = input('ingresa 1 para empezar: ')
    while juego == True:
        for j in jugadores:
            print("cambio de turno")
            tirada,c = jugar_turno()
            llenar_plantilla(tirada, plantilla,c,j)
            for p in plantilla:
                if p == 0:
                    juego == True
                else:
                    completo[j] += 1
            if plantilla[j][9] == 0 and c == 1:
                juego == False
        if completo[1] >= 5 and completo[0] >= 5:
            juego == False
    print("se termino el juego")
    print("gano el jugador: ", max(puntos[0], puntos[1]))

jug = [0,1]
opciones = ["1", "2", "3", "4", "5", "6", "E", "F", "P", "G"]
plantilla =[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
puntos = [0,0]

juego_final(jug, plantilla)