notaAluno = int(input('Digite a nota do aluno: '))

if notaAluno >= 9:
    print(f'Perfeito, nota A')
elif notaAluno >= 7:
    print(f'Muito bem, nota B')
elif notaAluno >= 5:
    print(f'Passou por pouco, nota C')
else:
    print(f'VAMOS ESTUDAR PORRA???? REPROVADO')