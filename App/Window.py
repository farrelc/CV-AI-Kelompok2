import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Eye Refresh App')
        self.geometry('1200x640')
        self.resizable(0,0)

        # label
        self.label = ttk.Label(self, text='Hello, Welcome to the App')
        self.label.pack()



