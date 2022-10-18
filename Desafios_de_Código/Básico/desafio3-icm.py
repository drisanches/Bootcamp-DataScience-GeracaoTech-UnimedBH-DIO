# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

#distancia = int(input("Informe a distância entre os dois Palantírs: "))
#diametro1 = int(input("Informe o diâmetro do primeiro Palantír: "))
#diametro2 = int(input("Informe o diâmetro do segundo Palantír: "))

entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

interferencia_comunicacao_magica = (distancia / (diametro1 + diametro2))

print(f'{interferencia_comunicacao_magica:.2f}')

# Definindo as condições de cálculo
# N = distancia (0 < N < 10000)
# X = diametro1 (0 < X < 100)
# Y = diametro2 (0 < Y < 100)

#condicao1 = distancia > 0 and distancia < 10000
#condicao2 = diametro1 > 0 and diametro1 < 100
#condicao3 = diametro2 > 0 and diametro2 < 100

#if condicao1 and condicao2 and condicao3:
#    print(f"A Interferência de Comunicação Mágica é: {interferencia_comunicacao_magica:.2f}")
#else:
#    print("Os valores inseridos não são válidos!")