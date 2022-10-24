A_lista_1 = ['a', '2', 'c', '3', 'e', '4', 'g', '5', 'i', '6', 'k', '7', 'm']
B_lista_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# A - B 

A_conjunto_1 = set(A_lista_1)
B_conjunto_2 = set(B_lista_2)

diferencia = A_conjunto_1.difference(B_conjunto_2)

print(diferencia) 

#La diferencia es el conjunto resultannte de A-B 