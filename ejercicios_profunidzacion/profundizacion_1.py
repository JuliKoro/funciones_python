# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Este ejercicio representa ya un problema que forma parte de un juego
Lo que se desea realizar es una parte del juego "la generala".
El enunciado está armado a modo de guía, pueden resolver el problemla
de otra forma.
Si tienen dudas sobre el enunciado o alguno de los puntos por favor
comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
puede haber varias interpretaciones de un mismo enunciado.

Deberá realizar una lista para guardar 5 dados, guardar los números
sacados en esa tirada de de dados (son 5 dados, cada uno del número 1 al 6)

1) El jugador tira los dados y saca 5 números aleatorios, puede usar
la función de "lista_aleatoria" para generar dichas lista de números.
Esa lista de datos se llamará dados_tirados

2) Luego debe analizar los 5 números y ver cual es el número que
más se repitio entre los 5 dados.
Debe usar la función de Python "max" con la "key" de list.count para
determinar cual fue el número que más se repitió. Consultar los ejemplos
vistos en clase en donde se realizó esta operación con "max"

3) Una vez reconocido el número más repetido entre los 5 dados,
debe guardar en una lista aparte esos números más repetidos.
Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4"
Debe extrarlos de la lista, quedándole una lista separada
dados_guardados = [4,4,4]
Debe realizar un bucle para recorrer la lista de dados_tirados
y guardar los "4" en nuestra nueva lista dados_guardados
Utilice append para ir sumando a dados_guardados los valores

4) Debe volver a tirar los dados, generar nuevos
números aleatorios.
Si en la lista "dados_guardados" tengo 3 dados guardados
significa que ahora deberé tirar solo dos dados. Puede usar la función
"len" para ver cuantos elementos hay en "dados_guardados"
Es decir que en este caso debería generar solo dos números
aleatorios nuevos con "lista_aleatoria"
Ahora tendré una nueva lista de "dados_tirados", en este caso
de dos nuevos números aleatorios entre 1 y 6 representando a los dados
tirados.

5) Luego de tirar nuevamente los datos en el paso anterior,
por ejemplo digamos que salieron los números: 4-1
Debo volver a quedarme con el "4" ya que es el número que estoy
buscando almacenar en la otra lista de "dados_guardados".
Sino salió el "4" vuelvo a tirar todos los dados (solo 2 dados en este caso)
Si salió un "4" me lo quedo y lo guardo en "dados_guardados".

6) Debe repetir este proceso hasta que en su lista de "dados
guardados" tenga "generala", es decir, 5 números iguales.
'''

import random

# --------------------------------
# Dentro de esta sección copiar y crear
# todas las funciones que utilice
def lista_aleatoria (inicio = 1, fin = 6, cantidad = 5):
    '''Generar lista aleatoria de números.
    
    Retorna una lista de 5 números 
    aleatorios entre el 1 y el 6

    @param inicio Número donde empieza el rango
                    de números aleatorios (default = 1)
    @param fin Número donde termina el rango
                    de números aleatorios (default = 6)
    @param cantidad Cantidad de números que tendrá la lista (default = 5)
    '''
    if cantidad > 0:
        lista_num = [] # Lista que almacena los números generados
        for i in range(cantidad):
            numero = random.randrange(inicio, fin+1)
            lista_num.append(numero)
        return lista_num
    else:
        print('La cantidad debe ser mayor a 0.')


def contar_max (dados_tirados):
    '''Detectar número que más repetido

    Retorna el número de una lista que más veces 
    se repite.

    @param dados_tirados Lista con 5 dados tirados entre 1 y 6

    '''
    if any(dados_tirados) == True:
        max_repeticiones = max(dados_tirados, key=dados_tirados.count)
        return max_repeticiones
    else:
        print('Error, no se ha tirado ningún dado.')


def guardar_dados (dados_guardados, dados_tirados, dado_max):
    '''Guardar números más repetidos en una lista

    Retorna una lista con el número que más veces se
    repitió de una lista

    @param dados_tirados Lista de 5 números aleatorios del 1 al 6
    @param dado_max Variable con el número que más veces se repitió en dicha lista

    '''
    if any(dados_tirados) == True:
        
        for dado in dados_tirados:
            if dado == dado_max:
                dados_guardados.append(dado)
        return dados_guardados
    else:
        print('Error, no se ha tirado ningún dado.')

# --------------------------------

if __name__ == '__main__':
    print("¡El juego de la generala!")
    # A partir de aquí escriba el código que
    # invoca al as funciones y resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    dados_tirados = lista_aleatoria() # Primera tirada de dados
    print('Primera tirada de dados:\n', dados_tirados)
    dado_max = contar_max(dados_tirados) # Dado que más se repite en al tirada
    dados_guardados = [] # Lista que almacena los dados más repetidos
    dados_guardados = guardar_dados(dados_guardados, dados_tirados, dado_max) # Guardo en dados_guardados
    print(f'El dado {dado_max} es el más repetido {len(dados_guardados)} veces.')
    tiradas = 1
    while len(dados_guardados) != 5: # Hasta tener 5 dados iguales
        dados_tirados = lista_aleatoria(cantidad=5-len(dados_guardados)) # Vuelve a tirar los dados restantes
        tiradas += 1
        print(f'Tirada nro. {tiradas}:\n{dados_tirados}')
        dados_guardados = guardar_dados(dados_guardados, dados_tirados, dado_max) # Guardo los repetidos a dado_max
    print(dados_guardados, f'\n¡Generala!\n Lo conseguiste luego de {tiradas} tiradas.')