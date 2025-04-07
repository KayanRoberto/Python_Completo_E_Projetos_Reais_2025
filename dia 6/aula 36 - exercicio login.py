dados = input('Digite seu usuario e senha: ').split()
usuario = dados[0]
senha =  dados[1]

if usuario == 'admin' and senha == '1234':
    print(f'senha e usuario aceito')
else:
    print(f'senha e usuario não aceito')