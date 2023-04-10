import tkinter as tk

# Cria a janela
janela = tk.Tk()

# Adiciona um título à janela
janela.title("Tela de Entrada")

# Define o tamanho da janela
janela.geometry("400x200")

# Função para substituir o conteúdo do primeiro campo pelo conteúdo do segundo campo
def substituir():
    texto = campo2.get()
    campo1.delete(0, tk.END)
    campo1.insert(0, texto)

# Função para adicionar novos campos de entrada
def adicionar_campos():
    # Cria um novo campo de entrada
    novo_campo1 = tk.Entry(janela, width=30)
    novo_campo1.pack(pady=5)

    # Cria outro novo campo de entrada
    novo_campo2 = tk.Entry(janela, width=30)
    novo_campo2.pack(padx=5)

    """ # Adiciona um botão "Substituir" para substituir o conteúdo do novo campo 1 pelo conteúdo do novo campo 2
    novo_botao_substituir = tk.Button(janela, text="Substituir", command=lambda: novo_campo1.insert(0, novo_campo2.get()))
    novo_botao_substituir.pack(pady=5) """

# Cria um botão para executar a função de substituição
botao_substituir = tk.Button(janela, text="Substituir", command=substituir, width=30)
botao_substituir.pack(pady=1)

# Cria um botão "Adicionar" para adicionar novos campos de entrada
botao_adicionar = tk.Button(janela, text="Adicionar", command=adicionar_campos, width=30)
botao_adicionar.pack(pady=1)

# Cria o primeiro campo de entrada
campo1 = tk.Entry(janela, width=30)
""" campo1.pack(pady=5) """
campo1.grid(row=0, column=0, padx=5, pady=5)

# Cria o segundo campo de entrada
campo2 = tk.Entry(janela, width=30)
campo2.pack(pady=5)
""" campo2.grid(row=0, column=1, padx=5, pady=5) """


# Inicia a janela principal
janela.mainloop()
