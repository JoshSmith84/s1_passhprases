
import customtkinter as ctk
from main_page import MainPage


class Application(ctk.CTk):
    """Application root window"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.m_page = ''
        self.main_label = ''
        self.title(" S1 Passphrases v1.1")
        self.minsize(400, 350)
        self.main_page()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=100)


    def main_page(self):
        self.m_page = MainPage(self)
        self.main_label = ctk.CTkLabel(
            self,
            text="S1 Passphrases",
            font=("TKDefaultFont", 14))
        self.main_label.grid(row=0)
        self.main_label.grid_columnconfigure(0, weight=1)
        self.main_label.grid_rowconfigure(0, weight=1)
        self.m_page.grid(row=1, padx=10, sticky="nsew")
        self.m_page.rowconfigure(1, weight=100)
        self.m_page.columnconfigure(0, weight=1)





if __name__ == "__main__":
    app = Application()
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.mainloop()