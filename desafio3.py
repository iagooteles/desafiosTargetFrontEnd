# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

def analisar_faturamento(faturamento_diario):
    dias_com_faturamento = [faturamento['valor'] for faturamento in faturamento_diario if faturamento['valor'] > 0]

    menor_valor = min(dias_com_faturamento)
    maior_valor = max(dias_com_faturamento)

    media = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_da_media = len([d for d in dias_com_faturamento if d > media])

    print(f"Menor valor de faturamento: R${menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")

faturamento_diario = [
    {"dia": 1, "valor": 200},
    {"dia": 2, "valor": 300},
    {"dia": 3, "valor": 100},
    {"dia": 4, "valor": 500},
    {"dia": 5, "valor": 0},
    {"dia": 6, "valor": 0},
    {"dia": 7, "valor": 400},
    {"dia": 8, "valor": 250},
    {"dia": 9, "valor": 150},
    {"dia": 10, "valor": 500},
    {"dia": 11, "valor": 0},
    {"dia": 12, "valor": 0},
]

analisar_faturamento(faturamento_diario)
