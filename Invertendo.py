# Função para inverter as strings
def inverter_string(string):
    if string == "":
        return string
    else:
        # Removendo o primeiro caractere e adicionando no final, invertendo eles.
        return string[-1] + inverter_string(string[:-1])

# Funcao 2 para inverter as strings, mas agora passando a string
def inverter_string2():
    string = "Raissa Beatriz Carlucio"
    print(f"String invertida: {inverter_string(string)}")

# Chamando a função
inverter_string2()
