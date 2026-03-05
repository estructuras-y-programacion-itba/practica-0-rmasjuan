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
    for dado in range(1, cantidad):
        dados = []
        dados =+ random.randint(1,6)
    return dados

ejemplo = tirada_dados(5)
print(ejemplo)
