import customtkinter as ctk
from tkinter import *
import DataBase
from tkinter import messagebox
import BACKENDoficial
import subprocess




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.tela_de_login()

        # icon do app
        # photo = PhotoImage(file='robo.png')
        # self.iconphoto(False, photo)

       # Configurando a janela principal
    def configuracoes_da_janela_inicial(self):
        self.geometry("750x400")
        self.title("Sistema de Login")
        self.resizable(False, False)

    def tela_de_login(self):
        # Trabalhando com as imagens
        self.img = PhotoImage(
            file="C:\\Users\\User\\PycharmProjects\\Pedro_python\\Python\\task_optimization\\telaLogin\\login.png")
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10)

        # Titulo da plataforma
        self.title = ctk.CTkLabel(
            self, text="Faça o seu login ou Cadastre-se\n em nossa plataforma para acessar\n nossos serviços!", font=("Century Gothic bold", 14))
        self.title.grid(row=0, column=0, padx=10, pady=10)

        # Criar a frame do formulario de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=390, y=10)

        # Colocando widgets dentro do frame - formulario de login
        self.lb_title = ctk.CTkLabel(
            self.frame_login, text="Faça o seu login", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        # Criando o loginusername
        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Nome de usuario...", font=(
            "Century Gothic bold", 16), corner_radius=15, border_color="#FF6400")
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=10)

        # Criando o password
        self.password_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Senha de usuario...", font=(
            "Century Gothic bold", 16), corner_radius=15, show="*", border_color="#FF6400")
        self.password_login_entry.grid(row=2, column=0, padx=10, pady=10)

        # Criando o VER password
        self.confirma_password_login = ctk.CTkCheckBox(self.frame_login, text="Clique para ver a senha", font=(
            "Century Gothic bold", 14), corner_radius=20, border_color="#FF6400")
        self.confirma_password_login.grid(row=3, column=0, padx=10, pady=10)

        # Criando o botão de login
        self.button_login = ctk.CTkButton(self.frame_login, width=300, fg_color="#e35b04", hover_color="#ff9100", text="Login".upper(), font=("Century Gothic bold", 16), corner_radius=15, border_color="#FF6400")  # command=self.sistema_entry
        self.button_login.grid(row=4, column=0, padx=10, pady=10)
        


        # Criando o testo para login
        self.span = ctk.CTkLabel(
            self.frame_login, text="Se não tem conta clique no botão abaixo\n para se inscrever em nosso sistema",  font=("Century Gothic", 10))
        self.span.grid(row=5, column=0, padx=10, pady=10)

        # Criando o botão de cadastro
        self.button_cadastro = ctk.CTkButton(self.frame_login, width=300, fg_color="#e35b04", hover_color="#ff9100", text="Fazer cadastro".upper(), font=("Century Gothic bold", 16), corner_radius=15, command=self.tela_de_cadastro)
        self.button_cadastro.grid(row=6, column=0, padx=10, pady=10)

    def tela_de_cadastro(self):
        # Removendo tela de login
        self.frame_login.place_forget()

        # Frame do formulario de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=390, y=10)

        # Colocando titulo
        self.lb_title = ctk.CTkLabel(
            self.frame_cadastro, text="Faça o seu login", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        # Criando o widget para tela de cadastro
        self.username_cadastro = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Nome de usuario...", font=(
            "Century Gothic bold", 16), corner_radius=15, border_color="#FF6400")
        self.username_cadastro.grid(row=1, column=0, padx=10, pady=6)

        self.email_cadastro = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="E-mail de usuario...", font=(
            "Century Gothic bold", 16), corner_radius=15, border_color="#FF6400")
        self.email_cadastro.grid(row=2, column=0, padx=10, pady=6)

        self.password_cadastro = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha de usuario...", font=(
            "Century Gothic bold", 16), corner_radius=15, show="*", border_color="#FF6400")
        self.password_cadastro.grid(row=3, column=0, padx=10, pady=6)

        self.confirma_password = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirmar senha de usuario...", font=(
            "Century Gothic bold", 16), corner_radius=15, show="*", border_color="#FF6400")
        self.confirma_password.grid(row=4, column=0, padx=10, pady=6)

        # Criando o VER password
        self.view_password_cadastro = ctk.CTkCheckBox(self.frame_cadastro, text="Clique para ver a senha", font=(
            "Century Gothic bold", 14), corner_radius=20, border_color="#FF6400")
        self.view_password_cadastro.grid(row=5, column=0, padx=10, pady=6)


        #################
        # BANCO DE DADOS
        #################
    def RegisterToDataBase(self):
            #Name = self.username_cadastro.get()
            Email = self.email_cadastro.get()
            User = self.username_cadastro.get()
            Pass = self.password_cadastro.get()
            DataBase.cursor.execute("""
                INSERT INTO User (User, Email, Password) VALUES(?,?,?)
            """,(User, Email, Pass))
            DataBase.connection.commit()
            messagebox.showinfo(title="Register Info", message="Conta criada com sucesso...")
        #################

        # Criando o botão de cadastro
            self.button_cadastro_user = ctk.CTkButton(self.frame_cadastro, width=300, fg_color="#e35b04", hover_color="#ff9100", text="Registrar".upper(), font=("Century Gothic bold", 16), corner_radius=15, command=self.RegisterToDataBase)
            self.button_cadastro_user.grid(row=6, column=0, padx=10, pady=6)

            # Criando o botão de login
            self.button_login_back = ctk.CTkButton(self.frame_cadastro, width=300, text="Voltar ao Login".upper(), font=(
                "Century Gothic bold", 16), corner_radius=15, fg_color="#e35b04", hover_color="#ff9100", border_color="#FF6400", command=self.tela_de_login)
            self.button_login_back.grid(row=7, column=0, padx=10, pady=6)


        ######################################################################################
        # estudar mais esse delete (ver se tem como colocar um widget maior pra fora da tela)#
        ######################################################################################
    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.password_cadastro_entry.delete(0, END)
        self.confirma_password_entry.delete(0, END)
        
    def limpa_entry_login(self):
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)
        ######################################################################################
    def sistema_entry(self):
        # Removendo tela de login
        self.frame_login.place_forget()

        # Frame do formulario de cadastro
        self.frame_sistema = ctk.CTkFrame(self, width=350, height=380)
        self.frame_sistema.place(x=390, y=10)

        # Titulo da plataforma
        self.lb_title = ctk.CTkLabel(
            self.frame_sistema, text="Insira as panavras chaves\npara a substituição", font=("Century Gothic bold", 22))
        self.lb_title.grid(row=0, column=1, padx=10, pady=10)

        self.campo1_sistema_entry = ctk.CTkEntry(self.frame_sistema, width=100, placeholder_text="Nome de usuario...", font=(
            "Century Gothic bold", 16), corner_radius=15, border_color="#FF6400")
        self.campo1_sistema_entry.grid(row=3, column=1, padx=10, pady=6)

        self.campo2_sistema_entry = ctk.CTkEntry(self.frame_sistema, width=100, placeholder_text="Nome de usuario...", font=(
            "Century Gothic bold", 16), corner_radius=15, border_color="#FF6400")
        self.campo2_sistema_entry.grid(row=4, column=1, padx=10, pady=6)

        # Criando o botão de login
        self.button_sistema = ctk.CTkButton(self.frame_sistema, width=200, text="Substituir".upper(), font=(
            "Century Gothic bold", 16), corner_radius=15, fg_color="#e35b04", hover_color="#ff9100", border_color="#FF6400", command=self.tela_de_login)
        self.button_sistema.grid(row=7, column=1, padx=10, pady=6)

        # Criando o botão de login
        self.button_sistema = ctk.CTkButton(self.frame_sistema, width=200, text="Adicionar".upper(), font=(
            "Century Gothic bold", 16), corner_radius=15, fg_color="#e35b04", hover_color="#ff9100", border_color="#FF6400", command=self.tela_de_login)
        self.button_sistema.grid(row=8, column=1, padx=10, pady=6)

if __name__ =="__main__":
    app = App()
    app.mainloop()
    subprocess.run(["BACKENDoficial.py"])