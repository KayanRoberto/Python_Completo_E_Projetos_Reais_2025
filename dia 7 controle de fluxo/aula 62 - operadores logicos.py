renda = int(input(f'Qual a sua renda? '))
nomeLimpo =bool(input(f'Seu nome está limpo? '))

if renda >= 5000 and nomeLimpo:
    print(f'Financiamento aprovado')
else:
    print(f'Financiamento negado')