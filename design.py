from tkinter import ttk

def aplicar_estilo_moderno(root):
    style = ttk.Style(root)
    root.configure(bg="#2c2f33")
    style.theme_use("clam")

    fonte_padrao = ("Segoe UI", 12)

    style.configure("TFrame", background="#2c2f33")
    style.configure("TLabel", background="#2c2f33", foreground="#dddddd", font=fonte_padrao)

    style.configure("TEntry",
        font=fonte_padrao,
        fieldbackground="#f0f0f0",
        foreground="#000000",
        borderwidth=1,
        relief="flat")

    style.configure("TButton",
        background="#4e545a",
        foreground="white",
        font=fonte_padrao,
        padding=8,
        borderwidth=0)

    style.map("TButton",
        background=[("active", "#5e656b"), ("!active", "#4e545a")],
        foreground=[("active", "white"), ("!active", "white")])
