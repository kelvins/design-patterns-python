# -*- encoding: UTF-8 -*-

# Nota: no exemplo o código não compila, é para entender o conceito.

from connection_factory import Connection_factory

connection = Connection_factory().get_connection()

cursor = connection.cursor()

cursor.execute('SELECT * FROM cursos')

for linha in cursor:
    print linha

connection.close()