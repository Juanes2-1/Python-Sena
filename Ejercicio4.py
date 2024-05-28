#hacer un algoritmo que imprima los primeros 20 términos de la siguiente serie: 1, 3, 6, 10, 
#15, 21, 28…….

n = 1
s = 2
p = 1
for i in range(20):

    re =  (n*(n + 1)) /2
    n += 1

    print(re.__round__())