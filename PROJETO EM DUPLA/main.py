import psycopg2
from Controle.classControle import Conexao
from Modelo.classCliente import Cliente
from Modelo.classImovel import Imovel
from Modelo.classCompra import Comercial
from customtkinter import *
from tkinter import *
from functools import partial
import tkinter as tk
from tabulate import tabulate


# Conexão no Banco de Dados

conexao = Conexao("Empresa", "localhost", "5432", "postgres", "postgres")

# Criação de Tabelas no Banco

def CriarTabelas(aux):

    while aux<2:
        try: 
           # conexao.manipularBanco(Cliente. criarTabelaCliente())
           # conexao.manipularBanco(Imovel. criarTabelaImovel())
           # conexao.manipularBanco(Comercial. criarTabelaCompra())
            print("Tabelas Criadas com sucesso!")
        except(Exception,psycopg2.Error) as error:
            print("Algo deu Errado! ",error)

        aux += 1

# CriarTabelas(1)

set_appearance_mode("dark")

class App(Tk):
    def __init__(self):
        super().__init__()

        
        self.title("Sistema de Gerenciamento")
        self.geometry("600x400")
        self.resizable(False,False)
        
        
        imagem = PhotoImage(file = "vniokprancheta-30-3-1468-566(2).png")   
        label_img = CTkLabel(master = self,image = imagem,text = "",compound ="center")
        label_img.place(x=2,y=2)
        
        self.telaInicial = CTkFrame(self,corner_radius= 8,width=300,height = 295, fg_color="light cyan")
        self.telaInicial.pack(side = "right", anchor = "ne")
        
        self.mensagem = CTkLabel(self.telaInicial, text="Tela Inicial",text_color="black",font=CTkFont(size=16,weight="bold"), compound="top", wraplength=500)
        self.mensagem.grid(column=3,row=0, pady= 8,sticky="nsew")

        self.botaoImovel = CTkButton(self.telaInicial, text="Clientes",width=250 ,command=self.abrir_menu_secundario)
        self.botaoImovel.grid(column=3,row=1, padx= 20, pady= 25,sticky="nsew")
        self.botaoCliente = CTkButton(self.telaInicial, text="Imóveis",width=250, command=self.abrir_menu_secundario1)
        self.botaoCliente.grid(column=3, row=2, padx= 20, pady= 25,sticky="nsew")
        self.botaoVenda = CTkButton(self.telaInicial, text="Comercial",width=250, command=self.abrir_menu_secundario2)
        self.botaoVenda.grid(column=3,row=3, padx= 20, pady= 25,sticky="nsew")

    def abrir_menu_secundario(self):
        self.destroy()
        self.menu_secundario = MenuClientes()

    def abrir_menu_secundario1(self):
        self.destroy()
        self.menu_secundario = MenuImoveis()

    def abrir_menu_secundario2(self):
        self.destroy()
        self.menu_secundario = MenuCompra()

    def iniciar(self):
        self.mainloop()
            
 
set_appearance_mode("dark") 


