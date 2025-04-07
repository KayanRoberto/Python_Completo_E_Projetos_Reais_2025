aluno = {'Nome:': 'Kayan',
         'Idade:': 21,
         'Nota:': 'A',
         'Aprovação:': True,
         'Matérias:': ['Fisica', 'Matemática','Inglês']
}

print(aluno)

print(aluno.get('matérias'))
print(len(aluno))
print(aluno.items())
print(aluno.keys())
print(aluno.values())

for keys,values in aluno.items():
    print(keys, values)
