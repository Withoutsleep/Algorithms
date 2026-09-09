#Mierdon de algoritmo xd


lista = list(range(1, 10**8))
objetivo = 4851878

izquierda = 0
derecha = len(lista) -1
intentos=0

while True:
    intentos=intentos+1
    numero_medio = len(lista)/2
    if numero_medio % 1 == 0.5:
        numero_medio=numero_medio-0.5
    numero_medio=int(numero_medio)
    if lista[numero_medio]<objetivo:
        del lista[:numero_medio]
    elif lista[numero_medio]>objetivo:
        del lista[numero_medio:]
    elif lista[numero_medio]==objetivo:
        print(f"Numero encontrado en intento: {intentos}")
        break
    print(f"Intento numero: {intentos} = {lista} ")