import psycopg2

conexao = psycopg2.connect(host = 'localhost', database = 'CD', 
                         user = 'postgres', password = '')


cursor = conexao.cursor()


consulta = 'select * from clientes'

cursor.execute(consulta)

registros = cursor.fetchall()


for row in registros:
    print("nome= ", row[1])
    print("estado= ", row[2], "\n")


cursor.close()
conexao.close()