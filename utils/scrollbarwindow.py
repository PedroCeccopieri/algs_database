import tkinter as tk
from tkinter import ttk


def scrollbarWindow():

    root = tk.Toplevel()

    mainFrame = tk.Frame(root)
    mainFrame.pack(fill = tk.BOTH, expand = 1)
    canvas = tk.Canvas(mainFrame)
    canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
    scrollbar = ttk.Scrollbar(mainFrame, orient = tk.VERTICAL, command = canvas.yview)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    canvas.configure(yscrollcommand = scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
    frame = tk.Frame(canvas)
    canvas.create_window((0,0), window = frame, anchor = "nw")

    return (root,frame)