class MenuClientes(Tk):
    def __init__(self):
        super().__init__()
        

        self.title("Sistema de Gerenciamento")
        self.geometry("700x400")
        self.resizable(False,False)

        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=4)


        #Menu de navegação
        self.menuNavegacao = CTkFrame(self, fg_color="light cyan")
        self.menuNavegacao.grid(column=0, row=0, sticky="nsew")

        self.menuNavegacao.columnconfigure(0, weight=1)

        self.label = CTkLabel(master = self.menuNavegacao,font= CTkFont(size=16, weight = "bold"), text = "Menu Clientes",text_color = "black", compound= "top")
        self.label.grid(column=0,row=0, padx= 20, pady= 25)
        self.botaoAtualizarDados = CTkButton(self.menuNavegacao, text="Atualizar dados ", command=partial(self.abrirTela,"Atualizar dados"))
        self.botaoAtualizarDados.grid(column=0,row=3, padx= 20, sticky="ew", pady = 15)

        self.botaoInserirCliente = CTkButton(self.menuNavegacao, text="Inserir Cliente", command=partial(self.abrirTela,"Inserir Cliente"))
        self.botaoInserirCliente.grid(column=0, row=1, padx= 20, sticky="ew", pady = 15)

        self.botaoVisualizarClientes = CTkButton(self.menuNavegacao, text="Visualizar Clientes", command=partial(self.abrirTela,"Visualizar Clientes"))
        self.botaoVisualizarClientes.grid(column=0, row=2, padx= 20, sticky="ew", pady = 15)

        self.botaoRemoverClientes = CTkButton(self.menuNavegacao, text="Remover Clientes", command=partial(self.abrirTela,"Remover Clientes"))
        self.botaoRemoverClientes.grid(column=0, row=4, padx= 20, sticky="ew", pady = 15)

        self.botaoImovel = CTkButton(self.menuNavegacao, text="Voltar a Tela Inicial",command=self.voltar_menu_principal)
        self.botaoImovel.grid(column=0,row=5, padx= 20, sticky="ew", pady = 15)


        #Tela Inicial
        self.telaInicial = CTkFrame(self, fg_color="gray")
        self.telaInicial.grid(column=1, row=0, sticky="nsew")

       
        self.mensagemBoasVindas = CTkLabel(self.telaInicial, text="Bem vindo ao Sistema de Gerenciamento de Clientes",text_color="black",font=CTkFont(size=32, weight="bold"),wraplength=300)
        self.mensagemBoasVindas.grid(column=1, row=0, pady = 120, padx = 120)

        #Tela Inserir Cliente

        self.telaInserirCliente = CTkFrame(self, fg_color="transparent")
        self.telaInserirCliente.grid_columnconfigure(0,weight=1)

        self.tituloInserirCliente = CTkLabel(self.telaInserirCliente, text= "Inserir Cliente", font=CTkFont(size=20, weight= "bold"), text_color = "black")
        self.tituloInserirCliente.grid(column=0, row=0,sticky="ew",pady = 15)

        self.rotuloNome = CTkLabel(self.telaInserirCliente, text= "Nome: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloNome.grid(column=0, row=1, padx= 15, pady =15,) 
 
        self.campoNome = CTkEntry(self.telaInserirCliente, placeholder_text=("Digite o nome do cliente"))
        self.campoNome.grid(column=1, row=1, padx= 30, pady = 15,sticky="ew")

        self.rotuloCPF = CTkLabel(self.telaInserirCliente, text= "CPF: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloCPF.grid(column=0, row=2, padx= 15, pady = 15) 

        self.campoCPF = CTkEntry(self.telaInserirCliente, placeholder_text=("Digite o CPF do cliente"))
        self.campoCPF.grid(column=1, row=2, padx= 30, pady = 15)

        self.campoTelefone = CTkEntry(self.telaInserirCliente, placeholder_text=("Digite o telefone do cliente"))
        self.campoTelefone.grid(column=1, row=3, padx= 30, pady = 15)

        self.rotuloTelefone = CTkLabel(self.telaInserirCliente, text= "Telefone: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloTelefone.grid(column=0, row=3, padx= 15, pady = 15) 

        self.campoEmail = CTkEntry(self.telaInserirCliente, placeholder_text=("Digite o Email do cliente"))
        self.campoEmail.grid(column=1, row=4, padx= 30, pady = 15, sticky = "ew")

        self.rotuloEmail = CTkLabel(self.telaInserirCliente, text= "Email: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloEmail.grid(column=0, row=4, padx= 15, pady = 15) 

        self.botaoInserirCliente = CTkButton(self.telaInserirCliente, text="Enviar", command=self.inserirClienteBanco)
        self.botaoInserirCliente.grid(column=1, row=5,pady = 15)

        self.rotuloResultado = CTkLabel(master= self.telaInserirCliente)
        self.rotuloResultado.grid(column=1, row=6)


        # Visualizar Clientes

        self.telaVisualizarClientes = CTkFrame(self, fg_color="transparent")
        self.telaVisualizarClientes.grid_columnconfigure(0,weight=1)
        self.telaVisualizarClientes.grid_rowconfigure(1,weight=1)

        self.tituloVisualizarClientes = CTkLabel(self.telaVisualizarClientes, text= "Lista de Clientes",text_color = "black" ,font=CTkFont(size=24))
        self.tituloVisualizarClientes.grid(column=0, row=0)

        self.listaDeClientes = CTkTextbox(self.telaVisualizarClientes, fg_color="transparent", text_color="black")
        self.listaDeClientes.grid(column=0, row =1, sticky="nsew")

       # Remover Clientes
    
        self.telaRemoverClientes = CTkFrame(self, fg_color="transparent")
        self.telaRemoverClientes.grid_columnconfigure(0,weight=1)
        self.telaRemoverClientes.grid_rowconfigure(1,weight= 1)

        self.tituloRemoverClientes = CTkLabel(self.telaRemoverClientes, text= "Remover Cliente",text_color = "black" ,font=CTkFont(size=16), compound = "center")
        self.tituloRemoverClientes.grid(row=0, sticky = "ew")

        self.campoRemover = CTkEntry(self.telaRemoverClientes, placeholder_text=("Digite o id do cliente para remoção"))
        self.campoRemover.grid(column=1, row=1, padx= 75, pady = 10, sticky = "ew")

        self.rotuloRemover = CTkLabel(self.telaRemoverClientes, text= "Id_Cliente: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloRemover.grid(column=0, row=1, padx= 7, pady = 10) 

        self.botaoRemoverCliente = CTkButton(self.telaRemoverClientes, text="Enviar", command=self.removerClienteBanco)
        self.botaoRemoverCliente.grid(column=1, row=2,pady = 15)

        self.rotuloConfirmarRemover = CTkLabel(master= self.telaRemoverClientes)
        self.rotuloConfirmarRemover.grid(column=1, row=3, pady =15)


        # Atualizar Dados Cadastrais 

        self.novatelaAtualizarDados = CTkFrame(self, fg_color="transparent")
        self.novatelaAtualizarDados.grid_columnconfigure(0,weight=1)
        self.novatelaAtualizarDados.grid_rowconfigure(1,weight= 1)


        self.novorotuloNome = CTkLabel(self.novatelaAtualizarDados, text= "Nome: ",text_color = "black", font=CTkFont(size= 16))
        self.novorotuloNome.grid(column=0, row=3, padx= 15, pady =15,) 
 
        self.novocampoNome = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o nome do cliente"))
        self.novocampoNome.grid(column=1, row=3, padx= 30, pady = 15,sticky="ew")

        self.novorotuloCPF = CTkLabel(self.novatelaAtualizarDados, text= "CPF: ",text_color = "black", font=CTkFont(size= 16))
        self.novorotuloCPF.grid(column=0, row=4, padx= 15, pady = 15) 

        self.novocampoCPF = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o CPF do cliente"))
        self.novocampoCPF.grid(column=1, row=4, padx= 30, pady = 15,sticky = "ew")

        self.novocampoTelefone = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o telefone do cliente"))
        self.novocampoTelefone.grid(column=1, row=5, padx= 30, pady = 15,sticky = "ew")

        self.novorotuloTelefone = CTkLabel(self.novatelaAtualizarDados, text= "Telefone: ",text_color = "black", font=CTkFont(size= 16))
        self.novorotuloTelefone.grid(column=0, row=5, padx= 15, pady = 15) 

        self.novocampoEmail = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o Email do cliente"))
        self.novocampoEmail.grid(column=1, row=6, padx= 30, pady = 15, sticky = "ew")

        self.novorotuloEmail = CTkLabel(self.novatelaAtualizarDados, text= "Email: ",text_color = "black", font=CTkFont(size= 16))
        self.novorotuloEmail.grid(column=0, row=6, padx= 15, pady = 15) 

        self.novotituloAtualizarDados = CTkLabel(self.novatelaAtualizarDados, text= "Atualizar Cadastro",text_color = "black" ,font=CTkFont(size=16), compound = "center")
        self.novotituloAtualizarDados.grid(row=0, sticky = "ew")

        self.campoAtualizar = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("ID que será atualizado"))
        self.campoAtualizar.grid(column=1, row=1, padx= 30, pady = 10, sticky = "ew")

        self.rotuloAtualizar = CTkLabel(self.novatelaAtualizarDados, text= "Id_Cliente: ",text_color = "black", font=CTkFont(size= 16))
        self.rotuloAtualizar.grid(column=0, row=1, padx= 7, pady = 10) 

        self.botaoAtualizarCliente = CTkButton(self.novatelaAtualizarDados, text="Enviar", command=self.atualizarClienteBanco)
        self.botaoAtualizarCliente.grid(column=0, row=7,pady = 15)

        self.rotuloConfirmarAtualizar = CTkLabel(master= self.novatelaAtualizarDados)
        self.rotuloConfirmarAtualizar.grid(column=1, row=7, pady =15)


  

    def atualizarClienteBanco(self):

        escolha = self.campoAtualizar.get()

        nome = self.novocampoNome.get()
        cpf = self.novocampoCPF.get()
        telefone = self.novocampoTelefone.get()
        email = self.novocampoEmail.get()
        
        aux = conexao.consultarBanco(f'''
            Select * From "Cliente"
            where "Id" = '{escolha}'
            ''')

        
        if not escolha:
            self.rotuloConfirmarAtualizar.configure(text="Digite o id do cliente", text_color="red")

        
        elif not  aux:
            self.rotuloConfirmarAtualizar.configure(text="Cliente não encontrado", text_color="red")


        else:
            conexao.manipularBanco(f'''
            UPDATE "Cliente"
            SET
              "Nome" = '{nome}',
              "CPF" = '{cpf}',
              "Telefone" = '{telefone}',
              "Email" = '{email}'
            WHERE
              "Id" = '{escolha}'
            ''')


            if escolha not in aux:
                self.rotuloConfirmarAtualizar.configure(text = "Dados atualizados", text_color = "green")
            elif escolha in aux:
                self.rotuloConfirmarAtualizar.configure(text = "Dados não atualizados", text_color = "red")



    def removerClienteBanco(self):
        
        escolha = self.campoRemover.get()

        aux = conexao.consultarBanco(f'''
            Select * From "Cliente"
            where "Id" = '{escolha}'
            ''')
        
        if not escolha:
            self.rotuloConfirmarRemover.configure(text="Digite o id do cliente", text_color="red")

        
        elif not aux:
            self.rotuloConfirmarRemover.configure(text="Cliente não encontrado", text_color="red")
    

        else:
            conexao.manipularBanco(f'''
            DELETE FROM "Cliente"
            WHERE "Id" = '{escolha}'
            ''')


            if escolha not in aux:
                self.rotuloConfirmarRemover.configure(text = "Cliente Removido", text_color = "green")
            elif escolha in aux:
                self.rotuloConfirmarRemover.configure(text = "Cliente não removido", text_color = "red")
 

        
    def inserirClienteBanco(self):

        
        nome = self.campoNome.get()
        cpf = self.campoCPF.get()
        telefone = self.campoTelefone.get()
        email = self.campoEmail.get()

        if not nome or not cpf or not telefone or not email:
            self.rotuloResultado.configure(text="Digite as informações", text_color="red")

        else:
            cliente = Cliente(None, nome,cpf,telefone, email)
            conexao.manipularBanco(cliente.inserirCliente())

            aux = conexao.consultarBanco('''
            Select * From "Cliente"
            Order BY "Nome" ASC ''')

            for novo in aux: 
                if novo[2] == cpf: 
                    self.rotuloResultado.configure(text="Cliente inserido com sucesso", text_color="green")
                else:
                    self.rotuloResultado.configure(text="Houve um erro ao inserir o cliente", text_color="red")
    



    def abrirTela(self,nomeDaTela):

        if nomeDaTela == "Tela Inicial":
            self.telaInicial.grid(column=1,row=0, sticky="ew")
        else:
            self.telaInicial.grid_forget()

        if nomeDaTela == "Inserir Cliente":
            self.telaInserirCliente.grid(column=1,row=0, sticky="nsew")
        else:
            self.telaInserirCliente.grid_forget()
        
        if nomeDaTela == "Visualizar Clientes":
            self.telaVisualizarClientes.grid(column=1,row=0, sticky="nsew")
        
            Clientes = conexao.consultarBanco('''
            Select * From "Cliente"
            Order BY "Nome" ASC ''')
           
            dados = []
            for Cliente in Clientes:
                dados.append([Cliente[0], Cliente[1], Cliente[2], Cliente[3], Cliente[4]])

            headers = ["ID", "Nome", "CPF", "Telefone", "Email"]
            textoExibicao = tabulate(dados, headers=headers, tablefmt="pipe")

            self.listaDeClientes.insert("end", textoExibicao)
          
        else:
            self.telaVisualizarClientes.grid_forget()
            self.listaDeClientes.delete("0.0","end")

        if nomeDaTela == "Remover Clientes":
            self.telaRemoverClientes.grid(column = 1, row = 0, sticky = "nsew")
        else:
            self.telaRemoverClientes.grid_forget()

        if nomeDaTela == "Atualizar dados":
            self.novatelaAtualizarDados.grid(column=1,row=0, sticky="nsew")
        else:
            self.novatelaAtualizarDados.grid_forget()


        
    def voltar_menu_principal(self):
        self.destroy()
        self.menu_principal = App()
        self.menu_principal.iniciar()

    def iniciar(self):
        self.mainloop()
    







set_appearance_mode("dark") 


class MenuImoveis(Tk):
    def __init__(self):
        super().__init__()
        

        self.title("Sistema de Gerenciamento")
        self.geometry("600x400")
        self.resizable(False,False)

        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=4)


        #Menu de navegação
        self.menuNavegacao = CTkFrame(self, fg_color="light cyan")
        self.menuNavegacao.grid(column=0, row=0, sticky="nsew")

        self.menuNavegacao.columnconfigure(0, weight=1)

        self.label = CTkLabel(master = self.menuNavegacao,font= CTkFont(size=16, weight = "bold"), text = "Menu Imóveis",text_color = "black", compound= "top")
        self.label.grid(column=0,row=0, padx= 20, pady= 25)
        self.botaoAtualizarDados = CTkButton(self.menuNavegacao, text="Atualizar dados", command=partial(self.abrirTela,"Atualizar dados"))
        self.botaoAtualizarDados.grid(column=0,row=3, padx= 20, sticky="ew", pady = 15)

        self.botaoInserirImovel = CTkButton(self.menuNavegacao, text="Inserir Imovel", command=partial(self.abrirTela,"Inserir Imovel"))
        self.botaoInserirImovel.grid(column=0, row=1, padx= 20, sticky="ew", pady = 15)

        self.botaoVisualizarImovels = CTkButton(self.menuNavegacao, text="Visualizar Imoveis", command=partial(self.abrirTela,"Visualizar Imovels"))
        self.botaoVisualizarImovels.grid(column=0, row=2, padx= 20, sticky="ew", pady = 15)

        self.botaoRemoverImovels = CTkButton(self.menuNavegacao, text="Remover Imoveis", command=partial(self.abrirTela,"Remover Imovels"))
        self.botaoRemoverImovels.grid(column=0, row=4, padx= 20, sticky="ew", pady = 15)

        self.botaoImovel = CTkButton(self.menuNavegacao, text="Voltar a Tela Inicial",command=self.voltar_menu_principal1)
        self.botaoImovel.grid(column=0,row=5, padx= 20, sticky="ew", pady = 15)


        #Tela Inicial
        self.telaInicial = CTkFrame(self, fg_color="gray")
        self.telaInicial.grid(column=1, row=0, sticky="nsew")

       
        self.mensagemBoasVindas = CTkLabel(self.telaInicial, text="Bem vindo ao Sistema de Gerenciamento de Imóveis",text_color="black",font=CTkFont(size=32, weight="bold"),wraplength=300)
        self.mensagemBoasVindas.grid(column=1, row=0, pady = 120, padx = 80)

        #Tela Inserir Imovel

        self.telaInserirImovel = CTkFrame(self, fg_color="transparent")
        self.telaInserirImovel.grid_columnconfigure(0,weight=1)

        self.tituloInserirImovel = CTkLabel(self.telaInserirImovel, text= "Inserir Imovel", font=CTkFont(size=20, weight= "bold"), text_color = "black")
        self.tituloInserirImovel.grid(column=0, row=0,sticky="ew",pady = 15)

        self.rotuloEndereco = CTkLabel(self.telaInserirImovel, text= "Rua: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloEndereco.grid(column=0, row=1, padx= 15, pady =15,) 
 
        self.campoEndereco = CTkEntry(self.telaInserirImovel, placeholder_text=("Digite o endereco do Imovel"))
        self.campoEndereco.grid(column=1, row=1, padx= 30, pady = 15,sticky="ew")

        self.rotuloNumero = CTkLabel(self.telaInserirImovel, text= "Numero: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloNumero.grid(column=0, row=2, padx= 15, pady = 15) 

        self.campoNumero = CTkEntry(self.telaInserirImovel, placeholder_text=("Digite o Numero do Imovel"))
        self.campoNumero.grid(column=1, row=2, padx= 30, pady = 15)

        self.campoBairro = CTkEntry(self.telaInserirImovel, placeholder_text=("Digite o Bairro do Imovel"))
        self.campoBairro.grid(column=1, row=3, padx= 30, pady = 15)

        self.rotuloBairro = CTkLabel(self.telaInserirImovel, text= "Bairro: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloBairro.grid(column=0, row=3, padx= 15, pady = 15) 

        self.campoCidade = CTkEntry(self.telaInserirImovel, placeholder_text=("Digite o Cidade do Imovel"))
        self.campoCidade.grid(column=1, row=4, padx= 30, pady = 15, sticky = "ew")

        self.rotuloCidade = CTkLabel(self.telaInserirImovel, text= "Cidade: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloCidade.grid(column=0, row=4, padx= 15, pady = 15) 

        self.botaoInserirImovel = CTkButton(self.telaInserirImovel, text="Enviar", command=self.inserirImovelBanco)
        self.botaoInserirImovel.grid(column=1, row=5,pady = 15)

        self.rotuloResultado = CTkLabel(master= self.telaInserirImovel)
        self.rotuloResultado.grid(column=1, row=6)


        # Visualizar Imovels

        self.telaVisualizarImovels = CTkFrame(self, fg_color="transparent")
        self.telaVisualizarImovels.grid_columnconfigure(0,weight=1)
        self.telaVisualizarImovels.grid_rowconfigure(1,weight=1)

        self.tituloVisualizarImovels = CTkLabel(self.telaVisualizarImovels, text= "Lista de Imoveis",text_color = "black" ,font=CTkFont(size=24))
        self.tituloVisualizarImovels.grid(column=0, row=0)

        self.listaDeImovels = CTkTextbox(self.telaVisualizarImovels, fg_color="transparent", text_color="black")
        self.listaDeImovels.grid(column=0, row =1, sticky="nsew")

       # Remover Imovels
    
        self.telaRemoverImovels = CTkFrame(self, fg_color="transparent")
        self.telaRemoverImovels.grid_columnconfigure(0,weight=1)
        self.telaRemoverImovels.grid_rowconfigure(1,weight= 1)

        self.tituloRemoverImovels = CTkLabel(self.telaRemoverImovels, text= "Remover Imovel",text_color = "black" ,font=CTkFont(size=16), compound = "center")
        self.tituloRemoverImovels.grid(row=0, sticky = "ew")

        self.campoRemover = CTkEntry(self.telaRemoverImovels, placeholder_text=("Digite o id do Imovel para remoção"))
        self.campoRemover.grid(column=1, row=1, padx= 75, pady = 10, sticky = "ew")

        self.rotuloRemover = CTkLabel(self.telaRemoverImovels, text= "Id_Imovel: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloRemover.grid(column=0, row=1, padx= 7, pady = 10) 

        self.botaoRemoverImovel = CTkButton(self.telaRemoverImovels, text="Enviar", command=self.removerImovelBanco)
        self.botaoRemoverImovel.grid(column=1, row=2,pady = 15)

        self.rotuloConfirmarRemover = CTkLabel(master= self.telaRemoverImovels)
        self.rotuloConfirmarRemover.grid(column=1, row=3, pady =15)


        # Atualizar Dados Cadastrais 

        self.novatelaAtualizarDados = CTkFrame(self, fg_color="transparent")
        self.novatelaAtualizarDados.grid_columnconfigure(0,weight=1)
        self.novatelaAtualizarDados.grid_rowconfigure(1,weight= 1)


        self.novorotuloEndereco = CTkLabel(self.novatelaAtualizarDados, text= "Rua: ",text_color = "black", font=CTkFont(size= 16))
        self.novorotuloEndereco.grid(column=0, row=3, padx= 15, pady =15,) 
 
        self.novocampoEndereco = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o rua do Imovel"))
        self.novocampoEndereco.grid(column=1, row=3, padx= 30, pady = 15,sticky="ew")

        self.novorotuloNumero = CTkLabel(self.novatelaAtualizarDados, text= "Numero: ",text_color = "black", font=CTkFont(size= 16))
        self.novorotuloNumero.grid(column=0, row=4, padx= 15, pady = 15) 

        self.novocampoNumero = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o numero do Imovel"))
        self.novocampoNumero.grid(column=1, row=4, padx= 30, pady = 15,sticky = "ew")

        self.novocampoBairro = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o bairro do Imovel"))
        self.novocampoBairro.grid(column=1, row=5, padx= 30, pady = 15,sticky = "ew")

        self.novorotuloBairro = CTkLabel(self.novatelaAtualizarDados, text= "Bairro: ",text_color = "black", font=CTkFont(size= 16))
        self.novorotuloBairro.grid(column=0, row=5, padx= 15, pady = 15) 

        self.novocampoCidade = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o cidade do Imovel"))
        self.novocampoCidade.grid(column=1, row=6, padx= 30, pady = 15, sticky = "ew")

        self.novorotuloCidade = CTkLabel(self.novatelaAtualizarDados, text= "Cidade: ",text_color = "black", font=CTkFont(size= 16))
        self.novorotuloCidade.grid(column=0, row=6, padx= 15, pady = 15) 

        self.novotituloAtualizarDados = CTkLabel(self.novatelaAtualizarDados, text= "Atualizar Cadastro",text_color = "black" ,font=CTkFont(size=16), compound = "center")
        self.novotituloAtualizarDados.grid(row=0, sticky = "ew")

        self.campoAtualizar = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("ID que será atualizado"))
        self.campoAtualizar.grid(column=1, row=1, padx= 30, pady = 10, sticky = "ew")

        self.rotuloAtualizar = CTkLabel(self.novatelaAtualizarDados, text= "Id_Imovel: ",text_color = "black", font=CTkFont(size= 16))
        self.rotuloAtualizar.grid(column=0, row=1, padx= 7, pady = 10) 

        self.botaoAtualizarImovel = CTkButton(self.novatelaAtualizarDados, text="Enviar", command=self.atualizarImovelBanco)
        self.botaoAtualizarImovel.grid(column=0, row=7,pady = 15)

        self.rotuloConfirmarAtualizar = CTkLabel(master= self.novatelaAtualizarDados)
        self.rotuloConfirmarAtualizar.grid(column=1, row=7, pady =15)


  

    def atualizarImovelBanco(self):

        escolha = self.campoAtualizar.get()

        endereco = self.novocampoEndereco.get()
        numero = self.novocampoNumero.get()
        bairro = self.novocampoBairro.get()
        cidade = self.novocampoCidade.get()
        
        aux = conexao.consultarBanco(f'''
            Select * From "Imovel"
            where "Id_Imovel" = '{escolha}'
            ''')

        
        if not escolha:
            self.rotuloConfirmarAtualizar.configure(text="Digite o id do Imovel", text_color="red")

        
        elif not  aux:
            self.rotuloConfirmarAtualizar.configure(text="Imovel não encontrado", text_color="red")


        else:
            conexao.manipularBanco(f'''
            UPDATE "Imovel"
            SET
              "Endereco" = '{endereco}',
              "Numero" = '{numero}',
              "Bairro" = '{bairro}',
              "Cidade" = '{cidade}'
            WHERE
              "Id_Imovel" = '{escolha}'
            ''')


            if escolha not in aux:
                self.rotuloConfirmarAtualizar.configure(text = "Dados atualizados", text_color = "green")
            elif escolha in aux:
                self.rotuloConfirmarAtualizar.configure(text = "Dados não atualizados", text_color = "red")



    def removerImovelBanco(self):
        
        escolha = self.campoRemover.get()

        aux = conexao.consultarBanco(f'''
            Select * From "Imovel"
            where "Id_Imovel" = '{escolha}'
            ''')
        
        if not escolha:
            self.rotuloConfirmarRemover.configure(text="Digite o id do Imovel", text_color="red")

        
        elif not aux:
            self.rotuloConfirmarRemover.configure(text="Imovel não encontrado", text_color="red")
    

        else:
            conexao.manipularBanco(f'''
            DELETE FROM "Imovel"
            WHERE "Id_Imovel" = '{escolha}'
            ''')


            if escolha not in aux:
                self.rotuloConfirmarRemover.configure(text = "Imovel Removido", text_color = "green")
            elif escolha in aux:
                self.rotuloConfirmarRemover.configure(text = "Imovel não removido", text_color = "red")
 

        
    def inserirImovelBanco(self):

        
        endereco = self.campoEndereco.get()
        numero = self.campoNumero.get()
        bairro = self.campoBairro.get()
        cidade = self.campoCidade.get()

        if not endereco or not numero or not bairro or not cidade:
            self.rotuloResultado.configure(text="Digite as informações", text_color="red")

        else:
            imovel = Imovel(None, endereco,numero,bairro, cidade)
            conexao.manipularBanco(imovel.inserirImovel())

            aux = conexao.consultarBanco('''
            Select * From "Imovel"
            Order BY "Id_Imovel" ASC ''')

            for novo in aux: 
                if novo[1] == endereco and novo[2] == numero: 
                    self.rotuloResultado.configure(text="Imovel inserido com sucesso", text_color="green")
                else:
                    self.rotuloResultado.configure(text="Houve um erro ao inserir o Imovel", text_color="red")
    



    def abrirTela(self,nomeDaTela):

        if nomeDaTela == "Tela Inicial":
            self.telaInicial.grid(column=1,row=0, sticky="ew")
        else:
            self.telaInicial.grid_forget()

        if nomeDaTela == "Inserir Imovel":
            self.telaInserirImovel.grid(column=1,row=0, sticky="nsew")
        else:
            self.telaInserirImovel.grid_forget()
        
        if nomeDaTela == "Visualizar Imovels":
            self.telaVisualizarImovels.grid(column=1,row=0, sticky="nsew")
        
            Imovels = conexao.consultarBanco('''
            Select * From "Imovel"
            Order BY "Id_Imovel" ASC ''')
        
            textoExibicao = " ID  | Endereco                    | Numero        |  Bairro    | Cidade  \n"
            for Imovel in Imovels:
                textoExibicao += f" {Imovel[0]}  | {Imovel[1]} | {Imovel[2]}  | {Imovel[3]}        | {Imovel[4]} \n"
            self.listaDeImovels.insert("end", textoExibicao)
        else:
            self.telaVisualizarImovels.grid_forget()
            self.listaDeImovels.delete("0.0","end")

        if nomeDaTela == "Remover Imovels":
            self.telaRemoverImovels.grid(column = 1, row = 0, sticky = "nsew")
        else:
            self.telaRemoverImovels.grid_forget()

        if nomeDaTela == "Atualizar dados":
            self.novatelaAtualizarDados.grid(column=1,row=0, sticky="nsew")
        else:
            self.novatelaAtualizarDados.grid_forget()


        
    def voltar_menu_principal1(self):
        self.destroy()
        self.menu_principal = App()
        self.menu_principal.iniciar()

    def iniciar(self):
        self.mainloop()








set_appearance_mode("dark") 


class MenuCompra(Tk):
    def __init__(self):
        super().__init__()
        

        self.title("Sistema de Gerenciamento")
        self.geometry("700x500")
        self.resizable(False,False)

        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=4)


        #Menu de navegação
        self.menuNavegacao = CTkFrame(self, fg_color="light cyan")
        self.menuNavegacao.grid(column=0, row=0, sticky="nsew")

        self.menuNavegacao.columnconfigure(0, weight=1)

        self.label = CTkLabel(master = self.menuNavegacao,font= CTkFont(size=16, weight = "bold"), text = "Menu Comercial",text_color = "black", compound= "top")
        self.label.grid(column=0,row=0, padx= 20, pady= 25)
        self.botaoAtualizarDados = CTkButton(self.menuNavegacao, text="Atualizar dados", command=partial(self.abrirTela,"Atualizar dados"))
        self.botaoAtualizarDados.grid(column=0,row=3, padx= 20, sticky="ew", pady = 15)

        self.botaoInserirCompra = CTkButton(self.menuNavegacao, text="Inserir Compra", command=partial(self.abrirTela,"Inserir Compra"))
        self.botaoInserirCompra.grid(column=0, row=1, padx= 20, sticky="ew", pady = 15)

        self.botaoVisualizarCompras = CTkButton(self.menuNavegacao, text="Visualizar Compras", command=partial(self.abrirTela,"Visualizar Compras"))
        self.botaoVisualizarCompras.grid(column=0, row=2, padx= 20, sticky="ew", pady = 15)

        self.botaoRemoverCompras = CTkButton(self.menuNavegacao, text="Remover Compras", command=partial(self.abrirTela,"Remover Compras"))
        self.botaoRemoverCompras.grid(column=0, row=4, padx= 20, sticky="ew", pady = 15)

        self.botaoImovel = CTkButton(self.menuNavegacao, text="Voltar a Tela Inicial",command=self.voltar_menu_principal2)
        self.botaoImovel.grid(column=0,row=5, padx= 20, sticky="ew", pady = 15)


        #Tela Inicial
        self.telaInicial = CTkFrame(self, fg_color="gray")
        self.telaInicial.grid(column=1, row=0, sticky="nsew")

       
        self.mensagemBoasVindas = CTkLabel(self.telaInicial, text="Bem vindo ao Sistema de Gerenciamento de Compras",text_color="black",font=CTkFont(size=32, weight="bold"),wraplength=300)
        self.mensagemBoasVindas.grid(column=1, row=0, pady = 120, padx = 120)

        #Tela Inserir Compra

        self.telaInserirCompra = CTkFrame(self, fg_color="transparent")
        self.telaInserirCompra.grid_columnconfigure(0,weight=1)

        self.tituloInserirCompra = CTkLabel(self.telaInserirCompra, text= "Inserir Compra", font=CTkFont(size=20, weight= "bold"), text_color = "black")
        self.tituloInserirCompra.grid(column=0, row=0,sticky="ew",pady = 15)

        self.rotuloCliente = CTkLabel(self.telaInserirCompra, text= "Id_Comprador: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloCliente.grid(column=0, row=1, padx= 15, pady =15,) 
 
        self.campoCliente = CTkEntry(self.telaInserirCompra, placeholder_text=("Digite o id do cliente"))
        self.campoCliente.grid(column=1, row=1, padx= 30, pady = 15,sticky="ew")

        self.rotuloImovel = CTkLabel(self.telaInserirCompra, text= "Id_Imovel: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloImovel.grid(column=0, row=2, padx= 15, pady = 15) 

        self.campoImovel = CTkEntry(self.telaInserirCompra, placeholder_text=("Digite o id do Imovel"))
        self.campoImovel.grid(column=1, row=2, padx= 30, pady = 15)

        self.campoPreco = CTkEntry(self.telaInserirCompra, placeholder_text=("Digite o Preco do Imovel"))
        self.campoPreco.grid(column=1, row=3, padx= 30, pady = 15)

        self.rotuloPreco = CTkLabel(self.telaInserirCompra, text= "Preco_Imovel: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloPreco.grid(column=0, row=3, padx= 15, pady = 15) 


        self.botaoInserirCompra = CTkButton(self.telaInserirCompra, text="Enviar", command=self.inserirCompraBanco)
        self.botaoInserirCompra.grid(column=1, row=5,pady = 15)

        self.rotuloResultado = CTkLabel(master= self.telaInserirCompra)
        self.rotuloResultado.grid(column=1, row=6)


        # Visualizar Compras

        self.telaVisualizarCompras = CTkFrame(self, fg_color="transparent")
        self.telaVisualizarCompras.grid_columnconfigure(0,weight=1)
        self.telaVisualizarCompras.grid_rowconfigure(1,weight=1)

        self.tituloVisualizarCompras = CTkLabel(self.telaVisualizarCompras, text= "Lista de Compras",text_color = "black" ,font=CTkFont(size=24))
        self.tituloVisualizarCompras.grid(column=0, row=0)

        self.listaDeCompras = CTkTextbox(self.telaVisualizarCompras, fg_color="transparent", text_color="black")
        self.listaDeCompras.grid(column=0, row =1, sticky="nsew")

       # Remover Compra
    
        self.telaRemoverCompras = CTkFrame(self, fg_color="transparent")
        self.telaRemoverCompras.grid_columnconfigure(0,weight=1)
        self.telaRemoverCompras.grid_rowconfigure(1,weight= 1)

        self.tituloRemoverCompras = CTkLabel(self.telaRemoverCompras, text= "Remover Compra",text_color = "black" ,font=CTkFont(size=16), compound = "center")
        self.tituloRemoverCompras.grid(row=0, sticky = "ew")

        self.campoRemover = CTkEntry(self.telaRemoverCompras, placeholder_text=("Digite o id da compra para remoção"))
        self.campoRemover.grid(column=1, row=1, padx= 75, pady = 10, sticky = "ew")

        self.rotuloRemover = CTkLabel(self.telaRemoverCompras, text= "Id_Compra: ",text_color = "black", font=CTkFont(size= 20))
        self.rotuloRemover.grid(column=0, row=1, padx= 7, pady = 10) 

        self.botaoRemoverCompra = CTkButton(self.telaRemoverCompras, text="Enviar", command=self.removerCompraBanco)
        self.botaoRemoverCompra.grid(column=1, row=2,pady = 15)

        self.rotuloConfirmarRemover = CTkLabel(master= self.telaRemoverCompras)
        self.rotuloConfirmarRemover.grid(column=1, row=3, pady =15)


        # Atualizar Dados Cadastrais 

        self.novatelaAtualizarDados = CTkFrame(self, fg_color="transparent")
        self.novatelaAtualizarDados.grid_columnconfigure(0,weight=1)
        self.novatelaAtualizarDados.grid_rowconfigure(1,weight= 1)


        self.novotituloAtualizarDados = CTkLabel(self.novatelaAtualizarDados, text= "Atualizar Cadastro",text_color = "black" ,font=CTkFont(size=16), compound = "center")
        self.novotituloAtualizarDados.grid(row=0, sticky = "ew")

        self.campoAtualizar = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("ID que será atualizado"))
        self.campoAtualizar.grid(column=1, row=1, padx= 30, pady = 10, sticky = "ew")

        self.rotuloAtualizar = CTkLabel(self.novatelaAtualizarDados, text= "Id_Compra: ",text_color = "black", font=CTkFont(size= 16))
        self.rotuloAtualizar.grid(column=0, row=1, padx= 7, pady = 10) 

        self.novorotuloCliente = CTkLabel(self.novatelaAtualizarDados, text= "Novo_Id_Comprador: ",text_color = "black", font=CTkFont(size= 20))
        self.novorotuloCliente.grid(column=0, row=2, padx= 15, pady =15,) 
 
        self.novocampoCliente = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o id do cliente"))
        self.novocampoCliente.grid(column=1, row=2, padx= 30, pady = 15,sticky="ew")

        self.novorotuloImovel = CTkLabel(self.novatelaAtualizarDados, text= "Novo_Id_Imovel: ",text_color = "black", font=CTkFont(size= 20))
        self.novorotuloImovel.grid(column=0, row=3, padx= 15, pady = 15) 

        self.novocampoImovel = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o id do Imovel"))
        self.novocampoImovel.grid(column=1, row=3, padx= 30, pady = 15)

        self.novocampoPreco = CTkEntry(self.novatelaAtualizarDados, placeholder_text=("Digite o Preco do Imovel"))
        self.novocampoPreco.grid(column=1, row=4, padx= 30, pady = 15)

        self.novorotuloPreco = CTkLabel(self.novatelaAtualizarDados, text= "Preco_Imovel: ",text_color = "black", font=CTkFont(size= 20))
        self.novorotuloPreco.grid(column=0, row=4, padx= 15, pady = 15) 


        self.botaoAtualizarCliente = CTkButton(self.novatelaAtualizarDados, text="Enviar", command=self.atualizarCompraBanco)
        self.botaoAtualizarCliente.grid(column=0, row=5,pady = 15)

        self.rotuloConfirmarAtualizar = CTkLabel(master= self.novatelaAtualizarDados)
        self.rotuloConfirmarAtualizar.grid(column=1, row=5, pady =15)


  

    def atualizarCompraBanco(self):

        escolha = self.campoAtualizar.get()

        cliente = self.novocampoCliente.get()
        imovel = self.novocampoImovel.get()
        preco = self.novocampoPreco.get()
        
        
        aux = conexao.consultarBanco(f'''
            Select * From "Compra"
            where "Id_Compra" = '{escolha}'
            ''')

        
        if not escolha:
            self.rotuloConfirmarAtualizar.configure(text="Digite o id para atualizar", text_color="red")

        
        elif not  aux:
            self.rotuloConfirmarAtualizar.configure(text="Compra não encontrada", text_color="red")


        else:
            conexao.manipularBanco(f'''
            UPDATE "Compra"
            SET
              "ID_Cliente" = '{cliente}',
              "Id_Imovel" = '{imovel}',
              "Preço_Imovel" = '{preco}'
            WHERE
              "Id_Compra" = '{escolha}'
            ''')


            if escolha not in aux:
                self.rotuloConfirmarAtualizar.configure(text = "Dados atualizados", text_color = "green")
            elif escolha in aux:
                self.rotuloConfirmarAtualizar.configure(text = "Dados não atualizados", text_color = "red")



    def removerCompraBanco(self):
        
        escolha = self.campoRemover.get()

        aux = conexao.consultarBanco(f'''
            Select * From "Compra"
            where "Id_Compra" = '{escolha}'
            ''')
        
        if not escolha:
            self.rotuloConfirmarRemover.configure(text="Digite o id para ser removido", text_color="red")

        
        elif not aux:
            self.rotuloConfirmarRemover.configure(text="Cliente não encontrado", text_color="red")
    

        else:
            conexao.manipularBanco(f'''
            DELETE FROM "Compra"
            WHERE "Id_Compra" = '{escolha}'
            ''')


            if escolha not in aux:
                self.rotuloConfirmarRemover.configure(text = "Compra Removida", text_color = "green")
            elif escolha in aux:
                self.rotuloConfirmarRemover.configure(text = "Compra não removido", text_color = "red")
 

        
    def inserirCompraBanco(self):

        
        cliente = self.campoCliente.get()
        imovel = self.campoImovel.get()
        preco = self.campoPreco.get()
        

        if not cliente or not imovel or not preco:
            self.rotuloResultado.configure(text="Digite as informações", text_color="red")

        else:

            compra = Comercial(None, cliente,imovel,None, preco)
            conexao.manipularBanco(compra.inserirCompra())

            aux = conexao.consultarBanco('''
            Select * From "Compra"
            Order BY "Id_Compra" ASC ''')

            for novo in aux: 
                if novo[1] not in aux and novo[2] not in aux: 
                    self.rotuloResultado.configure(text="Compra inserida com sucesso", text_color="green")
                else:
                    self.rotuloResultado.configure(text="Houve um erro ao inserir o compra", text_color="red")
    



    def abrirTela(self,nomeDaTela):

        if nomeDaTela == "Tela Inicial":
            self.telaInicial.grid(column=1,row=0, sticky="ew")
        else:
            self.telaInicial.grid_forget()

        if nomeDaTela == "Inserir Compra":
            self.telaInserirCompra.grid(column=1,row=0, sticky="nsew")
        else:
            self.telaInserirCompra.grid_forget()
        
        if nomeDaTela == "Visualizar Compras":
            self.telaVisualizarCompras.grid(column=1,row=0, sticky="nsew")

            listaCompras = conexao.consultarBanco('''
            Select * From "Compra"
            Order BY "Id_Compra" ASC ''')
        
            textoExibicao = " ID   |  Nome do Cliente          | Imovel            |   Data da Compra       |  Preco do Imovel   \n"
        
            for Compra in listaCompras:

                clienteCompra = conexao.consultarBanco(f'''
                SELECT*FROM "Cliente"
                WHERE "Id" = '{Compra[1]}'
                ''')[0]

                imovelCompra = conexao.consultarBanco(f'''
                SELECT*FROM "Imovel"
                WHERE "Id_Imovel" = '{Compra[2]}'
                ''')[0]

                textoExibicao += f" {Compra[0]}  | {clienteCompra[1]} | Rua {imovelCompra[1]} - Nº {imovelCompra[2]} | {Compra[3]}        | R$  {Compra[4]} \n"
            self.listaDeCompras.insert("end", textoExibicao)
        else:
            self.telaVisualizarCompras.grid_forget()
            self.listaDeCompras.delete("0.0","end")

        if nomeDaTela == "Remover Compras":
            self.telaRemoverCompras.grid(column = 1, row = 0, sticky = "nsew")
        else:
            self.telaRemoverCompras.grid_forget()

        if nomeDaTela == "Atualizar dados":
            self.novatelaAtualizarDados.grid(column=1,row=0, sticky="nsew")
        else:
            self.novatelaAtualizarDados.grid_forget()


        
    def voltar_menu_principal2(self):
        self.destroy()
        self.menu_principal = App()
        self.menu_principal.iniciar()

    def iniciar(self):
        self.mainloop()





app = App()
app.iniciar()

