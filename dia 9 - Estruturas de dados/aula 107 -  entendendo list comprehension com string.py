frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = [ ]

#for itens in frutas1:
#   if 'i' in itens:
#      frutas2.append(itens)

frutas2 = [itens for itens in frutas1 if 'a' in itens]

print(frutas2)

cores  = ['amarelo', 'branco', 'vermelho', 'laranja']

cores2 = [valorzinho for valorzinho in cores if 'a' in valorzinho]

print(cores2)









