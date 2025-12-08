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
                if laberinto[nx][ny] == "#" or laberinto[nx][ny] == "x" or laberinto[nx][ny] == "$":
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


if __name__ == "__main__":
    n,m = 11,11
    laberintos = []
    for i in range(20):
        lab = generar_laberinto(n,m)
        lab1 = np.array(lab)
        laberintos.append(lab1)

    file = open("laberintos2.txt","w+")
    content = str(laberintos)
    file.write(content)
    file.close()
    for i in laberintos:
        print(f"\n\n{i}")
