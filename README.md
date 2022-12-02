# Pesquisa Operacional Para Computação

> Programa desenvolvido para a matéria Pesquisa Operacional Para Computação da UFSJ

### 🛠 Ferramentas

- Python
  - Tkinter
  - Pandas
  - Pulp

### ℹ️ Instalação

- pip install tkinter
- pip install pandas
- pip install pulp

### Informações

> O problema irá minimizar os custos da compra de bebidas para uma festa.

#### Variáveis:

x[1] ~ x[10] de acordo com a planilha editável "valoers.xlsx"

#### Instruções:

1. O usuário monta sua planilha com os fornecedores disponiveis, bebidas (no máximo 10, sendo que os 5 primeiros devem ser os refrigerantes disponíveis, os próximos 3 as cervejas e os ultimos suco e água respectivamente) e seus valores;
2. Na execução ele deve escolher qual fornecedor irá contratar, qual tipo de festa vai ser (isso varia a quantidade de cada tipo de bebida) e o valor máximo que ele pretende gastar;
3. Os valores serão equilibrados, para não ter muita de uma bebida e nenhuma da outra.
4. Se o valor inserido para compra for válido, irá mostrar o resultado da otimização.

#### Restrições:

1. Tem que ter no mínimo um refrigerante, uma cerveja, água e suco
2. Só pode um tipo de cerveja
3. Só pode um tipo de refrigerante
4. O preço da compra deve ser menor ou igual ao valor total disponibilizado pelo usuário
5. Se for festa de criança o número de refrigerante deve ser maior que o de cerveja
6. Se for festa de adulto o número de cerveja deve ser maior que o de refrigerante
7. A soma da quantidade de água e suco deve ser no máximo a metade da soma de refrigerante e cerveja
