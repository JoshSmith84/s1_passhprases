import tkinter as tk
from tkinter import ttk
from main_page import MainPage


class Application(tk.Tk):
    """Application root window"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.m_page = ''
        self.main_label = ''
        self.title(" S1 Passphrases v1.1")
        self.minsize(400, 350)
        self.main_page()

    def main_page(self):
        self.m_page = MainPage(self)
        self.main_label = ttk.Label(
            self,
            text="S1 Passphrases",
            font=("TKDefaultFont", 14))
        self.main_label.grid(row=0)
        self.m_page.grid(row=1, padx=10, sticky=(tk.W + tk.E))





if __name__ == "__main__":
    app = Application()
    app.grid_columnconfigure(0, weight=1)
    app.mainloop()