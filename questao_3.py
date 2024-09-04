import json
import os

path_dir = os.path.dirname(os.path.realpath(__file__)) # recupera o diretório atual do script

# Leitura do arquivo json
with open(path_dir + '\dados.json') as file:
    dado_faturamento = json.load(file)

# Calculo do menor, maior e da média do faturamento
menor = float('inf')
maior = 0
soma = 0

for _, item in enumerate(dado_faturamento):
    if item['valor'] != 0:
        if item['valor'] < menor:
            menor = item['valor']

        if item['valor'] > maior:
            maior = item['valor']

        soma += item['valor']

media = soma / len(dado_faturamento)

print("\nMenor = {:.2f}\nMaior = {:.2f}\nMédia= {:.2f}".format(menor, maior, media))

# Contar o número de dias no mês que o faturamento diárioé maior que a média
contar_dias = 0
for _, item in enumerate(dado_faturamento):
    if item['valor'] != 0:
        if item['valor'] > media:
            contar_dias += 1

print("\nNúmero de dias no mês com valor maior que a média mensal foram {} dia(s)\n".format(contar_dias))

