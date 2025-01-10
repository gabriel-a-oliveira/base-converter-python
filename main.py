import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 

cor_fundo = "#f5f5f5" 
cor_titulo = "#4a90e2"  
cor_label = "#333333"  
cor_valor = "#555555" 
cor_botao = "#4CAF50" 
cor_botao_hover = "#45a049"

janela = tk.Tk()
janela.title("Conversor de Base Numérica")
janela.geometry("400x300")
janela.configure(bg=cor_fundo)

janela.rowconfigure(1, weight=1)
janela.columnconfigure(0, weight=1)

frame_cima = tk.Frame(janela, bg=cor_fundo)
frame_cima.grid(row=0, column=0, sticky="nsew", pady=10)

frame_baixo = tk.Frame(janela, bg=cor_fundo)
frame_baixo.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
frame_baixo.columnconfigure(1, weight=1)

app_nome = tk.Label(
    frame_cima, 
    text="Conversor de Base Numérica", 
    font=("Arial", 16, "bold"), 
    bg=cor_fundo, 
    fg=cor_titulo
)
app_nome.pack()

def converter():
    numero = e_valor.get()
    base = combo.get()

    if not base or base == "Selecione":
        messagebox.showwarning("Erro", "Por favor, selecione uma base para conversão!")
        return
    
    if not numero:
        messagebox.showwarning("Erro", "Por favor, insira um número!")
        return

    def numero_para_decimal(numero, base):
        try:
            decimal = int(numero, base)
        except ValueError:
            messagebox.showwarning("Erro", "Número inválido para a base selecionada!")
            return
        
        binario = bin(decimal)[2:] 
        octal = oct(decimal)[2:]  
        hexadecimal = hex(decimal)[2:].upper() 

        l_binario_valor['text'] = binario
        l_octal_valor['text'] = octal
        l_decimal_valor['text'] = str(decimal)
        l_hexadecimal_valor['text'] = hexadecimal

    if base == 'BINÁRIO':
        base = 2
    elif base == 'OCTAL':
        base = 8
    elif base == 'DECIMAL':
        base = 10
    elif base == 'HEXADECIMAL':
        base = 16
    else:
        l_binario_valor['text'] = l_octal_valor['text'] = l_decimal_valor['text'] = l_hexadecimal_valor['text'] = "Erro"
        return

    numero_para_decimal(numero, base)

bases = ['BINÁRIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']
combo = ttk.Combobox(frame_baixo, values=bases, state='readonly', font=("Arial", 11))
combo.set("Selecione")
combo.grid(row=0, column=0, padx=5, pady=10, sticky="w")

e_valor = tk.Entry(frame_baixo, font=("Arial", 12), width=10, justify="center")
e_valor.grid(row=0, column=1, padx=5, pady=10, sticky="ew")

b_converter = tk.Button(
    frame_baixo, 
    text="Converter", 
    font=("Arial", 11), 
    bg=cor_botao, 
    fg="white", 
    activebackground=cor_botao_hover, 
    activeforeground="white", 
    relief="flat", 
    command=converter
)
b_converter.grid(row=0, column=2, padx=5, pady=10)

def criar_label_resultado(texto, row):
    label = tk.Label(frame_baixo, text=texto, font=("Arial", 11), bg=cor_fundo, fg=cor_label)
    label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
    valor = tk.Label(frame_baixo, text="", font=("Arial", 11, "bold"), bg=cor_fundo, fg=cor_valor)
    valor.grid(row=row, column=1, columnspan=2, padx=5, pady=5, sticky="w")
    return valor

l_binario_valor = criar_label_resultado("Binário:", 1)
l_octal_valor = criar_label_resultado("Octal:", 2)
l_decimal_valor = criar_label_resultado("Decimal:", 3)
l_hexadecimal_valor = criar_label_resultado("Hexadecimal:", 4)

janela.mainloop()
