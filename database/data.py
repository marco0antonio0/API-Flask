import json
import sqlite3


class Master():
    #=============================================================
    #   init args 
    #   required 'campos' 'table'
    #   cria banco com nome 'table' com os campos 'campos'
    def __init__(self,campos,table):
        self.table = table
        self.con = sqlite3.connect("databaseSQL.db")
        self.cur = self.con.cursor()
        self.args =campos
        fnContatenar =' TEXT,'.join(self.args)
        self.cur.execute(f'CREATE TABLE IF NOT EXISTS {self.table}(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, {fnContatenar})')
    #=============================================================
    #   function insert only or more
    def publicar(self,argsL):
        args1 =','.join(self.args)
        args2 =','.join(len(self.args)*'?')
        self.cur.execute(f'INSERT INTO {self.table}({args1}) VALUES({args2})',argsL)
        self.con.commit()
    #=============================================================
    #   function search all
    def exibirTudo(self):
        args = self.cur.execute(f'SELECT * FROM {self.table}')
        return self.convert(args.fetchall())
        #self.convert(fn=)
    #=============================================================
    #   function search only
    def exibirApenas(self,args):
        args = self.cur.execute(f'SELECT * FROM {self.table} WHERE id= ?',[args])
        return args.fetchall()
    
    #=============================================================
    #   function search tables
    def exibirTodasTables(self):
        args = self.cur.execute('select name from sqlite_schema where type = "table" and name not like "sqlite%";')
        return args.fetchall()
    #=============================================================
    #   function exibir Campos da tabela referida
    def exibirCampos(self,table):
        args = self.cur.execute(f'PRAGMA table_info("{table}");')
        return args.fetchall()
    #=============================================================
    #   function delete all
    def deletarTudo(self):
        self.cur.execute(f'DELETE FROM {self.table}')
        self.con.commit()
    #=============================================================
    #   faz a conversão da class object sqlite para dict
    def convert(self,fn): 
        campos = self.args 
        campos.insert(0,'id')
        dados = fn
        dados_dict = []
        for linha in dados:
            d = {}
            for i in range(len(linha)):
                d[campos[i]] = linha[i]
            dados_dict.append(d)

        # Cria o arquivo JSON
        return dados_dict
    #=============================================================
    #   faz a conversão da class object sqlite para dict
    def convert_args(self,list_temp): 
        d = []
        for i in range(len(list_temp)):
            d.append(list_temp[i][1])
            pass
 
        dados_dict = []
        for i in range(len(d)):
            dd = {}
            
            dd[d[i]] = d[i]
            dados_dict.append(dd)

        # Cria o arquivo JSON
        return dados_dict
#============================================


class Sundai():
    #=============================================================
    #   init args 
    #   required 'campos' 'table'
    def __init__(self):
        self.con = sqlite3.connect("databaseSQL.db")
        self.cur = self.con.cursor()
    #=============================================================
    #   function insert only or more
    def publicar(self,itensPublicar,table,campos):
        camposs = campos[1:]
        args1 =','.join(camposs)
        args2 =','.join(len(camposs)*'?')
        self.cur.execute(f'INSERT INTO {table}({args1}) VALUES({args2})',itensPublicar)
        self.con.commit()
    #=============================================================
    #   function delete all
    def deletarTudo(self,table):
        self.cur.execute(f'DROP TABLE {table}')
        self.con.commit()

    #=============================================================
    #   function search tables
    def exibirTodasTables(self):
        args = self.cur.execute('select name from sqlite_schema where type = "table" and name not like "sqlite%";')
        return args.fetchall()
    
    #=============================================================
    #   function search all
    def exibirTudo(self,table):
        args = self.cur.execute(f'SELECT * FROM {table}')
        return args.fetchall()
    

    #=============================================================
    #   function search only
    def exibirApenas(self,args,table):
        args = self.cur.execute(f'SELECT * FROM {table} WHERE id= ?',[args])
        return args.fetchall()
    

    #=============================================================
    #   function exibir Campos da tabela referida
    def exibirCampos(self,table):
        args = self.cur.execute(f'PRAGMA table_info("{table}");')
        return args.fetchall()



    #=============================================================
    #   faz a conversão da class object sqlite para dict
    def convert(self,fn,campos=[]): 
        dados = fn
        dados_dict = []
        for linha in dados:
            d = {}
            for i in range(len(linha)):
                d[campos[i]] = linha[i]
            dados_dict.append(d)

        # Cria o arquivo JSON
        return dados_dict
    #=============================================================
    #   faz a conversão da class object sqlite para dict
    def convert_args(self,list_temp,default = True): 
        d = []
        for i in range(len(list_temp)):
            d.append(list_temp[i][1])
            pass
 
        dados_dict = []
        if default:
            for i in range(len(d)):
                dd = {}
                
                dd[d[i]] = d[i]
                dados_dict.append(dd)

        # Cria o arquivo JSON
        if default:
            return dados_dict
        else:
            return d
    



