import pandas as pd

import src.utils as utils
import src as variables

def main():
    relatorio = pd.DataFrame(columns = [['Nome', 'Média de acertos %', 'Média de acertos', 'Total de acertos']])
    
    respostas, gabarito = variables.respostas, variables.gabarito 
    
    lista_alunos = utils.criar_lista_alunos(respostas.index) 

    for aluno in lista_alunos:
        acertos = utils.calcula_acertos(aluno, respostas, gabarito)
        
        boletim = (aluno, ((acertos/len(gabarito)*100)), (acertos/len(gabarito)), acertos)
        boletim = pd.DataFrame([boletim], columns = [['Nome', 'Média de acertos %', 'Média de acertos', 'Total de acertos']])
        
        relatorio = pd.concat([relatorio, boletim], ignore_index=True)

    print(relatorio)

if __name__ == '__main__':
    main()