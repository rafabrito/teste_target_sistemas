faturamento_mensal = {"faturamento":{"sp": 67836.43, "rj": 36678.66, "mg": 29229.88, "es": 27165.48, "outros": 19849.53}, "total": 0} # dicionário com o faturamento de cada estado e o faturamento total

# Calcular o valor total do faturamento
for item in faturamento_mensal['faturamento']:
    if item != 'total':
         faturamento_mensal['total'] += faturamento_mensal['faturamento'][item]

# Calcular o percentual representativo de cada estado em relação ao faturamento total
porcentagem = 0
for item in faturamento_mensal['faturamento']:
    if item != 'total':
        porcentagem = (100 * faturamento_mensal['faturamento'][item]) / faturamento_mensal['total']
        print('\nPorcentagem {} = {:.2f}%'.format(str.upper(item), porcentagem))