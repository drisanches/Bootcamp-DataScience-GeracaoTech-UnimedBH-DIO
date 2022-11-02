# **Criação de Pacotes em Python**

## Módulo x Pacote

**Módulo**: objeto que serve como unidade organizacional do código que é carregado pelo comando de import.

**Pacote:** coleção de módulos com hierarquia.
  
### Vantagens da modularização

- Legibilidade
- Manutenção
- Reaproveitamento de código

### Vantagens de criar um pacote:

- Facilidade de compartilhamento
- Facilidade de instalação

## Conceitos

- **Pypi:** repositório público oficial de pacotes;
- **Wheel e Sdist:** dois tipos de distribuições;
- **Setuptools:** pacote usado em setup.py para gerar as distribuições;
- **Twine:** pacote usado para subir as distribuições no repositório Pypi.

## Estrutura de Pacote Simples

Ao utilizar o *\__init\__* dentro do pacote, permitimos que esse diretório seja invocado como módulo.

    project_name/
        README.md
        setup.py
        requirements.txt
        package_name/
            __init__.py
            file1_name.py
            file2_name.py

Para chamar determinado arquivo, utilizamos os seguintes comandos:

    import package_name.file1_name

    from package_name import file1_name

## Estrutura de Pacote com Vários Módulos

    project_name/
        README.md
        setup.py
        requirements.txt
        package_name/
            __init__.py
            module1_name/
                __init__.py
                file1_name.py
                file2_name.py
             module2_name/
                __init__.py
                file1_name.py
                file2_name.py

Para chamar determinado arquivo inserido em módulo, utilizamos os seguintes comandos:

    import package_name.module1_name.file1_name

    from package_name.module1_name import file1_name

## Passos para Criar o Projeto

1. Fork do template
2. Adição do conteúdo dos módulos do projeto
3. Edição do  arquivo setup.py
4. Edição do requirements.txt
5. Edição do README.md

### Arquivo setup.py

Usado para especificar como o pacote deve ser construído. Acesse a [Documentação Guia](https://setuptools.readthedocs.io/en/latest/setuptools.html).

**Configuração Básica:**

    from setuptools import setup, find_packages
    
    with open("README.md", "r") as f:
        page_description = f.read()
        
    with open("requirements.txt") as f:
        requirements = f.read().splitlines()
        
    setup(
        name="package_name",
        version="0.0.1",
        author="my_name",
        author_email="my_email",
        description="My short description",
        long_description=page_description,
        long_description_content_type="text/markdown",
        url="my_github_repository_project_link"
        packages=find_packages(),
        install_requires=requirements,
        python_requires='>=3.8',
    )
        

### Arquivo requirements.txt

Usado para passar as dependências que devem ser instaladas com o seu pacote. Opcionalmente, podem ser especificadas as versões. Por exemplo, Matplotlib, Scikit-Image, etc. É importante ressaltar que são apenas as dependências que devem ser instaladas juntas com o pacote e não do projeto como um todo.

### Arquivo README.md

Será exibido como documentação na página do Pypi do seu pacote. Nesse caso, foi usado o formato markdown.

## Distribuições

Para subir o pacote, devemos criar uma distribuição binária (*wheel*) ou distribuição de código fonte (*sdist*). As versões mais recentes do pip instalam primeiramente a binária e usam a distribuição de código fonte apenas se necessário.

### Passos para gerar as distribuições:

1. Acessar a raiz do projeto;
2. Comandos de instalação;
3. Comando para criar a distribuição.

**Comandos de Instalação:**

    # Primeiro temos que fazer o upgrade do pip (boa prática):
    python -m pip install --upgrade pip
    
    # Instalação da ferramenta twine 
    python -m pip install --user twine
    
    # Instalação do setuptools
    python -m pip install --user setuptools

**Comandos para Criar Distribuições:**

    python setup.py sdist bdist_wheel

## Publicar no Pypi

É uma boa prática fazer primeiramente o teste através do Test Pypi antes de subir o pacote para a versão final do Pypi.

Para criar uma conta, acesse abaixo:
[Pypi](https://pypi.org/account/register/)
[Test Pypi](https://test.pypi.org/account/register/)


### Passos para subir pacote:

1. Criar conta no Test Pypi
2. Publicar no Test Pypi
3. Instalar pacote usando Test Pypi
4. Testar pacote
5. Criar conta no Pypi
6. Publicar no Pypi
7. Instalar pacote usando Pypi

**Comando para publicar no Test Pypi:**

    python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

**Comando para instalar o pacote de teste:**

    pip install –-index-url https://test.pypi.org/simple/ image-processing

**Comando para publicar no Pypi:**

    python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

**Comando para instalar o pacote:**

    python -m pip install package_name

## Links Úteis:

[Documentação do setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)

[Testes automatizados](https://docs.pytest.org/en/latest/goodpractices.html)

[Uso do Tox](https://tox.readthedocs.io/en/latest/)

[GitHub](https://github.com/tiemi/)
