aluno = {'nome': 'Kayan', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

#aluno['nome'] = 'João' #alterando nome

aluno.update({'nome': 'João', 'nota_final': 'B'}) #alterando nome e nota

aluno.update({'endereço': 'Rua A'}) #adicionando endereço

#print(aluno.get('endereço', 'Não existe')) #retorna um valor caso o item que pediu não tenha

del aluno['idade']
print(aluno)
