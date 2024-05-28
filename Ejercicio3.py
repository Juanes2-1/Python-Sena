#caso de estudio se centrará en el desarrollo de un simple juego de adivinanza de números 
#en Python. El juego pedirá al usuario que adivine un número entre 1 y 5. Solo se utilizarán 
#condicionales

n = input(" En que numero estoy pensando? (del 1 al 5): ")

if n == 1:
    print("Ese no era el nuemro")
elif n == 2:
    print("Este tampoco era el numero")
elif n == 3:
    print("mmm tampoco es el numero")
elif n == 4:
    print("Epppaaa este es")
elif n == 5:
    print("No es")
else:
    print("Digito no compatible")

