import tkinter as tk


def only_decimal(char):
    return char.isdigit() or char == "."


def celsius_to_fahrenheit(temp):
    """ Convert celsius to Fahrenheit"""
    return temp * 9 / 5 + 32


class TemperatureConverter(tk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.temp_celsius = tk.StringVar()
        validation = self.register(only_decimal)

        self.temperature_label = tk.Label(self, text="Celsius")
        self.temperature_entry = tk.Entry(self, textvariable=self.temp_celsius,
                                          validate="key",
                                          validatecommand=(validation, '%S'),
                                          width=10,
                                          justify="center")
        self.convert_button = tk.Button(self, text="Convert", command=self.convert_clicked)
        self.output_label = tk.Label(self)

        # Place the widgets in the TemperatureConverter Frame
        self.place_widgets()

        # Put the focus on the entry box, so that values can be typed in directly
        self.temperature_entry.focus()

        # Bind the return key to invoke the button press
        parent.bind('<Return>', lambda event: self.convert_button.invoke())

    def place_widgets(self):
        padding_options = {'padx': 5, 'pady': 5}

        # Use this method to place your widgets using the grid layout manager
        self.temperature_label.grid(row=0, column=0, sticky="w", **padding_options)
        self.temperature_entry.grid(row=0, column=1, **padding_options)
        self.convert_button.grid(row=0, column=2, **padding_options)
        self.output_label.grid(row=1, column=0, columnspan=3)

    def convert_clicked(self):
        temp_c = float(self.temp_celsius.get())
        temp_f = celsius_to_fahrenheit(temp_c)
        output_message = f'{temp_c:.1f} \N{DEGREE CELSIUS} = {temp_f:.1f} \N{DEGREE FAHRENHEIT}'
        self.output_label.config(text=output_message)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Temperature Converter')
    root.geometry('300x70')
    root.resizable(False, False)
    main_frame = TemperatureConverter(root)
    main_frame.pack()
    root.mainloop()
