# MANIPULAÇÃO DE STRINGS COM PYTHON

## Métodos Úteis da Classe String:

- Maiúscula: print(curso.upper())
- Minúscula: print(curso.lower())
- Título: print(curso.title()) *somente primeira letra maiúscula*
- Strip: elimina os espaços em branco desnecessários. Ex: curso = "   Python  "
	- print(curso.strip()) = "Python"
	- print(curso.lstrip()) = "Python  " *elimina espaços somente à esquerda*
	- print(curso.rstrip()) = "   Python" *elimina espaços somente à direita*
- Centralização (método center): print(curso.center(10, "#")) = "##Python##" 
	- Recebe 2 atributos: 10 representa o número total de caracteres e # representa o caractere que ocupará o espaço (opcional)
- Junção (método join): print(".".join(curso)) = "P.y.t.h.o.n" *adiciona o caractere informado entre cada letra*

## Interpolação de Variáveis:

Existem 3 formas de interpolar variáveis, sendo:
1. Sinal %s (str), %d (int) ou %f (float): atualmente não é recomendada e seu uso em Python 3 é raro

Exemplo:

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

2. Método format: utiliza {} como marcador/identificador

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

*Também é possível alterar as posições de cada string*
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(nome, idade, profissao, linguagem))

*Outro formato*
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

*Associando a um dicionário pessoa*

pessoa = {"nome": "Guilherme", "idade": 28, "profissao": "programador",  "linguagem": "Python"}
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

3. f-string: mais limpo e simples.

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

**Formatação:** definir tamanho da string e número de casas *variável:width.casasdecimaisf(float)*
PI = 3.14159
print(f"Valor de PI:{PI:.2f}") = Valor de PI: 3.14 
print(f"Valor de PI:{PI:10.2f}") = Valor de PI:           3.14

## Fatiamento de String:

É uma técnica utilizada para retornar substrings (partes da string original), informando início (start), fim (stop) e passo (step): [start:stop[,step]].

Exemplo:
nome = "Drielly de Fátima Sanches da Silva"
nome[0] = "D"
nome[-1] = "a" *última letra da string*
nome[:7] = "Drielly"
nome[11:25] = "Fátima Sanches"
nome[11:25:2] = "Ftm ace"
nome[:] = "Drielly de Fátima Sanches da Silva"
nome[::-1] = "avliS ad sehcnaS amitáF ed ylleirD"


## String Múltiplas Linhas ou Triplas

São definidas informando 3 aspas simples ou duplas durante a atribuição. Podem ocupar várias linhas do código e todos os espaços em branco são incluídos na string final.

Exemplo: dessa forma o valor é exibido exatamente com o espaçamento e recuo definido no texto.
nome = "Drielly"

print(f"""
Olá, meu nome é {nome},
Eu estou aprendendo Python.
""")

print(f'''
Olá, meu nome é {nome},
Eu estou aprendendo Python.
''')