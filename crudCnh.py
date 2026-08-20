import mysql.connector
from datetime import date, datetime, timedelta

# =========================
# CONEXÃO COM O BANCO
# =========================

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA_AQUI",
    database="SEU_DATABASE_AQUI"
)

cursor = conexao.cursor()


# =========================
# CADASTRAR PESSOA
# =========================

def cadastrar_pessoa():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")

    sql = """
    INSERT INTO pessoa (nome, sobrenome)
    VALUES (%s, %s)
    """

    valores = (nome, sobrenome)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Pessoa cadastrada com sucesso!")


# =========================
# LISTAR PESSOAS
# =========================

def listar_pessoas():
    cursor.execute("SELECT * FROM pessoa")

    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("Nenhuma pessoa cadastrada.")
        return

    for linha in resultados:
        print(linha)


# =========================
# CADASTRAR HABILITAÇÃO
# =========================

def cadastrar_habilitacao():
    listar_pessoas()

    pessoa_id = int(input("Digite o ID da pessoa: "))
    numero = input("Digite o número da CNH: ")
    validade = input("Digite a validade (AAAA-MM-DD): ")

    sql = """
    INSERT INTO habilitacao
    (Num_Habilitacao, Validade, Pessoa_Id_pessoa)
    VALUES (%s, %s, %s)
    """

    valores = (numero, validade, pessoa_id)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Habilitação cadastrada com sucesso!")


# =========================
# LISTAR PESSOAS + CNH
# =========================

def listar_pessoas_habilitacoes():
    sql = """
    SELECT
        pessoa.Id_pessoa,
        pessoa.Nome,
        pessoa.Sobrenome,
        habilitacao.Num_Habilitacao,
        habilitacao.Validade
    FROM pessoa
    LEFT JOIN habilitacao
    ON pessoa.Id_pessoa = habilitacao.Pessoa_Id_pessoa
    """

    cursor.execute(sql)

    resultados = cursor.fetchall()

    for linha in resultados:
        print(linha)


# =========================
# BUSCAR PESSOA
# =========================

def buscar_pessoa():
    nome = input("Digite o nome da pessoa: ")

    sql = """
    SELECT
        pessoa.Id_pessoa,
        pessoa.Nome,
        pessoa.Sobrenome,
        habilitacao.Num_Habilitacao,
        habilitacao.Validade
    FROM pessoa
    LEFT JOIN habilitacao
    ON pessoa.Id_pessoa = habilitacao.Pessoa_Id_pessoa
    WHERE pessoa.Nome LIKE %s
    """

    cursor.execute(sql, ("%" + nome + "%",))

    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("Pessoa não encontrada.")
        return

    for linha in resultados:
        print(linha)

        validade = linha[4]

        if validade is not None:
            if validade < date.today():
                print("CNH VENCIDA")
            else:
                print("CNH VÁLIDA")


# =========================
# EDITAR PESSOA
# =========================

def editar_pessoa():
    listar_pessoas()

    pessoa_id = int(input("Digite o ID da pessoa: "))

    novo_nome = input("Digite o novo nome: ")
    novo_sobrenome = input("Digite o novo sobrenome: ")

    sql = """
    UPDATE pessoa
    SET Nome = %s, Sobrenome = %s
    WHERE Id_pessoa = %s
    """

    valores = (novo_nome, novo_sobrenome, pessoa_id)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Pessoa editada com sucesso!")


# =========================
# EXCLUIR PESSOA
# =========================

def excluir_pessoa():
    listar_pessoas()

    pessoa_id = int(input("Digite o ID da pessoa que deseja excluir: "))

    # primeiro apaga a habilitação vinculada
    cursor.execute(
        "DELETE FROM habilitacao WHERE Pessoa_Id_pessoa = %s",
        (pessoa_id,)
    )

    # depois apaga a pessoa
    cursor.execute(
        "DELETE FROM pessoa WHERE Id_pessoa = %s",
        (pessoa_id,)
    )

    conexao.commit()

    print("Pessoa excluída com sucesso!")


# =========================
# EDITAR HABILITAÇÃO
# =========================

def editar_habilitacao():
    numero = input("Digite o número da CNH que deseja editar: ")

    nova_validade = input("Digite a nova validade (AAAA-MM-DD): ")

    sql = """
    UPDATE habilitacao
    SET Validade = %s
    WHERE Num_Habilitacao = %s
    """

    valores = (nova_validade, numero)

    cursor.execute(sql, valores)
    conexao.commit()

    print("Habilitação editada com sucesso!")


# =========================
# EXCLUIR HABILITAÇÃO
# =========================

def excluir_habilitacao():
    numero = input("Digite o número da CNH: ")

    sql = """
    DELETE FROM habilitacao
    WHERE Num_Habilitacao = %s
    """

    cursor.execute(sql, (numero,))
    conexao.commit()

    print("Habilitação excluída com sucesso!")


# =========================
# ALERTA DE VENCIMENTO
# =========================

def verificar_vencimentos():
    hoje = date.today()
    limite = hoje + timedelta(days=30)

    sql = """
    SELECT
        pessoa.Nome,
        pessoa.Sobrenome,
        habilitacao.Num_Habilitacao,
        habilitacao.Validade
    FROM pessoa
    JOIN habilitacao
    ON pessoa.Id_pessoa = habilitacao.Pessoa_Id_pessoa
    WHERE habilitacao.Validade BETWEEN %s AND %s
    """

    cursor.execute(sql, (hoje, limite))

    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print("Nenhuma CNH vencendo nos próximos 30 dias.")
        return

    print("\nCNHs vencendo em até 30 dias:")

    for linha in resultados:
        print(linha)


# =========================
# MENU
# =========================

while True:
    print("\n===== SISTEMA DE GESTÃO DE CNH =====")

    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Cadastrar habilitação")
    print("4 - Listar pessoas e habilitações")
    print("5 - Buscar pessoa")
    print("6 - Editar pessoa")
    print("7 - Excluir pessoa")
    print("8 - Editar habilitação")
    print("9 - Excluir habilitação")
    print("10 - Verificar CNHs vencendo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_pessoa()

    elif opcao == "2":
        listar_pessoas()

    elif opcao == "3":
        cadastrar_habilitacao()

    elif opcao == "4":
        listar_pessoas_habilitacoes()

    elif opcao == "5":
        buscar_pessoa()

    elif opcao == "6":
        editar_pessoa()

    elif opcao == "7":
        excluir_pessoa()

    elif opcao == "8":
        editar_habilitacao()

    elif opcao == "9":
        excluir_habilitacao()

    elif opcao == "10":
        verificar_vencimentos()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")


cursor.close()
conexao.close()