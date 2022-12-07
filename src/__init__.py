# setup

import pandas as pd
pd.set_option('display.max_rows', 4000)
pd.set_option('display.precision', 2)

gabarito,respostas = pd.read_excel('Gabarito.xlsx', index_col = 0), pd.read_excel('Respostas.xlsx', index_col = 0)
gabarito.rename(columns={'Gabarito' : 'Resposta'}, inplace = True)
respostas.rename(columns = {'resp_aluno' : 'Resposta'}, inplace = True)
respostas['Resposta'] = respostas['Resposta'].str.upper()