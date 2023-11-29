from tkinter import ttk
import tkinter as tk


class Registration(tk.Tk):

    def __init__(self):
        super().__init__()

        self.settings = {'padx': 10, 'pady': 10}
        self.title("Registration form")
        self.submit_btn = tk.Button(self, text="Submit")
        self.submit_btn.config(bg="red")
        self.title_txt = tk.Label(self, text="Registration Form")
        self.name_entry = tk.Entry(width=50)
        self.email_entry = tk.Entry(width=50)
        self.female = tk.Radiobutton(text="Female", value="Female")
        self.male = tk.Radiobutton(text="Male", value="Male")

        self.country_dropdown = ttk.Combobox(values=["Poland", "Monaco", "indonesia"])
        self.country_dropdown["state"] = "readonly"
        self.python = tk.Checkbutton(text="Python")
        self.java = tk.Checkbutton(text="Java")
        text = ["Full Name", "Email", "Gender", "Country", "Programming"]
        x = 1
        for item in text:
            self.response_txt = tk.Label(self, text=item)
            self.response_txt.grid(row=x, column=0, sticky="W", **self.settings)
            x += 1

        self.place_widgets()

    def place_widgets(self):
        global settings
        self.title_txt.grid(row=0, column=0, **self.settings)
        self.submit_btn.grid(row=6, column=0, **self.settings)

        self.name_entry.grid(row=1, column=1, columnspan=2, **self.settings)
        self.email_entry.grid(row=2, column=1, columnspan=2, **self.settings)
        self.female.grid(row=3, column=1, sticky="W", **self.settings)
        self.male.grid(row=3, column=2, sticky="W", **self.settings)
        self.country_dropdown.grid(row=4, column=1,sticky="W", **self.settings)
        self.python.grid(row=5, column=1, sticky="W", **self.settings)
        self.java.grid(row=5, column=2, sticky="W", **self.settings)


if __name__ == '__main__':
    app = Registration()
    app.mainloop()
    app.resizable(True, True)
    app.geometry("1000x1000")

#didnt manage to put the "select your country"
#couldnt make the radio and checkbuttons go all the way to the left