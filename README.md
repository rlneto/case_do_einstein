<h1># case_do_einstein</h1>
<h2>Solução do case que me foi proposto para o PS do Einstein['Vale do Silício']
<br>
Autor: Rudolfo Lange Neto, rudolflange em gmail</h2>

-----------------------

	README

-----------------------
<h3>Conteúdo

1. Bibliotecas
2. Funções
3. Inicialização
4. Rotina
5. Conclusão</h3>

-----------------------

1. Bibliotecas

Foi feita a escolha pelo uso da biblioteca Pandas. A mesma pode ser instalada ao remover-se o comentário da primeira linha.

-----------------------

2. Funções

Criou-se uma opção que efetua o cálculo de acertos de cada aluno a fim de evitar a repetição de código, uma vez que esa é usada na rotina que gera o relatório.
A função faz a seleção dos dados com base no nome do aluno, armazena em duas variáveis que correspondem à primeira letra da origem e compara as igualdades, retornando o total acertos para o aluno selecionado pelo parâmetro "nome".

-----------------------

3. Inicialização

É feita a importação e tratamento dos dados a fim de obter-se dois DataFrames. Algumas colunas foram renomeadas a fim de permitir a comparação e aumentar a legibilidade da mesma.
Criam-se as variáveis gabarito e respostas, iguala-se o case das respostas dos alunos a fim de obter-se comparações válidas em caso de igualdade.
É feita uma relação de alunos a fim de fazer-se as iterações com os dados e calcular as médias.

-----------------------
4. Rotina

É gerado o template do relatório em um DataFrame vazio.
Armazena-se o retorno da função em uma variável (acertos) a fim de poupar tempo de processamento, uma vez que a função seria chamada 3 vezes por iteração, em 37 iterações, totalizando 91 chamadas da função.
É então gerado um dataframe que incorpora as informações desejadas para cada aluno e é feita a concatenação dos dados ao dataframe "relatorio".

-----------------------

5. Conclusão

Por fim, gera-se uma row com os dados totais pedidos além do "Total de acertos" a fim de evitar gatilhos de OCD e é impresso o DataFrame na tela.
