import pandas as pd
pd.set_option('display.max_rows', 4000)
pd.set_option('display.precision', 2)

def calcula_acertos(nome, resp, gab):
    acertos = 0
    resp = resp.loc[[nome]]
    r,g = resp.Resposta.tolist(), gab.Resposta.tolist()
    for q in range(len(g)):
        if r[q] == g[q]:
            acertos += 1
    return acertos

gabarito,respostas = pd.read_excel('Gabarito.xlsx', index_col = 0), pd.read_excel('Respostas.xlsx', index_col = 0)
gabarito.rename(columns={'Gabarito' : 'Resposta'}, inplace = True)
respostas.rename(columns = {'resp_aluno' : 'Resposta'}, inplace = True)
respostas['Resposta'] = respostas['Resposta'].str.upper()

lista_alunos = []
for aluno in respostas.index:
    if aluno not in lista_alunos:
        lista_alunos.append(aluno)

relatorio = pd.DataFrame(columns = [['Nome', 'Média de acertos %', 'Média de acertos', 'Total de acertos']])

for aluno in lista_alunos:
    acertos = calcula_acertos(aluno, respostas, gabarito)
    boletim = (aluno, ((acertos/len(gabarito)*100)), (acertos/len(gabarito)), acertos)
    boletim = pd.DataFrame([boletim], columns = [['Nome', 'Média de acertos %', 'Média de acertos', 'Total de acertos']])
    relatorio = pd.concat([relatorio, boletim], ignore_index=True)

boletim = ('Total', relatorio['Média de acertos %'].mean(skipna=False)[0], relatorio['Média de acertos'].mean(skipna=False)[0], relatorio['Total de acertos'].sum()[0])
boletim = pd.DataFrame([boletim], columns = [['Nome', 'Média de acertos %', 'Média de acertos', 'Total de acertos']])
relatorio = pd.concat([relatorio, boletim], ignore_index=True)

print(relatorio)