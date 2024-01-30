""" Each tkinter widget is an object with its own attributes and methods. To make a clearer GUI structure
we should create subclasses of the tkinter widgets using OOP """

import tkinter as tk
from PIL import  Image, ImageTk

cat_image = Image.open(r'cat_image.jpg').resize((300, 200))

class TestGUI(tk.Frame):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""
    def __init__(self, master):
        super().__init__(master)

        self.cat_image = ImageTk.PhotoImage(cat_image)
        self.counter = 0

        # This creates the widgets
        self.txt = tk.Label(self, text="My tkinter app")
        self.btn = tk.Button(self, image=self.cat_image, command=self.button_press)
        self.response_text = tk.Label(self, text="No clicks left")
        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and packs them on the left
        self.txt.pack(side=tk.TOP)
        self.btn.pack(side=tk.TOP, padx=10, pady=10, ipadx=5, ipady=5)
        self.response_text.pack(side=tk.TOP, pady=10)

    def button_press(self):
        self.counter += 1
        self.response_text.config(text=f'Cat picture clicked {self.counter} times')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tkinter Picture Button')
    main_frame = TestGUI(root)
    main_frame.pack()
    root.mainloop()
