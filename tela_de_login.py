import tkinter as tk
from tkinter import font

# Janela principal
root = tk.Tk()
root.title("Login - Pé d’Água")
root.geometry("900x600")
root.configure(bg="#e6f3f6")  # Fundo azul claro

# Fontes
fonte_titulo = ("Helvetica", 14, "bold")
fonte_label = ("Helvetica", 10)
fonte_input = ("Helvetica", 10)
fonte_botao = ("Helvetica", 9, "bold")
fonte_link = ("Helvetica", 8)

# ---------- Cabeçalho ----------
header = tk.Frame(root, bg="white", height=50)
header.pack(fill=tk.X)

titulo_app = tk.Label(header, text="Pé d’Água", font=("Helvetica", 10, "bold"), bg="white", fg="black", padx=10)
titulo_app.pack(side=tk.LEFT, pady=10)

# ---------- Título Central ----------
titulo = tk.Label(root, text="Bem Vindo Ao Pé d’Água", bg="#e6f3f6", font=fonte_titulo, fg="#1b1b1b")
titulo.pack(pady=(50, 30))

# ---------- Formulário ----------
form_frame = tk.Frame(root, bg="#e6f3f6")
form_frame.pack()

# Email
label_email = tk.Label(form_frame, text="Email", font=fonte_label, bg="#e6f3f6")
label_email.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 5))
entry_email = tk.Entry(form_frame, font=fonte_input, width=50, bg="#fefaf3", bd=0, relief="flat", highlightthickness=1, highlightbackground="#f1eadd")
entry_email.grid(row=1, column=0, padx=10, pady=(0, 15))

# Senha
label_senha = tk.Label(form_frame, text="Password", font=fonte_label, bg="#e6f3f6")
label_senha.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 5))
entry_senha = tk.Entry(form_frame, font=fonte_input, show="*", width=50, bg="#fefaf3", bd=0, relief="flat", highlightthickness=1, highlightbackground="#f1eadd")
entry_senha.grid(row=3, column=0, padx=10, pady=(0, 10))

# ---------- Link "Esqueceu sua senha?" ----------
link_senha = tk.Label(form_frame, text="Esqueceu Sua Senha?", font=fonte_link, bg="#e6f3f6", fg="#9aa276", cursor="hand2")
link_senha.grid(row=4, column=0, sticky="w", padx=10, pady=(5, 20))

def abrir_recuperacao_senha(event):
    print("Link de recuperação de senha clicado!")
    # Aqui você pode chamar outra janela ou função

link_senha.bind("<Button-1>", abrir_recuperacao_senha)

# ---------- Botão Entrar ----------
def entrar():
    email = entry_email.get()
    senha = entry_senha.get()
    print(f"Email: {email}, Senha: {senha}")
    # Aqui pode validar, redirecionar para próxima tela etc.

botao_entrar = tk.Button(
    root, text="→  Entrar",
    font=fonte_botao,
    bg="#8ed1e9", fg="black",
    activebackground="#6dc0de",
    bd=0, padx=20, pady=8,
    relief="flat",
    command=entrar
)
botao_entrar.place(relx=0.75, rely=0.6)

# ---------- Iniciar o app ----------
root.mainloop()
