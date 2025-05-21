import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk

# =================== Função da API ===================
def buscar_clima():
    cidade = entrada.get()
    api_key = "SUA_CHAVE_AQUI"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if resposta.status_code == 200:
            nome_cidade = dados["name"]
            temperatura = dados["main"]["temp"]
            umidade = dados["main"]["humidity"]
            descricao = dados["weather"][0]["description"]

            cidade_label.config(text=nome_cidade)
            temp_label.config(text=f"{temperatura:.0f}°C")
            descricao_label.config(text=descricao.capitalize())
            umidade_label.config(text=f"Umidade: {umidade}%")
        else:
            cidade_label.config(text="Cidade não encontrada")
            temp_label.config(text="")
            descricao_label.config(text="")
            umidade_label.config(text="")
    except:
        cidade_label.config(text="Erro ao conectar")
        temp_label.config(text="")
        descricao_label.config(text="")
        umidade_label.config(text="")

# =================== Interface Tkinter ===================
janela = tk.Tk()
janela.title("Pé d'Água")
janela.geometry("600x1000")
janela.configure(bg="#e0f7fa")


header = tk.Frame(janela, bg="#fffdeb", height=60)
header.pack(fill="x")

logo = tk.Label(header, text="Pé d'Água", font=("Arial", 12, "bold"), bg="#fffdeb")
logo.place(x=10, y=20)

pesquisa_frame = tk.Frame(header, bg="#f6f6d6", bd=1, relief="solid")
pesquisa_frame.place(x=380, y=15, width=150, height=30)

lupa = tk.Label(pesquisa_frame, text="🔍", bg="#f6f6d6")
lupa.pack(side="left", padx=5)

entrada = tk.Entry(pesquisa_frame, bd=0, font=("Arial", 10), bg="#f6f6d6")
entrada.pack(side="left", fill="both", expand=True)
entrada.bind("<Return>", lambda e: buscar_clima())

usuario_icon = tk.Label(header, text="🧑", font=("Arial", 14), bg="#fffdeb")
usuario_icon.place(x=550, y=15)


body = tk.Frame(janela, bg="#e0f7fa")
body.pack(fill="both", expand=True, pady=20)

cidade_label = tk.Label(body, text="San Francisco", font=("Arial", 14, "bold"), bg="#e0f7fa")
cidade_label.pack()

temp_label = tk.Label(body, text="66°C", font=("Arial", 16, "bold"), bg="#e0f7fa")
temp_label.pack(pady=5)

descricao_label = tk.Label(body, text="Céu limpo", font=("Arial", 12), bg="#e0f7fa")
descricao_label.pack()

umidade_label = tk.Label(body, text="Umidade: 40%", font=("Arial", 12), bg="#e0f7fa")
umidade_label.pack(pady=5)


def criar_cartao(parent, hora, temp):
    card = tk.Frame(parent, bg="white", width=150, height=150)
    card.pack(side="left", padx=10)

    img = tk.Label(card, bg="#99c2e6", width=18, height=7)
    img.pack(pady=5)

    hora_label = tk.Label(card, text=hora, bg="white", font=("Arial", 10))
    hora_label.pack()

    temp_label = tk.Label(card, text=temp, bg="white", font=("Arial", 10))
    temp_label.pack()

# =================== Seção Hoje ===================
hoje_label = tk.Label(body, text="Hoje", font=("Arial", 12, "bold"), bg="#e0f7fa")
hoje_label.pack(anchor="w", padx=20)

hoje_frame = tk.Frame(body, bg="#e0f7fa")
hoje_frame.pack(pady=10)

criar_cartao(hoje_frame, "15:00", "21°C")
criar_cartao(hoje_frame, "18:00", "25°C")
criar_cartao(hoje_frame, "21:00", "18°C")


amanha_label = tk.Label(body, text="Amanhã", font=("Arial", 12, "bold"), bg="#e0f7fa")
amanha_label.pack(anchor="w", padx=20, pady=(20, 0))

amanha_frame = tk.Frame(body, bg="#e0f7fa")
amanha_frame.pack(pady=10)

criar_cartao(amanha_frame, "15:00", "27°C")
criar_cartao(amanha_frame, "18:00", "27°C")
criar_cartao(amanha_frame, "21:00", "30°C")

# =================== Seção Ontem ===================
ontem_label = tk.Label(body, text="Ontem", font=("Arial", 12, "bold"), bg="#e0f7fa")
ontem_label.pack(anchor="w", padx=20, pady=(20, 0))

ontem_frame = tk.Frame(body, bg="#e0f7fa")
ontem_frame.pack(pady=10)

criar_cartao(ontem_frame, "15:00", "17°C")
criar_cartao(ontem_frame, "18:00", "21°C")
criar_cartao(ontem_frame, "21:00", "14°C")

# Iniciar janela
janela.mainloop()

