import tkinter as tk

# 1 - criando a janela
janela = tk.Tk()
janela.geometry("300x150")
janela.title("Gerenciador de frases")

# 2 - adicionando o frame
frame = tk.Frame(janela)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - adicionando o label
label = tk.Label(frame, text="Hello, World")
label.pack(fill='x', expand=True)

# 4 - Adicionando o input text
frase_lab = tk.Label(frame, text='Frase')
frase_lab.pack(fill='x', expand=True)

frase_input = tk.Entry(frame)
frase_input.pack(fill='x', expand=True)

# 5 - Função para alterar o texto do label
def click():
    label.config(text=frase_input)

# 6 Adicionando botão
botao = tk.Button(frame, text="Enviar", command=click)
botao.pack()

janela.mainloop()