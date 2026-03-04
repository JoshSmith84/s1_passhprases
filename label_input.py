
import customtkinter as ctk


class LabelInput(ctk.CTkFrame):
    """A widget containing a label and input together."""

    def __init__(
            self, parent, label, var, input_class=ctk.CTkEntry,
            input_args=None, label_args=None, **kwargs
    ):
        super().__init__(parent, **kwargs)
        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = var
        self.variable.label_widget = self

        if input_class in (ctk.CTkCheckBox, ctk.CTkButton):
            input_args["text"] = label
        else:
            self.label = ctk.CTkLabel(self, text=label, **label_args)
            self.label.grid(row=0, column=0, sticky="nsew")

        if input_class in (
            ctk.CTkCheckBox, ctk.CTkButton, ctk.CTkRadioButton
        ):
            input_args["variable"] = self.variable
        else:
            input_args["textvariable"] = self.variable

        if input_class == ctk.CTkRadioButton:
            self.input = ctk.CTkFrame(self)
            for v in input_args.pop('values', []):
                button = ctk.CTkRadioButton(
                    self.input, value=v, text=v, **input_args
                )
                button.pack(
                    side=ctk.LEFT, ipadx=10,
                    ipady=2, expand=True, fill='x'
                )
        else:
            self.input = input_class(self, **input_args)

        self.input.grid(row=1, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)

    def grid(self, sticky="nsew", **kwargs):
        """Override grid to add default sticky values"""
        super().grid(sticky=sticky, **kwargs)

