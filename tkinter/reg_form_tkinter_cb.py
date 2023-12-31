import tkinter as tk
from tkinter import ttk
import json


class RegistrationFrame(tk.Frame):
    """ RegistrationFrame displays a typical registration form"""

    def __init__(self, parent):
        super().__init__(parent)
        self.contents = None
        self.data_file = "registration_data.json"

        text_labels = ["Registration Form", "Full name", "Email", "Gender", "Country", "Programming"]
        country_options = ["France", "Germany", "United Kingdom", "United States", "Other"]

        # Add widgets
        # Text labels
        self.labels = [tk.Label(self, text=text_label,
                                justify=tk.LEFT,
                                font=('Arial', 12))
                       for text_label in text_labels]
        self.labels[0].config(font=('Arial', 24))

        # Submit button
        self.submit_button = tk.Button(self, text='Submit',
                                       command=self.get_results,
                                       bg="red",
                                       fg="white",
                                       font=('Arial', 12),
                                       )

        # Edit boxes
        self.edits = [tk.Entry(self, width=40, font=('Arial', 12))
                      for _ in range(2)]

        # Frame with gender choices - radio buttons
        self.gender_frame = GenderRadioBox(self)

        # Country dropdown
        self.country_var = tk.StringVar()
        self.country_var.set("select your country")
        self.country_select = ttk.Combobox(self,
                                           textvariable=self.country_var,
                                           values=country_options,
                                           width=20,
                                           font=('Arial', 12),
                                           )
        self.country_select.bind('<<ComboboxSelected>>', self.change_country)

        # Frame with programs check boxes
        self.program_frame = ProgramCheckBox(self)

        # Place the widgets in the grid
        self.place_widgets()

    def place_widgets(self):
        # Place all the text labels in self.labels using grid
        # Registration Label - include columnspan across both columns
        self.labels[0].grid(row=0, column=0, columnspan=2, padx=10, pady=3, sticky="w")
        for i, label in enumerate(self.labels[1:], 1):
            label.grid(row=i, column=0, padx=10, pady=3, sticky="w")

        # Place Submit button
        self.submit_button.grid(row=len(self.labels),
                                column=0, padx=15, pady=(3, 10), sticky="w",
                                )

        # Place Edit Boxes
        for i, edt in enumerate(self.edits, 1):
            edt.grid(row=i, column=1, padx=(10, 25), pady=3, sticky="we")

        # Place the Gender frame
        self.gender_frame.grid(row=3, column=1, padx=10, pady=3, sticky="w")

        # Place drop-down window
        self.country_select.grid(row=4, column=1, padx=10, pady=3, sticky="w")

        # Place the Programs frame
        self.program_frame.grid(row=5, column=1, padx=10, pady=3, sticky="w")

    def get_results(self):
        program_options = [option[0] for option in self.program_frame.program_options
                           if option[1].get()]
        self.contents = {'Name': self.edits[0].get(),
                         'Email': self.edits[1].get(),
                         'Gender': self.gender_frame.selected_gender.get(),
                         'Country': self.country_var.get(),
                         'Programs': program_options,
                         }
        with open(self.data_file, "w") as outfile:
            json.dump(self.contents, outfile)
        self.master.destroy()

    def change_country(self, event):
        print(f'You choose country {self.country_var.get()}')


class GenderRadioBox(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        gender_values = [('Male', 'M'),
                         ('Female', 'F'),
                         ('Other', 'O'),
                         ('Prefer not to say', 'P'),
                         ]

        self.selected_gender = tk.StringVar()
        self.selected_gender.set('P')

        self.radio_options = [tk.Radiobutton(self, text=option[0],
                                             value=option[1],
                                             variable=self.selected_gender,
                                             command=self.radio_select,
                                             font=('Arial', 12))
                              for option in gender_values]

        for ro in self.radio_options:
            ro.pack(side=tk.LEFT)

    def radio_select(self):
        print(f'You selected {self.selected_gender.get()}')


class ProgramCheckBox(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        options = ["C++", "Java", "JavaScript", "Python"]
        self.program_options = list(zip(options, [tk.IntVar() for _ in options]))

        self.cb_options = [tk.Checkbutton(self, text=option[0],
                                          variable=option[1],
                                          font=('Arial', 12),
                                          command=self.cb_select
                                          )
                           for option in self.program_options]

        for cb in self.cb_options:
            cb.pack(side=tk.LEFT)

    def cb_select(self):
        chosen_options = [option[0] for option in self.program_options if option[1].get()]
        if any(chosen_options):
            print(f'You selected the programs: {", ".join(chosen_options)}')
        else:
            print(f'You selected no programs')


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Registration Form')
    root.resizable(0, 0)
    RegistrationFrame(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
