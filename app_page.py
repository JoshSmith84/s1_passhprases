import tkinter as tk
from tkinter import ttk


class AppPage(ttk.Frame):
    """Application page class from which all other pages will inherit."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._vars = {}

    def _add_frame(self, label, cols=2):

        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame

    def get(self):
        data = dict()
        for key, variable in self._vars.items():
            try:
                data[key] = variable.get()
            except tk.TclError:
                message = f'Error in field: {key}.'
                raise ValueError(message)
        return data