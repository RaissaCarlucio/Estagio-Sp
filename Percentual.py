# Utilizando uma função para auxiliar no processo de calcular o percentual
def calcular_percentuais():
    estados_faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    soma_faturamento = sum(estados_faturamento.values())
    
    # Variavel auxiliar
    percentuais = {}
    
    # Usando um for para calcular o percentual de cada estado
    for estado in estados_faturamento:
        valor = estados_faturamento[estado]  
        percentual = (valor / soma_faturamento) * 100  # Calculando o percentual
        percentuais[estado] = percentual  # Armazenando na variavel percentuais

    print("Percentual de faturamento de cada estado:")
    for estado, percentual in percentuais.items():
        print(f"Percentual de {estado}: {percentual:.2f}%")

# Chamando a função
calcular_percentuais()
