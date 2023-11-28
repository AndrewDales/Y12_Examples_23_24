""" Each tkinter widget is an object with its own attributes and methods. To make a clearer GUI structure
we should create subclasses of the tkinter widgets using OOP """

import tkinter as tk


class TestGUI(tk.Frame):
    """ Test GUI subclasses the tk.Frame, so that we can use all the attributes of the tk.Frame and add our own widgets to
    the Frame"""
    def __init__(self, master):
        super().__init__(master)

        # This creates the widgets
        self.txt = tk.Label(self, text="My tkinter app")
        self.btn = tk.Button(self, text="Press me")
        self.edt = tk.Entry(self)

        self.place_widgets()

    def place_widgets(self):
        # This code creates the widgets and packs them on the left
        self.txt.pack(side=tk.LEFT)
        self.btn.pack(side=tk.LEFT)
        self.edt.pack(side=tk.LEFT)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tkinter Class Example')
    main_frame = TestGUI(root)
    main_frame.pack()
    root.mainloop()
