class Cliente: 
    def __init__(self,id,nome, cpf):
        self._id = id
        self._nome= nome
        self._cpf = cpf


    def criarTabelaCliente():
        sql = '''
        CREATE TABLE "Cliente"(
        "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        "Nome" varchar(255) NOT NULL,
        "CPF" varchar(11) NOT NULL
        )
        '''
        return sql
    
    def inserirCliente(self):
        sql = f'''
        INSERT INTO "Cliente"
        values(default, '{self._nome}','{self._cpf}')
        '''
        return sql