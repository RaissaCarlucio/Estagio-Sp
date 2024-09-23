import json

# Exemplo de dados JSON
faturamento_json = '''
{
    "faturamento": [100.0, 0.0, 200.0, 300.0, 0.0, 400.0, 0.0, 500.0, 0.0, 600.0, 0.0]
}
'''
# Carregando o json na json_carergado
json_carregado = json.loads(faturamento_json)

faturamento_diario = json_carregado['faturamento']

# Filtrando os valores do Json, chamada List Comprehension, serve para criar listas.
dias_faturamento = [
    valor for valor in faturamento_diario 
                        if valor > 0
                        ]

menor_valor = min(dias_faturamento)
maior_valor = max(dias_faturamento)
media = (sum(dias_faturamento) / len(dias_faturamento))

# Contando os dias acima da média
dias_acima_da_media = 0
for valor in dias_faturamento: # Varrendo os valores
    if valor > media: # Se o valor for maior que a media
        dias_acima_da_media += 1  # Incrementa o contador, aumentando os dias que o faturamento passou da media.

print(f"O menor valor de faturamento ocorrido no mes: {menor_valor}")
print(f"O maior valor de faturamento ocorrido no mes: {maior_valor}")
print(f"Numero de dias no mes em que o valor de faturamento diario foi superior a media mensal: {dias_acima_da_media}")
