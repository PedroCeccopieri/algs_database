import tkinter as tk

class MenuIcon:

    def __init__(self, parent, name, icon, x, y, command):
        self.parent = parent
        self.name = name
        self.icon = icon
        self.x = x
        self.y = y
        self.command = command

    def show(self):

        frame = tk.LabelFrame(self.parent, height = 200, width = 200)
        frame.grid(row = self.x, column = self.y, padx = 10, pady = 10)

        lableName = tk.Label(frame, text = self.name, width = 10, height = 1, font = ("Helvectia", 14))
        lableName.pack(pady = 5)

        self.icon.createCanvas(frame)
        self.icon.draw()
        self.icon.getCanvas().pack()

        but = tk.Button(frame, text = "algs", width = 10, font = ("Helvectia", 14), command = self.command)
        but.pack(pady = 5)