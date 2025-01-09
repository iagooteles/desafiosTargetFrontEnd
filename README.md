# Desafios Técnicos 

Este repositório contém a resolução de 5 desafios técnicos propostos para avaliação. As soluções foram implementadas em **Python** e estão organizadas de forma a facilitar a avaliação e execução.

## Estrutura do Repositório

- **Arquivos individuais para cada desafio**:
  - `desafio1.py` — Solução para o **Desafio 1**.
  - `desafio2.py` — Solução para o **Desafio 2**.
  - `desafio3.py` — Solução para o **Desafio 3**.
  - `desafio4.py` — Solução para o **Desafio 4**.
  - `desafio5.py` — Solução para o **Desafio 5**.
- **`desafios.ipynb`**: Um arquivo Jupyter Notebook que reúne todos os desafios resolvidos em um único lugar. Ideal para quem deseja analisar as soluções de forma centralizada.

## Como Executar

### Utilizando o arquivo `desafios.ipynb`
1. Certifique-se de ter o **Jupyter Notebook** ou equivalente configurado no ambiente.
2. Abra o arquivo `desafios.ipynb` no Jupyter Notebook ou vscode.
3. Execute as células sequencialmente para visualizar as resoluções dos desafios.

### Executando os desafios individualmente
1. Certifique-se de ter o **Python 3.x** instalado no ambiente.
2. Navegue até o diretório do repositório.
3. Execute o arquivo desejado com o comando:

```bash
python desafio<número>.py
```

OBS: Alternativamente pelo VScode pode-se executar o arquivo clicando em 'Run python file' no canto superior direito.

### Desafios

1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

### Observações
As soluções foram organizadas em arquivos individuais para maior flexibilidade. O avaliador pode optar por executar o notebook para visualizar tudo em conjunto ou os arquivos individuais para análise pontual.