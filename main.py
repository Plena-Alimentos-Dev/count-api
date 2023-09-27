import pyodbc
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Função para criar uma conexão com o banco de dados
def criar_conexao():
    server = "192.168.248.24"
    database = "SATKCONTAGEM"
    username = 'svc_rastreabilidade'
    password = '7rBVyTI@mu56'
    string_conexao = (
        'DRIVER={sql server};SERVER=' + server +
        ';DATABASE=' + database +
        ';UID=' + username +
        ';PWD=' + password
    )
    conexao = pyodbc.connect(string_conexao)
    conexao.setencoding(encoding='utf-8')
    conexao.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
    conexao.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
    return conexao

@app.route("/contador/<carga>")
def contador(carga):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute(f"""
            SELECT DISTINCT
                CONVERT(varchar, rom.Cod_filial_volume) + '-' +
                CONVERT(varchar, rom.Serie_volume) + '-' +
                CONVERT(varchar, rom.Num_volume) AS ID
            FROM
                tbSaidas s WITH(NOLOCK)
            INNER JOIN
                tbSaidasItemRom rom WITH(NOLOCK) ON s.Chave_fato = rom.Chave_fato
            WHERE
                s.Serie_carga = '001' AND
                s.Num_carga = '{carga}'
        """)

        results = cursor.fetchall()
        count = len(results)

        # Feche o cursor e a conexão após usar
        cursor.close()
        conexao.close()

        return jsonify({"count": count})
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run()
