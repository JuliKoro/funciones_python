# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones y módulos
import random

# --------------------------------
# Aquí dentro definir la función contar
def contar (lista_numeros, num):
    if any(lista_numeros) == True:
        numero_repetido = lista_numeros.count(num)
        return numero_repetido
    else:
        print('La lista está vacía o el numero no es un entero.')

# Aquí copiar la función lista_aleatoria
# ya elaborada
def lista_aleatoria (inicio, fin, cantidad):
    if cantidad > 0:
        lista_num = [] # Lista que almacena los números generados
        for i in range(cantidad):
            numero = random.randrange(inicio, fin+1)
            lista_num.append(numero)
        return lista_num
    else:
        print('La cantidad debe ser mayor a 0.')

# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    inicio = 0
    fin = 9
    cantidad = 5

    # Alumno: Crear la función "contar"

    # Utilice la función "lista_aleatoria"  creado antes 
    # para generar una lista de 5 números en
    # un rango de 1 a 9 inclusive

    # lista_numeros = lista_aleatoria(inicio, fin, cantidad)
    lista_numeros = lista_aleatoria(inicio, fin, cantidad)
    print(f'Lista de números aleatorios entre el {inicio} y el {fin}:\n{lista_numeros}')

    # Generar una una nueva funcion que se llame "contar",
    #que cuenta la cantidad de veces que un elemento pasado
    # por parámetro se repite en la lista también pasada por parámetro
    
    # Para saber cuantas veces se repiten el elemento pasado
    # en la lista pueden usar el método nativo de list "count"

    # Por ejemplo creo una lista de 5 elemtnos
    
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)

    # Luego de crear la función invocarla en este lugar:
    # Averiguar cuantas veces se repite el numero 3

    # cantidad_tres = contar(lista_numeros, 3)
    cantidad_tres = contar(lista_numeros, 3)

    # Imprimir en pantalla "cantidad_tres" que informa
    # cuantas veces se repite el tres en la lista

    # print(cantidad_tres)
    print(f'El número 3 se repite en la lista {cantidad_tres} veces.')

    print("terminamos")