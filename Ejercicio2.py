#Se requiere digitar los valores de las compras realizadas por los clientes de una tienda de 
#zapatos, no se saben cuántas compras se realizaron y se deben acumular los valores 
#ingresados, para así obtener el total de compra realizada. Una vez obtenido el total de 
#compra realizado se debe hallar el 25% del valor, que es lo que representará las ganancias

#import math
lista = []
contador = 0
cantidad = int(input("Digite la cantidad de zapatos que compro: "))
while contador != cantidad:

    valor = int(input(" Digite el valor del zapato (sin puntos ni comas): "))
    lista.append(valor)
    contador = contador + 1

resultado = sum(lista)   
resultado1 = resultado * 0.25

print("Compro:" ,cantidad, "Zapatos")
print("La suma de la compra es: " ,resultado)
print("Las ganasncias por la compra son (25%)" ,resultado1.__round__())    