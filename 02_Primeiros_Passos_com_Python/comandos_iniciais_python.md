# PRIMEIROS PASSOS COM PYTHON:

## Tipos de Dados:

- Definem as características e comportamentos de um objeto (valor)
- Tipos Built-in:
	- Texto: str
	- Numérico: int, float, complex
	- Sequência: list, tuple, range
	- Mapa: dict 
	- Coleção: set, fronzenset (parecido com lista, mas sem itens repetidos)
	- Booleano: bool (V/F)
	- Binário: bytes, bytearray, memoryview

**Booleano:** representa verdadeiro ou falso e é implementado pela classe bool. O tipo booleano é uma subclasse de int, pois qualquer número diferente de 0 representa verdadeiro e 0 representa falso.

## Usando o Modo Interativo do Python:

- O modo interativo do interpretador Python possibilita a visualização do resultado do código em tempo real.
- Como acionar: basta escrever python no terminal ou executar o script com a flag -i (*python -i app.py*) app é o arquivo que deseja abrir
- Para sair deste modo, basta digitar *exit()*

## Funções:

- **dir:** 
	- sem argumentos dir(), retorna a lista de nomes do escopo local atual
	- com argumentos dir(100), retorna uma lista de atributos e métodos válidos para o objeto
- **help:** invoca o sistema de ajuda integrado
	- Informa por parâmetro qual o nome do módulo, função, classe ou variável

## Variáveis e Constantes:

**Variáveis:** valores passíveis de alterações no decorrer da execução do programa.
- Formas de declarar as variáveis: age = 23 / name = 'Dri' ou age, name = (23, 'Dri') *os () são opcionais*
- Para alterar o valor da variável, basta atribuir um valor diferente do anterior 

**Constantes:** também armazenam valores, porém não é passível de alteração e permanece com o mesmo valor até o final da execução do programa.
- Python não tem uma palavra reservada para constante. A forma de definir uma constante é utilizar o nome todo em letras maiúsculas, que é uma convenção adotada em Python.

**Boas Práticas:**

- O padrão de nomes deve ser *snake case*, ou seja, deve-se substituir os espaços em brancos por underline (_);
- Deve-se adotar nomes sugestivos, ou seja, que sejam fáceis de correlacionar com o objetivo da variável;
- As constantes devem sere escritas todas em maiúsculo.

## Conversão de Tipos:

- Converter para float: float(variável)
	- Quando é feita a divisão entre 2 inteiros, o resultado automaticamente é convertido para float
- Converter para inteito: int(variável)
	- Quando é feita a divisão usando //, o resultado retorna em inteiro
- Converter valor numérico para string: str(variável)
	- Quando a string é composta por texto somente com letras, a conversão não é possível

## Funções de Entrada e Saída:

- **Função Input/Output:** utilizada quando queremos ler dados da entrada padrão (teclado). Recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). Resumindo, a função lê a entrada, converte para string e retorna o valor.
	- nome = input("Informe o seu nome: ")
	- Quando for informado um nome, este conteúdo será convertido para string e será atribuído à variável nome.
- **Função Print:** usada quando queremos exibir dados na saída padrão (tela). 
	- Recebe um argumento obrigatório do tipo *varargs de objetos* e 4 argumentos opcionais (sep, end, file e flush);
	- Todos os objetos são convertidos para string;
	- print(nome, sobrenome); 
	- print (nome, sobrenome, end="...\n") Dá o comando para finalizar com 3 pontos e adiciona uma quebra de linha;
	- print(nome, sobrenome, sep='#') Dá o comando para substituir o separador padrão (espaço) por #;;
- print (nome, sobrenome, end="...\n", sep='#').

## Tipos de Operadores:

1. **Operadores Aritméticos:** executam operações matemáticas entre 2 ou mais valores
- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/ para float ou // para int)
- Exponenciação (**)
- Módulo (% - resto da divisão)

