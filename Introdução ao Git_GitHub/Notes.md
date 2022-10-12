# INTRODUÇÃO AO GIT E AO GITHUB

O **Git** é um sistema de versionamento distribuído com código aberto e gratuito, também conhecido como um Sistema de Controle de Versão (SCV), que foi inicialmente desenvolvido por Linus Torvalds para resolver o problema de versionamento dos principais sistemas utilizados na época. 
Atualmente, é amplamente utilizado no universo da tecnologia como uma das melhores soluções de versionamento.

Já o **GitHub** oferece um serviço de hospedagem remota ou em nuvem do SCV, que neste caso é o Git.
Isso significa que a tecnologia por trás do Git permite a atuação simultânea de várias pessoas no mesmo projeto com um sistema de controle de versões altamente seguro e dinâmico, que pode ser feio por meio do GitHub.

## Comandos Básicos do Terminal:

- **dir:** listar diretórios (conjunto de pastas) do disco C ou qualquer outra pasta;
- **cd (change directory):** permite navegar entre as pastas e acessá-las;
- **cd ..:** retorna um nível na navegação entre as pastas;
- **cls (clear screen):** limpar o terminal [comando para Windows];
- **Ctrl + L:** limpar o terminal [comando para Linux/macOS];
- **Tab:** completa a escrita com base nos nomes das pastas;
- **mkdir (make directory):** criar nova pasta;
- **echo "texto":** apenas devolve qualquer texto que você escrever;
- **echo "texto" > "texto".txt:** pega a saída da função echo (texto) e cria um arquivo de mesmo nome de acordo com o formato definido;
- **del:** deletar arquivos (não aplicável a repositórios/pastas);
- **rmdir /S /Q (remove directory):** deletar repositórios/pastas com todos os arquivos inseridos;
  	- *Flag /S: apagar todas as pastas dentro do repositório selecionado;*
	- *Flag /Q: não abrir pergunta de confirmação.*

## Funcionamento do Git:

- **SHA1:** é uma forma única de representar um arquivo/objeto. O Git funciona com um algoritmo de encriptação de alta segurança que gera um conjunto de caracteres de 40 dígitos único para cada objeto;
- **Comando:** openss1 sha1 + arquivo/objeto (texto.txt) ~> gera a encriptação para o arquivo.

## Objetos Internos do Git:

1. **Blobs:** contêm metadados compostos por tipo, tamanho, sha1, \0 e conteúdo do objeto
	- Comando: echo -e 'blob 9\0conteudo' | openss1 sha1
	- Como passar uma string para uma função do Git e encriptar?
		- **Comando:** echo 'conteudo' | git hash-object --stdin (*stdin* apenas para que o Git entenda que não se trata de um arquivo, mas de um texto);
		- Quando feito esse comando, os arquivos são guardados nos objetos chamados Blobs, que contêm metadados.

2. **Trees:** armazenam as blobs e apontam para tipos de blobs diferentes
	- Mostram a estrutura de onde os arquivos estão salvos (diretório) e são recursivas;
	- Composta por tamanho, \0, blob (sha1 e nome do arquivo);
	- A Tree possui um sha1 específico assim como cada blob;
	- Se houver modificação de uma blob dentro da Tree, o seu sha1 também é alterado.

3. **Commits:** objeto que agrega tudo e também possui encriptação (sha1) 
	- Aponta para uma árvore/tree (sha1);
	- Aponta para um parente (último commit realizado antes dele / sha1);
	- Aponta para um autor (quem realizou a modificação);
	- Aponta para uma mensagem (explicação sobre modificação feita);
	- Aponta para um timestamp (registro da hora e horário).

Através dessa estrutura é gerado uma linha do tempo com o registro de todos os commits realizados e esse é o motivo de ser um software bastante seguro. Por isso entende-se que o Git é um sistema distribuído seguro

## Chaves SSH e Tokens do Github:

- O processo de autenticação do Git mudou em 2021;
- **Chave SSH:** forma de estabelecer uma conexão segura e encriptada entre 2 máquinas;
	- Composta por uma chave pública e uma chave privada
	- Faz o reconhecimento da máquina em que está trabalhando para configurar como uma máquina segura
- **Comando pra gerar a chave SSH no Git Bash:** ssh-keygen -t ed25519 -C *e-mail de acesso*
	- acessar id da chave: cat id_ed25519.pub
	- ativar entidade que faz o controle das chaves: eval $(ssh-agent -s)
	- enviar chave privada para a entidade: ssh-add id_ed25519
	- clonar repositório do github: git clone + *link SSH do GitHub*

## Primeiros Comandos com Git Bash:

1. **git init:** inicializar o repositório do git/Cria um repositório no Git
2. **git add:** mover arquivos e iniciar o versionamento
	- git add * (ou git add.) (move o arquivo de untracked para staged) *Nesse formato indica que devem ser consideradas todas as modificações da pasta local*
	- git add <nome do arquivo> (move somente este arquivo para staged)
3. **git commit:** criar um commit
	- git commit -m "commit inicial" (explicação de referência do commit)
4. **Outros comandos:**
	- *Comando ls:* exibe o repositório da pasta local
	- *Comando ls -a:* exibe também as pastas ocultas
	- *Comando para mover arquivos:* mv + *nome do arquivo* + ./novo local/

#### Configurando o Git no primeiro uso:

**Comandos:**
- git config --global user.email *"e-mail de acesso"*
- git config --global user.name *"nome de usuário"*

## Ciclo de Vida dos Arquivos no Git:

1. **Untracked:** arquivos não rastreáveis (Git não tem ciência deles)
2. **Tracked:** arquivos rastreáveis 
	- Unmodified: arquivo dentro do repositório do Git sem modificação
	- Modified: houve alteração no sha1
3. **Staged:** arquivos prontos para fazer parte de um commit

Após o commit, é feito um "snapshot" do código e os arquivos retornam para o modo "unmodified", ou seja, ficam registradas as modificações anteriores como estágio inicial para que o processo seja reiniciado

Quando é feito o commit, os arquivos passam a integrar o repositório local e podem ser enviados para o repositório remoto (GitHub)

Comando para consultar o status do arquivo: git status

## GitHub:

**Comandos:**
- git config --list (lista todas as configurações atribuídas)
- **Excluir configuração:** git config --global --unset user.name
- **Adicionar nova configuração:** git config --global user.name "nome de usuário"
- **Enviar repositório local do Git para repositório remoto do GitHub:**
	- git remote add origin + link do repositório do GitHub (HTTPS)
	- git remote -v (lista os repositórios remotos cadastrados)
	- git push origin master (solicita as credenciais e conclui o envio)

## Conflitos no GitHub:

**Conflito de merge:** quando o GitHub tenta mesclar duas alterações feitas feitas concomitantemente por 2 pessoas ou mais na mesma linha (uma no repositório remoto e outra no local). Nesse caso, será necessário baixar a versão mais atual do arquivo no GitHub para então fazer as alterações e enviar novamente

#### Como resolver?
- Comando Pull: git pull origin master
- Erro merge conflict in <nome do arquivo>: deve ir até o arquivo corrigir o erro
- Após a correção, seguir com os comandos:
	- git add *
	- git commit -m "resolve conflitos"

## Baixar Repositórios do GitHub:

- Caminho: Code > Download ZIP
- Clonar pelo terminal:
	- Acesse o diretório base onde quer salvar
	- **Comando:** git clone + *link do repositório (HTTPS)* -> já vem como um repositório completo