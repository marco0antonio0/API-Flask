# Facilities Flask API

![img](image-readme/image_readme.png)
<span><br>O API_FLASK_FACILITIES é um software que oferece uma maneira simples e eficiente de criar APIs com Flask, juntamente com a implementação de um banco de dados local. Com essa ferramenta, é possível criar APIs em questão de minutos, sem a necessidade de uma grande expertise em programação ou em Flask. <br><span>

## Porque usar a Facilities FLASK API?

<span><br>Uma das grandes vantagens do API_FLASK_FACILITIES é a facilidade em manipular o banco de dados local. Isso acontece porque a passagem de dados é feita por meio da URL, o que torna todo o processo muito intuitivo. Além disso, essa abordagem permite que a API seja facilmente integrada a outras aplicações.  Outra vantagem do API_FLASK_FACILITIES é a sua facilidade de criação. Com poucas linhas de código é possível implementar uma API com todas as funcionalidades necessárias, como rotas, métodos e autenticação de usuários. Isso torna o processo de criação muito mais rápido e eficiente, reduzindo o tempo e os custos necessários para implementar uma API completa.  O software também é altamente personalizável, permitindo que os usuários criem suas próprias rotas e métodos de acordo com suas necessidades específicas. Além disso, o API_FLASK_FACILITIES é altamente escalável, o que significa que ele pode ser facilmente adaptado para atender a demandas de maior volume. <br><span>

### Função exibir tabela especifica

```
@app.route('/api/exibir-table',methods=['GET'])
def read():
    table = request.args.get('table')
    print(table)
    instance = Sundai()
    camposs = instance.convert_args(default=False,list_temp=instance.exibirCampos(table))
    database_response = instance.convert(fn = instance.exibirTudo(table),campos=camposs)
    response = default(database_response)

    return response
```

<span>Aplicação facilities flask api ativa, pesquise no navegador <br>localhost:5000/api/exibir-table?table= < nome_table > <br><span>

### Função deletar uma tabela especifica tabela

```
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
```

<span>A aplicação facilities flask api ativa, pesquise no navegador <br>localhost:5000/api/drop-table?table= < nome_table > <br><span>

### Função exibir todas as tabelas

```
@app.route('/api/exibir-all-table',methods=['GET'])
def selectTables():
    database_response = Sundai().exibirTodasTables()
    response = default(database_response)
    return response
```

<span>A aplicação facilities flask api ativa, pesquise no navegador <br>localhost:5000/api/exibir-all-table <br><span>

### Função exibir todos os campos de uma tabela especifica

```
@app.route('/api/exibir-campos',methods=['GET'])
def selectTablesCampos():
    table = request.args.get('table')
    instance = Sundai()
    database_response= instance.convert_args(list_temp=instance.exibirCampos(table))
    response = default(database_response)
    return response
```

<span>A aplicação facilities flask api ativa, pesquise no navegador <br>localhost:5000/api/exibir-campos?table=< nome_table > <br><span>

### Função criar uma tabela e seus campos

```
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
```

<span>A aplicação facilities flask api ativa, pesquise no navegador <br>localhost:5000/api/create?table=< nome_table >?table=< nome_campo_1 >?table=< nome_campo_2 >?table=< n_nome_campos > <br><span>

### Função inserir dados uma tabela em uma tabela especifica

```
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
```

<span>A aplicação facilities flask api ativa, pesquise no navegador <br>localhost:5000/api/insert-table?table=< nome_table >?table=< dados_campo_1 >?table=< dados_campo_2 >?table=< n_dados_campos > <br><span>

## Equipe de desenvolvimento

#### > Marco Antonio

#### > Jean

## Ferramentas

#### > VSCODE && PYTHON && FLASK

#### > FIGMA && CANVA

## Documentação