**Precedência dos Operadores:**
- parêntesis > expoentes > multiplicações e divisões (da esquerda para a direita) > somas e subtrações (da esquerda para a direita)
- Deixar a ordem das operações explícitas é uma boa prática na programação

2. **Operadores de Comparação:** retornam o valor true ou false
- Igualdade (==)
- Diferença (!=)
- Maior (>) / Menor (<)
- Maior ou Igual (>=)
- Menor ou Igual (<=)

3.**Operadores de Atribuição:** usados para definir o valor inicial ou sobrescrever o valor de uma variável
- Atribuição simples (=): saldo = 500
- Atribuição com adição (+=): saldo += 200
- Atribuição com subtração (-=): saldo -= 100
- Atribuição com multiplicação (*=): saldo *= 2
- Atribuição com divisão (/=): saldo /= 5
- Atribuição com divisão inteiro (//=): saldo //= 5
- Atribuição com módulo (%=): saldo %= 480
- Atribuição com exponenciação (**=): saldo **= 80

4. **Operadores Lógicos:** representam uma expressão lógica que retorna um booleano
- And: saldo >= saque and saque <= limite (só é valido se ambas as partes são verdadeiras, caso contrário retorna falso )
- Or: saldo >= saque or saque <= limite (só é válido se pelo menos uma das partes for verdadeira, caso contrário retorna falso)
- Not (comparador de negação): not 1000 > 1500 (inverte o resultado da comparação que seria false e retorna true)
	- Se eu colocar o not associado a uma lista, ele vai avaliar se existe alguma conteúdo nela. Lista vazia retorna o valor de true e lista preenchida retorna o valor de false
 	- O mesmo vale para strings, se eu associar o not com uma string e ela tiver algum valor (not "saque 1500"), retorna false. Se não tiver valor (not ""), retorna true.

5. **Operadores de Identidade:** usados para comparar se os dois objetos testados ocupam a mesma posição na memória
- Is: objeto A ocupa o mesmo espaço na memória que o objeto B? Retorna True ou False
	- Ex.: curso is nome_curso (retorna verdadeiro se ambos tiverem o mesmo valor)
- Is not: objeto A não ocupa o mesmo espaço na memória que o objeto B? Retorna True ou False
	- Ex.: curso is not nome_curso

6. **Operadores de Associação:** utilizados para verificar se um objeto está presente em uma sequência
- In: verifica se algo está em determinada sequência/lista/string
- Not in: verifica se o objeto não está em determinada em determinada sequência/lista/string

# ESTRUTURAS CONDICIONAIS E DE REPETIÇÃO

## Indentação e Blocos de Comando:

É uma forma de manter o código fonte mais legível e manutenível, além disso o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

De acordo com a convenção em Python, as boas práticas indicam o uso de 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

O símbolo que indica o início do bloco em Python é os dois pontos (:). O Python reconhece o fim do bloco quando a indentação retorna ao valor inicial (sem espaços).

## Estruturas Condicionais: 

As estruturas condicionais permitem o desvio do fluxo de controle, quando determinadas expressões lógicas são atendidas.

1. **If:** 
if saldo >= saque:
	print("Realizando saque!")
if saldo < saque:
	print("Saldo insuficiente!")

2. **If-else:**
if saldo >= saque:
	print("Realizando saque!")
else:
	print("Saldo insuficiente!")
 
3. **If-elif-else:** a palavra reservada elif (else + if) permite mais de dois desvios no bloco. O elif é composto por uma nova expressão lógica, que será testada e, caso retorne verdadeiro, o bloco de código do elif será executado.
- Não existe um número máximo de elifs que podemos utilizar, mas deve-se evitar criar grandes estruturas condicionais pois elas aumentam a complexidade do código.

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
	valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
	print("Exibindo o extrato...")
else:
	sys.exit(Opção Inválida")

4. **If aninhado:** estruturas condicionais aninhadas são formadas pela conjunção de várias estruturas if-elif-else dentro do bloco de código.

if conta_normal:
	if saldo >= saque:
		print("Saque realizado com sucesso!")
	elif saque <= (saldo + cheque_especial):
		print("Saque realizado com sucesso com uso do cheque especial!")
elif conta_universitaria:
	if saldo >= saldo:
		print("Saque realizado com sucesso!")
	else:
		print("Saldo insuficiente!")

5. **If ternário:** permite escrever uma condição em uma única linha.
- Composto por 3 partes:
	- Primeira: retorno caso a expressão retorne verdadeiro;
	- Segunda: expressão lógica;
	- Terceira: retorno caso a expressão não seja atendida.

Exemplo:
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")

## Estruturas de Repetição:

As estruturas de repetição são utilizadas para repetir um trecho de código um determinado número de vezes, que pode ser conhecido previamente ou determinado através de uma expressão lógica.

1. **For:** usado para percorrer um objeto iterável. Seu uso é válido quando sabemos o número exato de vezes que nosso bloco de código deve ser excutad, ou quando queremos percorrer um objeto iterável.
- Estrutura: for *objeto sendo iterado* in *objeto iterável*

texto = input("Informe um texto: ")
VOGAIS = "AEIOU" *constante*

for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end="")

1.1. **For/Else:** 

texto = input("Informe um texto: ")
VOGAIS = "AEIOU" *constante*

for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end="")
else:
	print("") *adiciona uma quebra de linha*
	print("Executa o final do laço.")

