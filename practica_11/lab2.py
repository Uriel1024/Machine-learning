import random
import numpy as np
#el camino es vacio, las paredes son #, las x son lugares donde no puede pasar, el % es para definir el final del  laberinto
#el tesoro para puntos es $, el pozo es @
def generar_laberinto(filas, columnas):

    # Inicializar matriz llena de paredes
    laberinto = [["#" for _ in range(columnas)] for _ in range(filas)]

    # Movimientos posibles (arriba, abajo, izquierda, derecha)
    direcciones = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    objetos = ["$","x","@"]

    for i in range(filas):
        fil,col = random.randint(2,filas-2), random.randint(2,columnas-2)
        if random.choice(objetos) == "$":
            laberinto[col][fil] = "$"
        elif random.choice(objetos) == "x":
            laberinto[col][fil] = "x"
        else:
            laberinto[col][fil] = "@"

    def dfs(x, y):
        laberinto[x][y] = " "  # Celda libre
        random.shuffle(direcciones)  # Aleatorizar direcciones
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 1 <= nx < filas - 1 and 1 <= ny < columnas - 1:
                if laberinto[nx][ny] == "#" or laberinto[nx][ny] == "@":
                    # Romper pared intermedia
                    laberinto[x + dx // 2][y + dy // 2] = " "
                    dfs(nx, ny)

    # Iniciar desde (1,1)
    dfs(1, 1)


    laberinto[1][1] = "s"  # Entrada
    fil, col = random.randint(2,9) ,  random.randint(2,9)
    while laberinto[fil][col] == " ":
        fil, col = random.randint(2,9) ,  random.randint(2,9)
    laberinto[fil][col] = "g"  # Salida

    return laberinto

def crear_recompensas(lab,n,m):
    recompensas = [[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if lab[i][j] == '#':
                recompensas[i][j] = -10
            elif lab[i][j] == 'x':
                recompensas[i][j] = -5
            elif lab[i][j] == '@':
                recompensas[i][j] = -20
            elif lab[i][j] == '$':
                recompensas[i][j] = 20
            elif lab[i][j] == 'g':
                recompensas[i][j] = 50
            else: 
                recompensas[i][j] = -1
    return recompensas


if __name__ == "__main__":
    n, m = 11,11
    lab = generar_laberinto(n,m)
    recompensas = crear_recompensas(lab,n,m)
    for i in lab:
        print(i)
    movimientos = [0,1,2,3]
