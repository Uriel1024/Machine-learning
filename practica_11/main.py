import random
import numpy as np
#el camino es #, las paredes son vacio, las x son lugares donde no puede pasar, el % es para definir el final del  laberinto

def generar_laberinto(filas, columnas):

    # Inicializar matriz llena de paredes
    laberinto = [["#" for _ in range(columnas)] for _ in range(filas)]

    # Movimientos posibles (arriba, abajo, izquierda, derecha)
    direcciones = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    def dfs(x, y):
        laberinto[x][y] = " "  # Celda libre
        random.shuffle(direcciones)  # Aleatorizar direcciones
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 1 <= nx < filas - 1 and 1 <= ny < columnas - 1:
                if laberinto[nx][ny] == "#":
                    # Romper pared intermedia
                    laberinto[x + dx // 2][y + dy // 2] = " "
                    dfs(nx, ny)

    # Iniciar desde (1,1)
    dfs(1, 1)
    
    for i in range(filas):            
        if random.random() >= .3:
            fil, col = random.randint(2,9) ,  random.randint(2,9)
            while laberinto[fil][col] == " ":
                fil, col = random.randint(2,9) ,  random.randint(2,9)
            laberinto[fil][col] = "x"  # Salida


    laberinto[0][0] = "%"  # Entrada
    fil, col = random.randint(2,9) ,  random.randint(2,9)
    while laberinto[fil][col] == " ":
        fil, col = random.randint(2,9) ,  random.randint(2,9)
    laberinto[fil][col] = "%"  # Salida

    return laberinto


if __name__ == "__main__":
    n,m = 10,10
    laberintos = []
    for i in range(20):
        lab = generar_laberinto(n,m)
        lab1 = np.array(lab)
        laberintos.append(lab1)

    file = open("laberintos.txt","w+")
    content = str(laberintos)
    file.write(content)
    file.close()

    file = open("laberintos.txt", "r")
    content = file.read()

    print("Array contents in sample.txt: ", content)
    file.close()

