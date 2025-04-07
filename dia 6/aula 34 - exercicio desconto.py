valorCompra = float(input('Qual o valor da sua compra? R$'))

if valorCompra > 200:
    desconto = 0.2
elif valorCompra > 100:
    desconto = 0.1
else:
    deconto = 0.5

final = valorCompra - (valorCompra * desconto)
print(f'O valor da sua compra foi para R${final:.2f}')
