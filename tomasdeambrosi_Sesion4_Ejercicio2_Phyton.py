#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numeroInicial = 2
numeroFinal = 8

for numero in range (numeroInicial, numeroFinal):
    if numero % 2 != 0:
        print(numero)


