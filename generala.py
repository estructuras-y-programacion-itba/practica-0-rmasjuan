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


def jugar_turno():
    cantidad = 0
    dados = 5
    tirada = tirada_dados(dados)
    while cantidad < 3:
        tirada.sort()
        print(tirada)
        continuar = ""
        while continuar != "si" and continuar != "no":
                continuar = input("Queres cambiar los dados (si/no)")
        if continuar == "no":
            cantidad = 3
        else:
            cantidad += 1
            while True:
                cambios = input("Que posiciones queres cambiar (0, 1, 2, 3, 4): ")
                indices = [int(i) for i in cambios.split() if i.isdigit()]
                if all(0 <= i < len(tirada) for i in indices) and len(indices) > 0:
                    break
                print("Posiciones inválidas, ingresá números entre 0 y 4.")
            for i in indices:
                tirada[i] = random.randint(1, 6)
        tirada.sort()
    print("tu tirada final es:", tirada)
    return tirada, cantidad


def llenar_plantilla(tirada,plantilla,cant,jugador):
    tirada.sort()
    stop = False
    generala_real = False
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
                        stop = True
                        if cant == 1:
                            puntos[jugador] += 80 
                            puntaje_categorias[jugador][9] = 80
                            generala_real = True
                        else:
                            puntos[jugador] += 50
                            puntaje_categorias[jugador][9] = 50

                elif plantilla[jugador][i] == 0:
                    print("Ya completaste la generala, anotamos", opciones[i])
                    si = input("queres anotar esto? ")
                    if si == "si":
                        plantilla[jugador][i] = 1
                        stop = True
                        puntos[jugador] += 5*(i+1)
                        puntaje_categorias[jugador][i] = 5*(i+1)
                
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
                        stop = True
                        puntos[jugador] += 40 + (5 if cant == 1 else 0)
                        puntaje_categorias[jugador][i] = 40 + (5 if cant == 1 else 0)
                elif plantilla[jugador][i] == 0:
                    print("Ya completaste el poker, anotamos", opciones[i])
                    si = input("queres anotar esto? ")
                    if si == "si":
                        plantilla[jugador][i] = 1
                        stop = True
                        puntos[jugador] += 4*(i+1)
                        puntaje_categorias[jugador][i] = 4*(i+1)
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
                                puntos[jugador] += 30 + (5 if cant == 1 else 0)
                                puntaje_categorias[jugador][i] = 30 + (5 if cant == 1 else 0)
                            
                        elif plantilla[jugador][i] == 0 and plantilla[jugador][otro] == 0:
                            print("Ya completaste la full")
                            op = int (input("queres completar 3 dados o 2 dados?"))
                            plantilla[jugador][op-1] = 1
                            stop = True
                            puntos[jugador] += op*(i+1)
                            puntaje_categorias[jugador][i] = op*(i+1)
                            
                        elif plantilla[jugador][i] == 0:
                            print("Ya completaste la full, anotamos: ", opciones[i])
                            si = input("queres anotar esto? ")
                            if si == "si":
                                    plantilla[jugador][i] = 1
                                    stop = True
                                    puntos[jugador] += 3*(i+1)
                                    puntaje_categorias[jugador][i] = 3*(i+1)
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
                stop = True
                puntos[jugador] += 20 + (5 if cant == 1 else 0)
                puntaje_categorias[jugador][i] = 20 + (5 if cant == 1 else 0)
    
    if stop == False:
        for i in range(0,len(cantidades)):
            if cantidades[i] == 2:
                print("DOBLE ", opciones[i])
                if plantilla[jugador][i] == 0:
                    si = input("queres anotar esto? ")
                    if si == "si":
                        plantilla[jugador][i] = 1
                        stop = True
                        puntos[jugador] += 2*(i+1)
                        puntaje_categorias[jugador][i] = 2*(i+1)
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
                        stop = True
                        puntos[jugador] += 1*(i+1)
                        puntaje_categorias[jugador][i] = 1*(i+1)
                else:
                    print("no anotamos nada")

    if stop == False:
        for i in range(0, len(cantidades)):
            if cantidades[i] == 3:
                print("TRIO de ", opciones[i])
                if plantilla[jugador][i] == 0:
                    si = input("queres anotar esto? ")
                    if si == "si":
                        plantilla[jugador][i] = 1
                        stop = True
                        puntos[jugador] += 3 * (i + 1)
                        puntaje_categorias[jugador][i] =  3 * (i + 1)
                else:
                    print("no anotamos nada")

    if stop == False:
        print("No tenés jugadas disponibles. Elegí una categoría para anotar 0.")
        for i in range(len(opciones)):
            if plantilla[jugador][i] == 0:
                print(i, "-", opciones[i])
        op = int(input("Ingresá el número de la categoría: "))
        if 0 <= op < len(opciones) and plantilla[jugador][op] == 0:
            plantilla[jugador][op] = 1

    print("tu plantilla es: ", opciones, "\n", plantilla[jugador] ) 
    return generala_real

def guardar_csv(plantilla, puntos):
    categorias = ["1", "2", "3", "4", "5", "6", "E", "F", "P", "G"]
    with open("jugadas.csv", "w") as archivo:
        archivo.write("jugada,j1,j2\n")
        for i in range(len(categorias)):
            archivo.write(f"{categorias[i]},{puntaje_categorias[0][i]},{puntaje_categorias[1][i]}\n")

def juego_final(jugadores, plantilla):
    print("Bienvenido a la GENERALA")
    empezar = ""
    while empezar != "1":
        empezar = input("ingresa 1 para empezar: ")
    
    juego = True
    while juego:
        for j in jugadores:
            pausa = input("\n¿Querés continuar jugando? (si/no): ")
            if pausa == "no":
                print("Juego pausado. ¡Hasta la próxima!")
                guardar_csv(plantilla, puntos)
                return
            print(f"\n--- Turno del Jugador {j + 1} ---")
            tirada, c = jugar_turno()
            generala_real = llenar_plantilla(tirada, plantilla, c, j)
            guardar_csv(plantilla, puntos)

            if generala_real:
                print(f"¡Generala Real! El Jugador {j + 1} gana automáticamente.")
                juego = False
                break

        if juego:
            ambos_completos = all(plantilla[j][i] == 1 for j in jugadores for i in range(10))
            if ambos_completos:
                juego = False

    print("\n--- FIN DEL JUEGO ---")
    print(f"Jugador 1: {puntos[0]} puntos")
    print(f"Jugador 2: {puntos[1]} puntos")
    if puntos[0] > puntos[1]:
        print("Ganó el Jugador 1")
    elif puntos[1] > puntos[0]:
        print("Ganó el Jugador 2")
    else:
        print("¡Empate!")

jug = [0,1]
opciones = ["1", "2", "3", "4", "5", "6", "E", "F", "P", "G"]
plantilla =[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
puntaje_categorias = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
puntos = [0,0]

juego_final(jug, plantilla)