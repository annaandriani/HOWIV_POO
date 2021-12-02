import sqlite3

# conectando...
conn = sqlite3.connect('Assist.db')

# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
# cursor.execute("""
# CREATE TABLE Pessoa (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         nome TEXT NOT NULL,
#         cpf     VARCHAR(11) NOT NULL,
#         email TEXT NOT NULL,
#         fone TEXT,
#         endereco TEXT,
# );
# """)

print('Tabela criada com sucesso.')
# desconectando...
conn.close()