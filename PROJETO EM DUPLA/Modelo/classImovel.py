
class Imovel:
    def __init__(self,id_Imovel,endereco,numero, bairro, cidade):
        self._id_Imovel = id_Imovel
        self._Endereco = endereco
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade
    
        
    def criarTabelaImovel():
        sql = '''
        CREATE TABLE "Imovel"(
        "Id_Imovel" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        "Endereco" varchar(255) NOT NULL,
        "Numero" varchar(15) NOT NULL,
        "Bairro" varchar(255) NOT NULL,
        "Cidade" varchar(255) NOT NULL
        )
        '''
        return sql

    def inserirImovel(self):
        sql = f'''
        INSERT INTO "Imovel"
        values(default,'{self._Endereco}','{self._numero}', '{self._bairro}', '{self._cidade}')
        '''
        return sql







