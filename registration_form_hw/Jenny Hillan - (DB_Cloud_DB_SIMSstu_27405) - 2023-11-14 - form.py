import tkinter as tk
import tkinter.ttk as ttk
import pycountry


class ClickApp(tk.Tk):
    def __init__(self):
        # Initialised the tk.Tk app
        super().__init__()

        self.title('Registration Form')
        self.clicker_frame = ContactInformation(self)
        self.clicker_frame.pack(side=tk.TOP)
        self.gender = Gender(self)
        self.gender.pack(side=tk.TOP)
        self.country = Country(self)
        self.country.pack(side=tk.TOP)
        self.lang = Language(self)
        self.lang.pack(side=tk.TOP)
        self.submit = SubmitButton(self)
        self.submit.pack(side=tk.TOP)


class ContactInformation(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # This creates the widgets
        self.title_txt = tk.Label(self, text="Registration form", font=25)
        self.btn = tk.Button(self, text="Submit")
        self.label_name = tk.Label(self, text="Full name")
        self.label_email = tk.Label(self, text="Email")
        self.response_name = tk.Entry(self)
        self.response_email = tk.Entry(self)

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}

        self.title_txt.grid(row=0, column=0, **settings)
        self.label_name.grid(row=1, column=0, **settings)
        self.response_name.grid(row=1, column=1, **settings)
        self.label_email.grid(row=2, column=0, **settings)
        self.response_email.grid(row=2, column=1, **settings)


class SubmitButton(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.btn = tk.Button(self, text="Submit")
        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 20}
        self.btn.pack(side="right", **settings)


class Gender(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.label_gender = tk.Label(self, text="Gender")

        self.gender = ["Female", "Male"]

        # Create radio buttons (list comprehension)
        self.radio_options = (tk.Radiobutton(self, text=gender,
                                             value=gender,
                                             )
                              for gender in self.gender)

        self.place_widgets()

    def place_widgets(self):
        self.label_gender.pack(side="left")
        for ro in self.radio_options:
            ro.pack(side="right", padx=10, pady=5)


class Language(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.label_langs = tk.Label(self, text="Languages")
        self.langs = ["Java", "Python"]

        self.language_options = (tk.Checkbutton(self, text=lang, )
                                 for lang in self.langs)

        self.place_widgets()

    def place_widgets(self):
        self.label_langs.pack(side="left")
        for box in self.language_options:
            box.pack(side="right", anchor="n", padx=5, pady=5)


class Country(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Country")
        self.countries = ttk.Combobox(self)
        self.country_list = [count.name for count in pycountry.countries]
        self.country_list.sort()
        self.countries['values'] = self.country_list
        self.countries['state'] = "readonly"

        self.place_widgets()

    def place_widgets(self):
        self.label.pack(anchor="n", side="left")
        self.countries.pack(padx=5, pady=5, side="right")


if __name__ == '__main__':
    app = ClickApp()
    app.geometry("450x500")
    app.mainloop()
