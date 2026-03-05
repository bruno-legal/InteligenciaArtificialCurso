idades = [23, 45, 31, 54, 29, 61, 40, 37, 48, 33]
soma = 0
grupo_risco = []

print(idades)
print("a: ", idades[0])
print("b: ", idades[-1])
print("c: Tamanho da lista: ", len(idades))
print("d: Terceira idade: ", idades[2])

for idade in idades:
  soma += idade

print("Soma: ", soma)
print("a: Média: ", soma/len(idades))
print("b: Máx: ", max(idades))
print("c: Min: ", min(idades))

acima_40 = [idade for idade in idades if idade > 40]
print("a: Idades acima de 40: ", acima_40)
entre_30_e_50 = [idade for idade in idades if (idade < 50 and idade > 30)]
print("b: Idades entre 30 e 50: ", entre_30_e_50)
idades_pares = [idade for idade in idades if idade % 2 == 0]
print("c: idades pares: ", idades_pares)
lista_mais_5 = [idade+5 for idade in idades]
print("4: ", lista_mais_5)

for i in idades:
    if i > 50:
       grupo_risco += [i]
print("Grupo de risco:", grupo_risco)
print("Quantidade em risco: ", len(grupo_risco))