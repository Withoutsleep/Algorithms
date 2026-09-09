import random
import time

objetivo="4851"
codigos=[]
aciertos=[]
numero_de_muestra=5
fitness=[]
nuevos_codigos=[]
pruebas=0

#Primera generacion de codigos aleatorios
for i in range(10):
    numero=""
    for i in range(len(objetivo)):
        numero+=str((random.randint(0,9)))
    codigos.append(numero)
print(f"Primera muestra: {codigos}")

def mejorar():
    #Comrpobar similitud
    for i in range(len(codigos)):
        coincidencias=0
        n=0
        #print(i)
        for letra in codigos[i]:
            #print(f"letra actual = {letra} | letra que se busca {objetivo[n]}")
            if letra == objetivo[n]:
                #print("letra encontrada")
                coincidencias=coincidencias+1
            n=n+1
        aciertos.append(coincidencias)

    print(f"aciertos: {aciertos}")

    temporal_list=aciertos
    for i in range(numero_de_muestra):
        fitness.append(temporal_list.index(max(temporal_list)))
        temporal_list[temporal_list.index(max(temporal_list))]=-1

    print(f"lo importante: {fitness}")
    print(f"La lista al final: {temporal_list}")

def fusiones(test):
    print(f"la prueba definitiva: {test}")
    #Las primeras fusiones
    for i in fitness:
        codigobase=test[i]
        primeramitad=codigobase[:(len(test[i]) // 2)]
        for n in range(len(fitness)-1):
            codigosecundario=test[n]
            segundamitad=codigosecundario[(len(test[n]) // 2):]
            nuevos_codigos.append(primeramitad+segundamitad)
    codigos[:]=nuevos_codigos
    print(f"codigos antes de mutar: {codigos}")

def mutaciones():
    for i in range(5):
        codigo_a_cambiar=codigos[random.randint(0,len(codigos)-1)]
        codigomutado=codigo_a_cambiar
        codigomutado=list(codigomutado)
        codigomutado[random.randint(0,(len(objetivo)-1))]=str(random.randint(0,9))
        codigomutado="".join(codigomutado)
        codigos[codigos.index(codigo_a_cambiar)]=codigomutado

def comprobar():
    for codigo in codigos:
        if codigo == objetivo:
            print(codigos)
            print(f"Numero encontrado con exito en: {pruebas} intentos")
            return True
    #Limpia el fitness
    fitness.clear()
    aciertos.clear()
    nuevos_codigos.clear()
    print(f"comprobado\n")

while True:
    mejorar()
    fusiones(codigos)
    mutaciones()
    resultado=comprobar()
    if resultado==True:
        break
    else:
        pruebas=pruebas+1
        print(f"Prueba numero: {pruebas}")

#print(f"Codigos despu de mutar: {codigos}")

