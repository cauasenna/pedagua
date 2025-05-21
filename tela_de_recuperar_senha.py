import tkinter as tk
from tkinter import messagebox

# Janela principal
root = tk.Tk()
root.title("Redefinir Senha - Pé d’Água")
root.geometry("900x600")
root.configure(bg="#e6f3f6")  # Cor de fundo azul claro

# Fontes
fonte_titulo = ("Helvetica", 14, "bold")
fonte_subtitulo = ("Helvetica", 10)
fonte_label = ("Helvetica", 10)
fonte_input = ("Helvetica", 10)
fonte_botao = ("Helvetica", 9, "bold")

# ---------- Cabeçalho ----------
header = tk.Frame(root, bg="white", height=50)
header.pack(fill=tk.X)

titulo_app = tk.Label(header, text="Pé d’Água", font=("Helvetica", 10, "bold"), bg="white", fg="black", padx=10)
titulo_app.pack(side=tk.LEFT, pady=10)

# ---------- Título e Subtítulo ----------
titulo = tk.Label(root, text="Redefinir Sua Senha", font=fonte_titulo, bg="#e6f3f6", fg="#1b1b1b")
titulo.pack(pady=(40, 5))

subtitulo = tk.Label(root, text="Digite o código que você recebeu e defina uma nova senha.", font=fonte_subtitulo, bg="#e6f3f6", fg="#1b1b1b")
subtitulo.pack(pady=(0, 30))

# ---------- Formulário ----------
form_frame = tk.Frame(root, bg="#e6f3f6")
form_frame.pack()

# Campo Código
label_codigo = tk.Label(form_frame, text="Código", font=fonte_label, bg="#e6f3f6")
label_codigo.grid(row=0, column=0, sticky="w", padx=10, pady=(5, 5))
entry_codigo = tk.Entry(form_frame, font=fonte_input, width=50, bg="#fefaf3", bd=0, relief="flat", highlightthickness=1, highlightbackground="#f1eadd")
entry_codigo.grid(row=1, column=0, padx=10, pady=(0, 10))

# Nova Senha
label_nova = tk.Label(form_frame, text="Nova Senha", font=fonte_label, bg="#e6f3f6")
label_nova.grid(row=2, column=0, sticky="w", padx=10, pady=(5, 5))
entry_nova = tk.Entry(form_frame, font=fonte_input, show="*", width=50, bg="#fefaf3", bd=0, relief="flat", highlightthickness=1, highlightbackground="#f1eadd")
entry_nova.grid(row=3, column=0, padx=10, pady=(0, 10))

# Confirmar Nova Senha
label_confirmar = tk.Label(form_frame, text="Confirmar Nova Senha", font=fonte_label, bg="#e6f3f6")
label_confirmar.grid(row=4, column=0, sticky="w", padx=10, pady=(5, 5))
entry_confirmar = tk.Entry(form_frame, font=fonte_input, show="*", width=50, bg="#fefaf3", bd=0, relief="flat", highlightthickness=1, highlightbackground="#f1eadd")
entry_confirmar.grid(row=5, column=0, padx=10, pady=(0, 20))

# ---------- Botão "Resetar Senha" ----------
def resetar_senha():
    codigo = entry_codigo.get()
    nova = entry_nova.get()
    confirmar = entry_confirmar.get()

    if not codigo or not nova or not confirmar:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
    elif nova != confirmar:
        messagebox.showerror("Erro", "As senhas não coincidem.")
    else:
        # Aqui entraria a lógica para validar e salvar nova senha
        messagebox.showinfo("Sucesso", "Senha redefinida com sucesso!")

btn_resetar = tk.Button(
    root,
    text="Resetar Senha",
    font=fonte_botao,
    bg="#8ed1e9", fg="black",
    activebackground="#6dc0de",
    bd=0, padx=20, pady=10,
    relief="flat",
    command=resetar_senha
)
btn_resetar.pack(pady=(0, 20), ipadx=150)

# ---------- Iniciar App ----------
root.mainloop()
