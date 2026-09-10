import math
import random


ciudad_A = (2,4) #En un futuro se hará aleatorio
ciudad_B = (7,1)
ciudad_C = (8,8)

ciudades_a_visitar=[ciudad_A,ciudad_B,ciudad_C]

orden=[]

distancia_total=0

#Crea el orden aleatorio
n=ciudades_a_visitar
for i in range(len(ciudades_a_visitar)):
    #print(n)
    choice_selected=random.choice(n)
    orden.append(choice_selected)
    del n[n.index(choice_selected)]
    #n.remove(n.index(choice))

ciudades_a_visitar=[ciudad_A,ciudad_B,ciudad_C]

#Calcula las distancias dependiendo de el orden
for i in range(len(ciudades_a_visitar)):
    try:
        distancia_total+=math.sqrt(((orden[i])[0]-(orden[i+1])[0])** 2 + ((orden[i])[1]-(orden[i+1])[1])** 2)
    except:
        distancia_total+=math.sqrt(((orden[i])[0]-0)** 2 + ((orden[i])[1]-0)** 2) #Calcula la distancia desde la ultima hasta (0,0) <- origen
print(distancia_total)