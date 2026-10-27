import copy
tablero = [
    [0, 6, 0, 1, 0, 4, 0, 5, 0],
    [0, 0, 8, 3, 0, 5, 6, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 1],
    [8, 0, 0, 4, 0, 7, 0, 0, 6],
    [0, 0, 6, 0, 0, 0, 3, 0, 0],
    [7, 0, 0, 9, 0, 1, 0, 0, 4],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 7, 2, 0, 6, 9, 0, 0],
    [0, 4, 0, 5, 0, 8, 0, 7, 0]
]
#lista para mis soluciones
soluciones = []

def imprimir_tablero(matriz):
    "****Función auxiliar para mostrar el tablero de forma limpia.****"
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        fila_str = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                fila_str += "| "
            fila_str += str(matriz[i][j]) + " "
        print(fila_str)

def validar(num, f, c):
    for j in range(9):
        if tablero[f][j] == num:
            return False  
    for i in range(9):
        if tablero[i][c] == num:
            return False
            
    inicio_f = (f // 3) * 3
    inicio_c = (c // 3) * 3
    for i in range(inicio_f, inicio_f + 3):
        for j in range(inicio_c, inicio_c + 3):
            if tablero[i][j] == num:
                return False
                
    return True

def fcdisponible():
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return i, j
    return -1, -1

def sudoku():
    f, c = fcdisponible()
    if f == -1 and c == -1:
        soluciones.append(copy.deepcopy(tablero))
        return False
    else:
        for num in range(1, 10):
            if validar(num, f, c):
                tablero[f][c] = num
                #llamamos a la recursividad para seguir buscando soluciones
                sudoku()
                # Backtracking 
                tablero[f][c] = 0
                
        return False
print("******** SUDOKU INCIAL (encontraremos la solucion)*********")
imprimir_tablero(tablero)
print("\nBuscando todas las soluciones posibles...\n")
sudoku()
#par mostrar
if len(soluciones) == 0:
    print("No se encontraron soluciones...")
else:
    print(f"¡Lo logramos! Se encontro {len(soluciones)} solución:\n")
    for indice, sol in enumerate(soluciones, 1):
        print(f"*****SOLUCIÓN #{indice} *****")
        imprimir_tablero(sol)
        print()
    