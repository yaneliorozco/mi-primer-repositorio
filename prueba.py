#funcion para recorrer una lista de string
def recorrer_lista(lista):
    for elemento in lista:
        print(elemento)

#funcion para llenar una matriz de 2 dimensiones
def llenar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = input(f"Introduce el valor para la posición ({i},{j}): ")
            fila.append(valor)
        matriz.append(fila)
    return matriz

print(llenar_matriz(3, 3))  # Example call with 3 rows and 3 columns
recorrer_lista([10,20,30,40])
