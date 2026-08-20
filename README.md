# Sistema de Gestão de Habilitações

Projeto desenvolvido em Python com integração ao MySQL para praticar conceitos de banco de dados e operações CRUD.

## Funcionalidades

* Cadastro de pessoas
* Cadastro de habilitações vinculadas a uma pessoa
* Listagem de pessoas
* Listagem de pessoas com suas habilitações
* Busca de pessoas por nome
* Verificação de habilitação válida ou vencida
* Edição de pessoas
* Exclusão de pessoas
* Edição de habilitações
* Exclusão de habilitações
* Alerta para habilitações vencendo em até 30 dias

## Tecnologias utilizadas

* Python
* MySQL
* MySQL Connector for Python

## Instalação

Instale a dependência necessária:

```bash
pip install mysql-connector-python
```

Depois, configure a conexão com o banco de dados no arquivo `main.py`:

```python
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA_AQUI",
    database="SEU_BANCO_AQUI"
)
```

No campo `password`, coloque a senha do seu MySQL.

No campo `database`, coloque o nome do banco de dados que você deseja utilizar.

Não publique sua senha real no GitHub.

## Banco de dados

O arquivo `database.sql` contém os comandos necessários para criar as tabelas utilizadas pelo sistema.

## Execução

Depois de configurar o banco de dados e instalar o MySQL Connector, execute:

```bash
python main.py
```

O sistema funciona pelo terminal e utiliza entradas do usuário por meio de `input()`.
