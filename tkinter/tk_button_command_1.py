import tkinter as tk


class ClickApp(tk.Tk):
    def __init__(self):
        # Initiialised the tk.Tk app superclass
        super().__init__()
     
        self.title('Click Counter')
        self.clicker_frame = ButtonClicker(self)
        self.clicker_frame.pack(side=tk.LEFT)


class ButtonClicker(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.counter = 0

        # This creates the widgets   
        self.title_txt = tk.Label(self, text="My clicker app")
        self.btn = tk.Button(self, text="Press me", command=self.button_press)
        self.response_txt = tk.Label(self, text="No clicks yet")

        self.place_widgets()

    def place_widgets(self):
        # Use this for settings that will apply to all widgets
        settings = {'padx': 10, 'pady': 10}
        
        # The **settings 'unpacks' the dictionary into padx=10, pady=10
        self.title_txt.grid(row=0, column=0, **settings)
        self.btn.grid(row=1, column=0, **settings)
        self.response_txt.grid(row=2, column=0, **settings)

    def button_press(self):
        self.counter += 1
        self.response_txt.config(text = f'Clicked: {self.counter} times')


if __name__ == '__main__':
    app = ClickApp()
    app.mainloop()
