import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Registration Form')

        self.registration_frame = RegistrationFrame(self)
        self.registration_frame.pack(fill=tk.BOTH, expand=True)


class RegistrationFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.title_label = tk.Label(self, text='Registration Form', font=('Helvetica', 26))
        self.name_label = tk.Label(self, text='Full name')
        self.name_input = tk.Entry(self)
        self.email_label = tk.Label(self, text='Email')
        self.email_input = tk.Entry(self)
        self.gender_label = tk.Label(self, text='Gender')
        self.gender_input = GenderRadioboxFrame(self)
        self.country_label = tk.Label(self, text='Country')
        self.country_input = ttk.Combobox(self)
        self.programming_label = tk.Label(self, text='Programming')
        self.programming_input = ProgrammingCheckboxFrame(self)
        self.submit_button = tk.Button(self, text='Submit')

        self.country_input['values'] = ('UK', 'USA')

        self.place_widgets()

    def place_widgets(self):
        settings = {
            'padx': 5,
            'pady': 5,
        }
        self.title_label.grid(row=0, column=0, sticky='w', columnspan=2, **settings)
        self.name_label.grid(row=1, column=0, sticky='w', **settings)
        self.name_input.grid(row=1, column=1, sticky='w', **settings)
        self.email_label.grid(row=2, column=0, sticky='w', **settings)
        self.email_input.grid(row=2, column=1, sticky='w', **settings)
        self.gender_label.grid(row=3, column=0, sticky='w', **settings)
        self.gender_input.grid(row=3, column=1, sticky='w', **settings)
        self.country_label.grid(row=4, column=0, sticky='w', **settings)
        self.country_input.grid(row=4, column=1, sticky='w', **settings)
        self.programming_label.grid(row=5, column=0, sticky='w', **settings)
        self.programming_input.grid(row=5, column=1, sticky='w', **settings)
        self.submit_button.grid(row=6, column=0, sticky='w', **settings)



class GenderRadioboxFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        var = tk.IntVar()
        male = tk.Radiobutton(self, text='Male', variable=var, value=0)
        female = tk.Radiobutton(self, text='Female', variable=var, value=1)

        male.pack(side=tk.LEFT)
        female.pack(side=tk.LEFT)


class ProgrammingCheckboxFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        java_var = tk.IntVar()
        python_var = tk.IntVar()

        java = tk.Checkbutton(self, text='Java', variable=java_var)
        python = tk.Checkbutton(self, text='Python', variable=python_var)

        java.pack(side=tk.LEFT)
        python.pack(side=tk.LEFT)

if __name__ == '__main__':
    app = App()
    app.mainloop()