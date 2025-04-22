import pandas as pd
import itertools

# Tabela 1: Qtd. Máxima por OBM
tabela_max = pd.DataFrame({
    'OBM': ['A001', 'A002', 'A003'],
    'Qtd.MAX': [100, 50, 70]
})

# Tabela 2: Posições e Quantidades no depósito
tabela_deposito = pd.DataFrame({
    'OBM': ['A001', 'A001', 'A001', 'A002', 'A002', 'A003', 'A003'],
    'Posição_Deposito': ['P1', 'P2', 'P3', 'P1', 'P4', 'P2', 'P3'],
    'Qtd.': [40, 30, 60, 20, 40, 50, 30]
})

# Lista final de resultados
resultado_final = []

# Loop para cada OBM
for obm in tabela_max['OBM']:
    qtd_max = tabela_max.loc[tabela_max['OBM'] == obm, 'Qtd.MAX'].values[0]
    posicoes = tabela_deposito[tabela_deposito['OBM'] == obm]

    melhor_comb = None
    menor_diferenca = float('inf')

    # Testar todas as combinações possíveis de posições
    for i in range(1, len(posicoes)+1):
        for combinacao in itertools.combinations(posicoes.itertuples(index=False), i):
            soma_qtd = sum(item[2] for item in combinacao)  # item[2] é 'Qtd.'
            diferenca = abs(soma_qtd - qtd_max)

            if diferenca < menor_diferenca:
                menor_diferenca = diferenca
                melhor_comb = combinacao

            # se achou exatamente o valor, nem precisa continuar
            if diferenca == 0:
                break
        if menor_diferenca == 0:
            break

    # Adicionar a melhor combinação ao resultado final
    for item in melhor_comb:
        resultado_final.append({'OBM': item[0], 'Posição_Deposito': item[1], 'Qtd.': item[2]})

# Criar DataFrame final
resultado_df = pd.DataFrame(resultado_final)

print(resultado_df)
