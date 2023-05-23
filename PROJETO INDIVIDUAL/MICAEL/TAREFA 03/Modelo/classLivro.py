
class Livro:
    def __init__(self,id_Livro,titulo,autor,preco,estoque):
        self._id_Livro = id_Livro
        self._titulo = titulo
        self._autor = autor
        self._preco = preco
        self._estoque = estoque
        
    def criarTabelaLivro():
        sql = '''
        CREATE TABLE "Catalogo"(
        "Id_Livro" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        "Titulo" varchar(255) NOT NULL,
        "Autor" varchar(255) NOT NULL,
        "Preço" numeric NOT NULL default 0, 
        "Estoque" numeric NOT NULL default 0
        )
        '''
        return sql

    def inserirLivro(self):
        sql = f'''
        INSERT INTO "Catalogo"
        values(default,'{self._titulo}','{self._autor}', {self._preco}, {self._estoque})
        '''
        return sql







