import tkinter as tk
from tkinter import messagebox

black = "#131417"
green = "#0f0"


class GUI:
    def __init__(self):

        # Setting up window
        self.root = tk.Tk()
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.title("Medidor de Temperatura")

        # self.root.iconbitmap("icon.ico")
        self.root.config(bg=black)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.display = tk.Label(self.root, text="00°C")
        self.display.config(font=("Arial", 52), fg=green, anchor="center", bg=black)
        self.display.place(x=200, y=180, anchor="center")

        self.button_grid = tk.Frame(self.root)
        self.button_grid.columnconfigure(0)

        self.power_button = tk.Button(self.button_grid, text="Ligar/Desligar", command=self.switch_power)
        self.power_button.config(font=("Arial", 26), bg=black, activebackground=green, fg=green, activeforeground=black)
        self.power_button.grid(row=0, column=0)

        self.reset_button = tk.Button(self.button_grid, text="Atualizar", command=self.reset_info)
        self.reset_button.config(font=("Arial", 26), bg=black, activebackground=green, fg=green, activeforeground=black)
        self.reset_button.grid(row=0, column=1)

        self.button_grid.pack(side="bottom")

        # Start program
        self.root.mainloop()

    def switch_power(self):
        pass

    def reset_info(self):
        pass

    def on_closing(self):
        if messagebox.askyesno(title="Sair?", message="Quer mesmo sair?"):
            self.root.destroy()