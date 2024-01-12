import tkinter as tk

import sys
sys.path.append('../')

from puzzles.c333 import c333
from utils.menuIcons import MenuIcon
from utils.saveAndLoad import load
from utils.scrollbarwindow import scrollbarWindow

df = load("PLL333")

def pll():

    l = df.shape[0]
    c = 5
    r = l // c + 1

    pll_window, pll_frame = scrollbarWindow()
    pll_window.title("PLL")
    pll_window.geometry('900x500+100+100')

    for i in range(r):
        for j in range(c):

            if (5 * i + j < l):
                MenuIcon(pll_frame, f"Case {df['name'].iloc[5 * i + j]}", c333(150, 150, df["top"].iloc[5 * i + j], df["side"].iloc[5 * i + j], df["arrows"].iloc[5 * i + j]), i, j, command = lambda c = 5 * i + j: choosePll(c)).show()

def choosePll(ncase):

        pllcase_window = tk.Toplevel()
        pllcase_window.title(f"PLL Case {ncase}")
        pllcase_window.geometry('600x400+200+200')

        ca = c333(150, 150, df["top"].iloc[ncase], df["side"].iloc[ncase], df["arrows"].iloc[ncase])
        ca.createCanvas(pllcase_window)
        ca.draw()
        ca.getCanvas().pack()
        

        lb = tk.Listbox(pllcase_window, width = 50, height = 15)
        lb.pack(pady = 10)
        lb.bindtags((lb, pllcase_window, "all"))
        lb.config(font = ("Helvectia", 11, "bold"))

        for idx, elm in enumerate(df["algs"].iloc[ncase]):
            lb.insert(idx, " " + elm)
            if (idx % 2 == 0):
                lb.itemconfig(idx, bg = "#aaaaaa")
            else:
                lb.itemconfig(idx, bg = "#cccccc")