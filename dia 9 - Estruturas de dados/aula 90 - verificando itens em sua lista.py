escolha = input('fale uma cor: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

if escolha.lower() in cores:
    print('Essa cor está na lista')
else:
    print('Essa cor não está na lista')