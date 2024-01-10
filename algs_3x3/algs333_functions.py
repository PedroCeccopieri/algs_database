import sys
sys.path.append('../')

import tkinter as tk
import random as rd

from puzzles.c333 import c333
from algs_3x3.oll_algs.oll333_functions import oll
from algs_3x3.pll_algs.pll333_functions import pll
from utils.menuIcons import MenuIcon
from utils.saveAndLoad import load

olldf = load("OLL333")
plldf = load("PLL333")

def algs333():
    
    algs333_window = tk.Toplevel()
    algs333_window.title("3x3 Algs")
    algs333_window.geometry('600x400+200+200')
    
    i = rd.randint(1, olldf.shape[0]-1)
    MenuIcon(algs333_window, "OLL", c333(150, 150, olldf["top"].iloc[i], olldf["side"].iloc[i]), 0, 0, command = oll).show()
    j = rd.randint(1, plldf.shape[0]-1)
    MenuIcon(algs333_window, "PLL", c333(150, 150, plldf["top"].iloc[j], plldf["side"].iloc[j]), 0, 1, command = pll).show()