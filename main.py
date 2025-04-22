import pandas as pd
import itertools

# Carregar as tabelas com caminhos corretos
tabela_max = pd.read_csv(r"********************************")
tabela_deposito = pd.read_csv(r"******************************")

# Limpar nomes de colunas
tabela_max.columns = tabela_max.columns.str.strip()
tabela_deposito.columns = tabela_deposito.columns.str.strip()

resultado_final = []

for obm in tabela_max['OBM']:
    qtd_max = tabela_max.loc[tabela_max['OBM'] == obm, 'Qtd.MAX'].values[0]
    posicoes = tabela_deposito[tabela_deposito['OBM'] == obm]

    melhor_comb = None
    menor_diferenca = float('inf')

    for i in range(1, len(posicoes) + 1):
        for combinacao in itertools.combinations(posicoes.itertuples(index=False), i):
            soma_qtd = sum(item.Qtd for item in combinacao)
            diferenca = abs(soma_qtd - qtd_max)

            if diferenca < menor_diferenca:
                menor_diferenca = diferenca
                melhor_comb = combinacao

            if diferenca == 0:
                break
        if menor_diferenca == 0:
            break

    for item in melhor_comb:
        resultado_final.append({'OBM': item.OBM, 'Posição_Deposito': item.Posição_Deposito, 'Qtd.': item.Qtd})

resultado_df = pd.DataFrame(resultado_final)

print(resultado_df)
