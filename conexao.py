import sqlite3
import csv


class Connect(object):

    def __init__(self, Assist):
        try:
            # conectando...
            self.conn = sqlite3.connect('Assist.db')
            self.cursor = self.conn.cursor()
            print("Banco:", 'Assist.db')
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQLite version: %s" % self.data)
        except sqlite3.Error:
            print("Erro ao abrir banco.")
            return False

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")


class AssistDb(object):
    tb_name = 'Pessoa'

    def __init__(self):
        self.db = Connect('Assist.db')
        self.tb_name

    def fechar_conexao(self):
        self.db.close_db()

    def inserir_com_parametros(self):
        # solicitando os dados ao usuário
        self.nome = input('Nome: ')
        self.cpf = input('CPF: ')
        self.email = input('Email: ')
        self.telephone = input('telephone: ')
        self.address = input('address: ')
        self.necessity = input('necessity: ')

        try:
            self.db.cursor.execute("""
           INSERT INTO Pessoa (nome, cpf, email, telephone, address, necessity)VALUES (?,?,?,?,?,?)""",
                                   (self.nome, self.cpf, self.email, self.telephone, self.address, self.necessity))

            # gravando no bd
            self.db.commit_db()
            print("Dados inseridos com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False

    def inserir_um_registro(self):
        try:
            self.db.cursor.execute("""
            INSERT INTO  Pessoa (nome, cpf, email, telephone, address, necessity) VALUES ('Regis', '00000000000', 'regis@email.com', '11-98765-4321', 'Sao Paulo-SP', 'dinheiro')""")
            # gravando no bd
            self.db.commit_db()
            print("Um registro inserido com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False

    def inserir_de_csv(self, file_name='/home/anna/PycharmProjects/pythonOrientado/Pessoa.csv'):
        try:
            reader = csv.reader(
                open(file_name, 'rt'), delimiter=',')
            linha = (reader,)
            for linha in reader:
                self.db.cursor.execute("""
                   INSERT INTO Pessoa (nome, cpf, email, telephone, address, necessity) VALUES (?,?,?,?,?,?)""", linha)
            # gravando no bd
            self.db.commit_db()
            print("Dados importados do csv com sucesso.")
        except sqlite3.IntegrityError:
            print("Aviso: O email deve ser único.")
            return False

    def ler_pessoas(self):
        sql = 'SELECT * FROM Pessoa'
        r = self.db.cursor.execute(sql)
        return r.fetchall()

    def imprimir_todas_as_pessoas(self):
        lista = self.ler_pessoas()
        for c in lista:
            print(c)

    def meu_select(self, sql="SELECT nome FROM Pessoa;"):
        r = self.db.cursor.execute(sql)
        self.db.commit_db()
        print('Nomes das pessoas que necessitam de ajuda:')
        for c in r.fetchall():
            print(c)



if __name__ == '__main__':
    c = AssistDb()
    c.inserir_de_csv()
    c.imprimir_todas_as_pessoas()
    c.meu_select()
    c.inserir_com_parametros()
