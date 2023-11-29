import tkinter as tk
from tkinter import ttk


class RegistrationForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Registration Form')
        self.text_boxes = TextBoxes(self)
        self.gender_options = GenderRadioOptions(self)
        self.country_options = CountryOptions(self)
        self.programming_options = ProgrammingOptions(self)
        self.input_button = tk.Button(self, text="Input", bg="#2887a1")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}
        self.text_boxes.pack(side=tk.TOP)
        self.gender_options.pack(side=tk.TOP)
        self.country_options.pack(side=tk.TOP)
        self.programming_options.pack(side=tk.TOP)
        self.input_button.pack(side=tk.TOP, **settings)


class TextBoxes(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.name_txt = tk.Label(self, text="Full name")
        self.name_box = tk.Entry(self, width=40)

        self.email_txt = tk.Label(self, text="Email")
        self.email_box = tk.Entry(self, width=60)

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}
        self.name_txt.grid(row=0, column=0, **settings)
        self.name_box.grid(row=0, column=1, sticky='we', **settings)
        self.email_txt.grid(row=1, column=0, **settings)
        self.email_box.grid(row=1, column=1, sticky='we', **settings)


class GenderRadioOptions(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.gender_txt = tk.Label(self, text="Gender")
        self.selected_gender = tk.StringVar()
        self.selected_gender.set('Male')
        self.gender_options = [tk.Radiobutton(self, text="Male", value="Male", variable=self.selected_gender),
                               tk.Radiobutton(self, text="Female", value="Female", variable=self.selected_gender)]

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}
        self.gender_txt.grid(row=0, column=0, sticky="w", **settings)
        for i in range(len(self.gender_options)):
            self.gender_options[i].grid(row=0, column=i + 1, sticky="w", **settings)


class CountryOptions(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.country_txt = tk.Label(self, text="Country")
        self.current_var = tk.StringVar()
        self.current_var.set("select your country")
        self.combobox = ttk.Combobox(self, textvariable=self.current_var)
        self.combobox['values'] = ("United Kingdom", "USA", "France", "Japan", "China", "Canada", "Other")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}
        self.country_txt.grid(row=0, column=0, **settings)
        self.combobox.grid(row=0, column=1, **settings)


class ProgrammingOptions(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.programming_txt = tk.Label(self, text="Programming")
        self.ja_checkbox = ttk.Checkbutton(self, text="Java")
        self.py_checkbox = ttk.Checkbutton(self, text="Python")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}
        self.programming_txt.grid(row=0, column=0, **settings)
        self.ja_checkbox.grid(row=0, column=1, **settings)
        self.py_checkbox.grid(row=0, column=2, **settings)


if __name__ == '__main__':
    form = RegistrationForm()
    form.mainloop()
