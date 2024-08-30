# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
# faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à 
# média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. 
# Estes dias devem ser ignorados no cálculo da média;


import json

with open('data.json', 'r') as file:
    data = json.load(file)

billingDaily = [day["value"] for day in data["billingDaily"] if day["value"] > 0]

lowestBilling = min(billingDaily)
biggesttBilling = max(billingDaily)

monthlyAverage = sum(billingDaily) / len(billingDaily)

daysAboveAverage = sum(1 for value in billingDaily if value > monthlyAverage)

print(f"Menor valor de faturamento: {lowestBilling}")
print(f"Maior valor de faturamento: {biggesttBilling}")
print(f"Dias com faturamento acima da média: {daysAboveAverage}")
