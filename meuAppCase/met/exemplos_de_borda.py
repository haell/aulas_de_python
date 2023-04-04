# Exemplos de borda criadas pelo GPT
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        master.title("Exemplo de Bordas em Labels")
        
        # Borda sólida
        label_solid = tk.Label(master, text="Borda Sólida", bd=4, relief="solid", highlightbackground="red", highlightthickness=1)
        label_solid.grid(row=0, column=0, padx=15, pady=15)

        # Borda em relevo
        label_raised = tk.Label(master, text="Borda em Relevo", bd=4, relief="raised", highlightbackground="red", highlightthickness=1)
        label_raised.grid(row=0, column=1, padx=15, pady=15)

        # Borda em sulco
        label_sunken = tk.Label(master, text="Borda em Sulco", bd=4, relief="sunken", highlightbackground="red", highlightthickness=1)
        label_sunken.grid(row=1, column=0, padx=15, pady=15)

        # Borda plana
        label_flat = tk.Label(master, text="Borda Plana", bd=4, relief="flat", highlightbackground="red", highlightthickness=1)
        label_flat.grid(row=1, column=1, padx=15, pady=15)

        # Define o tamanho dos elementos ao redor das colunas
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)


root = tk.Tk()
my_app = App(root)
root.mainloop()
