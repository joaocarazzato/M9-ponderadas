# Importar o Flask
import sqlite3
from flask import Flask, request
conn = sqlite3.connect('../sqlite-db/database.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados (
        id INTEGER PRIMARY KEY, sensor TEXT, valor INTEGER
    )
''')
conn.commit()

# Criar uma instância da classe Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# Rota para gravar dados
@app.route('/gravar_dado', methods = ['POST'])
def gravar_dado_api():
    query = request.args
    print(query["sensor"])
    print(query["valor"])
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dados (sensor, valor) VALUES (?, ?)", (query["sensor"], query["valor"]))
    conn.commit()
    return 'Dado gravado com sucesso!'

# Rota para obter dados
@app.route('/obter_dados', methods = ['GET'])
def obter_dados_api():
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM dados
    ''')

    dados = cursor.fetchall()
    return str(dados)

# Iniciar a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)