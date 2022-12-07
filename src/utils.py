def calcula_acertos(nome, resp, gab):
    acertos = 0
    resp = resp.loc[[nome]]
    r,g = resp.Resposta.tolist(), gab.Resposta.tolist()

    for q in range(len(g)):
        if r[q] == g[q]:
            acertos += 1

    return acertos

def criar_lista_alunos(lista):
    lista_alunos = []
    for aluno in lista:
        if aluno not in lista_alunos:
            lista_alunos.append(aluno)

    return lista_alunos
