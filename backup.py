import sqlite3
import io

conn = sqlite3.connect('Assist.db')

with io.open('Assist_dump.sql', 'w') as f:
    for linha in conn.iterdump():
        f.write('%s\n' % linha)

print('Backup realizado com sucesso.')
print('Salvo como Assist_dump.sql')

conn.close()