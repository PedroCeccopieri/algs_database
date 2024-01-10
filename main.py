import tkinter as tk

from utils.saveAndLoad import *
from utils.menuIcons import *

from puzzles.c333 import c333
from algs_3x3.algs333_functions import algs333




root = tk.Tk()
root.title("ALGS")
root.geometry('600x400+100+100')

df = load("OLL333")

MenuIcon(root, "3x3", c333(150, 150, df["top"].iloc[0], df["side"].iloc[0]), 0, 0, algs333).show()

root.mainloop()