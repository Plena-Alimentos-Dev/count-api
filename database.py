import pyodbc


class BancoDeDados:
    def __init__(self, servidor='', base='', usuario='', senha=''):
        self.servidor = '192.168.248.24' if not servidor else servidor
        self.base = 'SATKCONTAGEM' if not base else base
        self.usuario = 'svc_rastreabilidade' if not usuario else usuario
        self.senha = '7rBVyTI@mu56' if not senha else senha
        self.status = True
        self.getErro = None

        try:
            string_conexao = (
                'Driver=FreeTDS;Server=' + self.servidor +
                ';Database=' + self.base +
                ';ClientCharset=UTF-8' +
                ';UID=' + self.usuario +
                ';PWD=' + self.senha
            )
            
            self.conexao = pyodbc.connect(string_conexao)
            self.conexao.setencoding(encoding='utf-8')
            self.conexao.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
            self.conexao.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
            self.cursor = self.conexao.cursor()
        except pyodbc.Error as ex:
            self.status = False
            self.getErro = '<div class="alert-danger">' + str(ex) + '</div>'

# Exemplo de uso da classe BancoDeDados
conexao_bd = BancoDeDados()
if conexao_bd.status:
    # Sua conexão foi bem-sucedida, você pode usar a conexão e o cursor aqui.
    cursor = conexao_bd.cursor
    # Realize as operações no banco de dados aqui.
else:
    print(conexao_bd.getErro)
