from flask import Flask, jsonify, request
from database.data import Master, Sundai

app = Flask(__name__)

def verificar_bool(fn):
    try:
        fn()
        database_response = [{'Status': True}]
    except :
        database_response = [{'Status': False}]
    else:
        database_response = [{'Status': True}]
    return database_response
    
def default(database_response):
    response = jsonify(database_response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')     
    return response

    
#============================================================
# rota de endereçamento
@app.route('/api/exibir-table',methods=['GET'])
def read():
    table = request.args.get('table')
    print(table)
    instance = Sundai()
    camposs = instance.convert_args(default=False,list_temp=instance.exibirCampos(table))
    database_response = instance.convert(fn = instance.exibirTudo(table),campos=camposs)
    response = default(database_response)

    return response

#============================================================
#   pass
@app.route('/api/drop-table',methods=['GET'])
def delete():
    table = request.args.get('table')
    try:
        instance = Sundai()
        instance.deletarTudo(table)
        database_response = [{'Status': True}]
    except:
        database_response = [{'Status': False}]


    response = default(database_response)
    return response

#============================================================
#   passXXXXXXXXX
@app.route('/api/exibir-all-table',methods=['GET'])
def selectTables():
    database_response = Sundai().exibirTodasTables()
    response = default(database_response)
    return response
     
#============================================================
#   pass
@app.route('/api/exibir-campos',methods=['GET'])
def selectTablesCampos():
    table = request.args.get('table')
    instance = Sundai()
    database_response= instance.convert_args(list_temp=instance.exibirCampos(table))
    response = default(database_response)
    return response

#============================================================
#   pass
@app.route('/api/create',methods=['GET'])
def createtable():
    args = request.args.getlist('table')
    try:
        Master(table=args[0],campos=args[1:])
        response = [{'Status': True}]
    except:
        response = [{'Status': False}]
    default(response)
    
    return response
#============================================================
#   pass
@app.route('/api/insert-table',methods=['GET'])
def InsertTables():
    campos_instance = Sundai()
    args = request.args.getlist('table')
    try:
        campos = campos_instance.convert_args(default=False,list_temp=campos_instance.exibirCampos(table=args[0]))
        i = Sundai()
        i.publicar(table=args[0],campos=campos,itensPublicar=args[1:])
        database_response = [{'Status': True}]
    except:
        database_response = [{'Status': False}]
        
    response = default(database_response)

    return response
     

if __name__ == '__main__':
    app.run(debug=True)


 

