class Cliente: 
    def __init__(self,id,nome, cpf,telefone,email):
        self._id = id
        self._nome= nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email


    def criarTabelaCliente():
        sql = '''
        CREATE TABLE "Cliente"(
        "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        "Nome" varchar(255) NOT NULL,
        "CPF" varchar(11) NOT NULL,
        "Telefone" varchar(9) NOT NULL,
        "Email" varchar(255) NOT NULL
        )
        '''
        return sql
    
    def inserirCliente(self):

        sql = f'''
        INSERT INTO "Cliente"
        values(default, '{self._nome}','{self._cpf}','{self._telefone}','{self._email}')
        '''
        return sql
    
    def removerCliente(self, numero):

        sql = f'''
        DELETE FROM "Cliente"
        WHERE "Id" = '{numero}'
        '''
        return sql