1.2. **Função Range:** função built-in usada para produzir uma sequência de números inteiros a partir de um início (inclusivo, ou seja, inclui este valor no intervalo) para um fim (exclusivo, ou seja, exclui esse valor do intervalo).
- Se usarmos a função range(i,j) será produzido i, i+1, i+2, i+3, ..., j-1.
- Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e set (opcional).
- Estrutura: range(stop) / range(start, stop[, step])
- Exemplo: list(range(4)) retorna uma lista [0, 1, 2, 3]
- Uso com for:

Exemplo 1:

for numero in range(0, 11):
	print(numero, end="")

retorna = 0 1 2 3 4 5 6 7 8 9 10

Exemplo 2:

for numero in range(0, 51, 5): *step 5 instrui para contar de 5 em 5*
	print(numero, end="")

retorna = 0 5 10 15 20 25 30 35 40 45 50

2. **While:** usado para repetir um bloco de códigos várias vezes. É válido quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

Exemplo:

opcao = -1

while opcao != 0: *diferente de zero*
	opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

	if opcao == 1:
		print("Sacando...")
	elif opcao == 2:
		print("Exibindo o extrato...")

2.2. **While/Else:**

opcao = -1

while opcao != 0: *diferente de zero*
	opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

	if opcao == 1:
		print("Sacando...")
	elif opcao == 2:
		print("Exibindo o extrato...")
else:
	print("Obrigado por utilizar nosso sistema bancário, até logo!")

2.3. **Break:** palavra reservada que interrompe o fluxo do código definido na estrutura While se uma determinada condição for atingida.

Exemplo:

While True: *enquanto a expressão lógica for verdadeira, imprima o número (laço infinito)*
	numero = int(input("Informe um número: "))

	if numero == 10; *se o número for 10, não execute o código/corte o laço da repetição*
		break

	print(numero)

Exemplo com for:

for numero in range(100):

	if numero == 10 *Interrompe a execucação do código ao atingir o valor 10, então imprime somente até o número 9*
		break

	print(numero, end=" ")

Retorna = 0 1 2 3 4 5 6 7 8 9

Exemplo Continue:

for numero in range(100):

	if numero == 12 *Interrompe a execucação do código no número 12 e segue para o próximo número na sequência*
		continue

	print(numero, end=" ")

Retorna = 0 1 2 3 4 5 6 7 8 9 10 11 13 14 15 16 ... 99
