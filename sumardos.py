#hacer una funcion que le pasas un array de numeros y otro parametro diciendo cual es el valor 
#que quieres que de la suma.
#debe devolver un array con los numeros que cumplan la condicion.

def sumar_dos(listanumeros,valor):
    lista_numero_res=[]
    for index,numero in enumerate(listanumeros):
        prox_index=index+1
        while prox_index <= len(listanumeros)-1:
            if (listanumeros[index]+listanumeros[prox_index] ==valor):
                lista_numero_res.append([listanumeros[index],listanumeros[prox_index]])
            prox_index=prox_index+1
    return lista_numero_res

def encontrar_parejas(numeros,objetivo):
    parejas=[]
    vistos=set()
    for numero in  numeros:
        complemento=objetivo-numero
        if complemento in vistos:
            parejas.append((complemento,numero))
        vistos.add(numero)
    return parejas



#me queda pendiente que devuelva la lista como un arreglo de tuplas.
print(sumar_dos([1,2,3,4,5,4,6],7))
print (encontrar_parejas([1,2,3,4,5,4,6],7))

def encontrar_parejas_tuplas(numeros, objetivo):
    parejas = []
    vistos = set()
    for numero in numeros:
        complemento = objetivo - numero
        if complemento in vistos:
            parejas.append((complemento, numero))
        vistos.add(numero)
    return parejas

print(encontrar_parejas_tuplas([1, 2, 3, 4, 5, 4, 6], 7))