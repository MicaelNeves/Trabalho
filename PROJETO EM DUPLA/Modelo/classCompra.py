class Comercial:
    def __init__(self,id_compra,id_cliente, id_imovel, data,quitacao):
        self._id_compra = id_compra
        self._id_cliente = id_cliente
        self._id_imovel = id_imovel
        self._data = data
        self._quitacao = quitacao


    

    def criarTabelaCompra():
        sql = '''
        CREATE TABLE "Compra"(
        "Id_Compra" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        "ID_Cliente" int NOT NULL,
        "Id_Imovel" int NOT NULL,
        "Data do Aluguel" timestamp default CURRENT_TIMESTAMP(0),
        "Preço_Imovel" numeric NOT NULL default 0,
        CONSTRAINT fk_cliente
        FOREIGN KEY("ID_Cliente")
        REFERENCES "Cliente"("Id")
        ,
        CONSTRAINT fk_imovel
        FOREIGN KEY("Id_Imovel")
        REFERENCES "Imovel"("Id_Imovel")
        )
        '''
        return sql
    
    def inserirCompra(self):

        sql = f'''
        INSERT INTO "Compra"
        values(default, {self._id_cliente},{self._id_imovel}, default, '{self._quitacao}')
        '''
        return sql

