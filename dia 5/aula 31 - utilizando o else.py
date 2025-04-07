idade = int(input('Qual a sua idade? '))

if idade < 18:
    print('Menor de idade')
elif idade >= 18 and idade <60:
    print('maior de idade')
else:
    print('Idoso')