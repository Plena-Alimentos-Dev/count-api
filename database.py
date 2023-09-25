import pyodbc

server = "SQLCO"
database = "SATKCONTAGEM"
username = 'svc_rastreabilidade'
password = '7rBVyTI@mu56'
string_conexao = 'Driver={SQL Server};Server='+server+';Database='+database+';UID='+username+';PWD='+password

conexao = pyodbc.connect(string_conexao)
cursor = conexao.cursor()