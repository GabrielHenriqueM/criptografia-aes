import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import tkinter as tk
from tkinter import ttk, messagebox
from aes_cipher import AESCipher
from design import aplicar_estilo_moderno

def cifrar_mensagem():
    chave = entry_chave_cifrar.get()
    mensagem = entry_mensagem_cifrar.get()
    if len(chave) < 8:
        messagebox.showerror("Erro", "A chave deve ter no mínimo 8 caracteres.")
        return
    if not mensagem:
        messagebox.showwarning("Aviso", "Digite a mensagem.")
        return
    try:
        aes = AESCipher(chave)
        texto_cifrado = aes.cifrar(mensagem)
        resultado_cifrado_var.set(texto_cifrado)
        entry_chave_cifrar.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cifrar: {e}")

def decifrar_mensagem():
    chave = entry_chave_decifrar.get()
    mensagem_cifrada = entry_mensagem_decifrar.get()
    if len(chave) < 8:
        messagebox.showerror("Erro", "A chave deve ter no mínimo 8 caracteres.")
        return
    if not mensagem_cifrada:
        messagebox.showwarning("Aviso", "Digite a mensagem cifrada.")
        return
    try:
        aes = AESCipher(chave)
        mensagem_decifrada = aes.decifrar(mensagem_cifrada)
        resultado_decifrado_var.set(mensagem_decifrada)
        entry_chave_decifrar.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao decifrar: {e}")

def limpar_cifrar():
    entry_mensagem_cifrar.delete(0, tk.END)
    entry_chave_cifrar.delete(0, tk.END)
    resultado_cifrado_var.set("")

def limpar_decifrar():
    entry_mensagem_decifrar.delete(0, tk.END)
    entry_chave_decifrar.delete(0, tk.END)
    resultado_decifrado_var.set("")

root = tk.Tk()
root.title("🔐 Criptografia AES")

largura_janela = 800
altura_janela = 460
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
posx = (largura_tela - largura_janela) // 2
posy = (altura_tela - altura_janela) // 2
root.geometry(f"{largura_janela}x{altura_janela}+{posx}+{posy}")

aplicar_estilo_moderno(root)

notebook = ttk.Notebook(root)
notebook.pack(padx=20, pady=20, expand=True, fill="both")

frame_cifrar = ttk.Frame(notebook)
notebook.add(frame_cifrar, text="🔐 Cifrar")

ttk.Label(frame_cifrar, text="Mensagem:").pack(pady=(10, 0))
entry_mensagem_cifrar = ttk.Entry(frame_cifrar, width=80)
entry_mensagem_cifrar.pack(pady=5)

ttk.Label(frame_cifrar, text="Chave de Criptografia:").pack()
entry_chave_cifrar = ttk.Entry(frame_cifrar, width=80, show="*")
entry_chave_cifrar.pack(pady=5)

ttk.Button(frame_cifrar, text="CIFRAR", command=cifrar_mensagem).pack(pady=10)

ttk.Label(frame_cifrar, text="Resultado - Mensagem Cifrada:").pack()
resultado_cifrado_var = tk.StringVar()
ttk.Entry(frame_cifrar, textvariable=resultado_cifrado_var, width=80, state="readonly").pack(pady=5)

ttk.Button(frame_cifrar, text="LIMPAR", command=limpar_cifrar).pack(pady=(5, 15))

frame_decifrar = ttk.Frame(notebook)
notebook.add(frame_decifrar, text="🔓 Decifrar")

ttk.Label(frame_decifrar, text="Mensagem Cifrada:").pack(pady=(10, 0))
entry_mensagem_decifrar = ttk.Entry(frame_decifrar, width=80)
entry_mensagem_decifrar.pack(pady=5)

ttk.Label(frame_decifrar, text="Chave de Criptografia:").pack()
entry_chave_decifrar = ttk.Entry(frame_decifrar, width=80, show="*")
entry_chave_decifrar.pack(pady=5)

ttk.Button(frame_decifrar, text="DECIFRAR", command=decifrar_mensagem).pack(pady=10)

ttk.Label(frame_decifrar, text="Resultado - Mensagem Decifrada:").pack()
resultado_decifrado_var = tk.StringVar()
ttk.Entry(frame_decifrar, textvariable=resultado_decifrado_var, width=80, state="readonly").pack(pady=5)

ttk.Button(frame_decifrar, text="LIMPAR", command=limpar_decifrar).pack(pady=(5, 15))

root.mainloop()
