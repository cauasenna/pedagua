import tkinter as tk
from tkinter import font

# Janela principal
root = tk.Tk()
root.title("Pé d'Água - Cadastro")
root.geometry("900x600")
root.configure(bg="#e6f3f6")  # Fundo azul claro

# Fonte personalizada
fonte_titulo = ("Helvetica", 14, "bold")
fonte_label = ("Helvetica", 10)
fonte_input = ("Helvetica", 10)
fonte_botao = ("Helvetica", 9, "bold")

# ---------- Cabeçalho ----------
header = tk.Frame(root, bg="white", height=50)
header.pack(fill=tk.X)

titulo_app = tk.Label(header, text="Pé d’Água", font=("Helvetica", 10, "bold"), bg="white", fg="black", padx=10)
titulo_app.pack(side=tk.LEFT, pady=10)

# ---------- Título Central ----------
titulo = tk.Label(root, text="Bem Vindo ao Pé d’Água", bg="#e6f3f6", font=fonte_titulo, fg="#1b1b1b")
titulo.pack(pady=(50, 20))

# ---------- Formulário ----------
form_frame = tk.Frame(root, bg="#e6f3f6")
form_frame.pack()

# Nome
label_nome = tk.Label(form_frame, text="Nome", font=fonte_label, bg="#e6f3f6")
label_nome.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 5))
entry_nome = tk.Entry(form_frame, font=fonte_input, width=50, bg="#fefaf3", bd=0, relief="flat", highlightthickness=1, highlightbackground="#f1eadd")
entry_nome.grid(row=1, column=0, padx=10, pady=(0, 15))

# Login
label_login = tk.Label(form_frame, text="Cadastro de Login", font=fonte_label, bg="#e6f3f6")
label_login.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 5))
entry_login = tk.Entry(form_frame, font=fonte_input, width=50, bg="#fefaf3", bd=0, relief="flat", highlightthickness=1, highlightbackground="#f1eadd")
entry_login.grid(row=3, column=0, padx=10, pady=(0, 15))

# Senha
label_senha = tk.Label(form_frame, text="Cadastro de Senha", font=fonte_label, bg="#e6f3f6")
label_senha.grid(row=4, column=0, sticky="w", padx=10, pady=(10, 5))
entry_senha = tk.Entry(form_frame, font=fonte_input, show="*", width=50, bg="#fefaf3", bd=0, relief="flat", highlightthickness=1, highlightbackground="#f1eadd")
entry_senha.grid(row=5, column=0, padx=10, pady=(0, 30))

# ---------- Botão Entrar ----------
def entrar():
    nome = entry_nome.get()
    login = entry_login.get()
    senha = entry_senha.get()
    print(f"Nome: {nome}, Login: {login}, Senha: {senha}")
    # Aqui você pode mudar para outra tela ou verificar login

botao_entrar = tk.Button(
    root, text="→  Entrar",
    font=fonte_botao,
    bg="#8ed1e9", fg="black",
    activebackground="#6dc0de",
    bd=0, padx=20, pady=8,
    relief="flat",
    command=entrar
)
botao_entrar.place(relx=0.75, rely=0.7)

# ---------- Iniciar a aplicação ----------
root.mainloop()
