import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class GraphFrame(tk.Frame):
    def __init__(self):
        super().__init__()

        fig = Figure(figsize=(5, 5),
                     dpi=100)

        # list of squares
        y = [i ** 2 for i in range(101)]

        # adding the subplot
        ax = fig.add_subplot(111)

        # plotting the graph
        ax.plot(y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()


# GUI
root = tk.Tk()
root.title("Simple plot in tkinter")
graph_page = GraphFrame()
graph_page.pack()
root.mainloop()
