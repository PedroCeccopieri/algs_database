import tkinter as tk
import pandas as pd
import copy as cp

from puzzles.c333 import c333
from utils.colors import colors
from utils.saveAndLoad import save, load

def redraw():
    print("redraw")

    c3.setFace(topColors)
    c3.setSide(sideColors)
    c3.draw()

def paint(event):
    print("paint", event)

    for idxi, i in enumerate(face):
        for idxj, j in enumerate(i):
            if (j[0][0] <= event.x <= j[2][0] and j[0][1] <= event.y <= j[2][1]):
                topColors[idxi][idxj] = currentColor

    for idxi, i in enumerate(side):
        for idxj, j in enumerate(i):
            if (j[0][0] <= event.x <= j[2][0] and j[0][1] <= event.y <= j[2][1]):
                sideColors[idxi][idxj] = currentColor

    redraw()

def setColor(color):
    print("setColor", color)

    global currentColor
    currentColor = color

def saveCase(case):
    print("saveCase", case)
    global df

    names = df["name"]
    add = False

    if not (names.empty):
        if not (str(case) in [str(i) for i in list(names)]):
            add = True
        else:
            df.loc[df["name"] == case, "top"] = [cp.deepcopy(topColors)]
            df.loc[df["name"] == case, "side"] = [cp.deepcopy(sideColors)]
    else:
        add = True
    
    if (case and add):
        newRow = {"name": [case], "top": [cp.deepcopy(topColors)], "side": [cp.deepcopy(sideColors)], "algs": [[]]}
        df = pd.concat([df,pd.DataFrame(newRow)], ignore_index = True)
    else:
        print("No case name given")

    reloadCases()

def loadCases(file):
    print("loadCases", file)

    global df

    df = load(file)

    for idx, row in df.iterrows():
        print(type(row["top"]))

    reloadCases()

def reloadCases():
    print("reloadCases")

    global caseSelected

    lstbox1.delete(0,tk.END)
    lstbox2.delete(0,tk.END)

    if not (df.empty):
        for index, row in df.iterrows():
            lstbox1.insert(tk.END, row["name"])
    else:
        print("df is empty")

    caseSelected = None

def deleteCase(case):
    print("deleteCase", case)
    
    global df

    if (case != None):
        df = df.drop(df.loc[df["name"] == case].index)
        reloadCases()
    else:
        print("No case selected")

def loadCaseImage(case):
    print("loadCaseImage", case)

    global topColors, sideColors

    topColors = cp.deepcopy(df.loc[df["name"] == case]["top"].iloc[0])
    sideColors = cp.deepcopy(df.loc[df["name"] == case]["side"].iloc[0])
    redraw()

def saveCases(file):
    print("saveCases", file)

    if (file):
        save(df, file)
    else:
        print("No file name given")

def loadAlgs(case):
    print("loadAlgs", case)

    global lstbox2

    lstbox2.delete(0,tk.END)

    for a in df.loc[df["name"] == case]["algs"].iloc[0]:
        lstbox2.insert(tk.END, a)

def addAlg(case, alg):
    print("addAlg", case, alg)

    if (case != None):
        if (alg):
            df.loc[df["name"] == case]["algs"].iloc[0].append(alg)
            loadAlgs(case)
        else:
            print("No alg to add")
    else:
        print("No case selected")

def deleteAlg(case, alg):
    print("deleteAlg", case, alg)

    if (case != None):
        if (alg):
            df.loc[df["name"] == case]["algs"].iloc[0].remove(alg)
            loadAlgs(case)
        else:
            print("No alg selected")
    else:
        print("No case selected")

    reloadCases()

def selectCase(listbox):
    print("selectCase", listbox)

    global caseSelected

    caseSelected = getSelected(listbox)

    if (caseSelected != None):
        loadAlgs(caseSelected)
        loadCaseImage(caseSelected)
    else:
        print("No case selected")

def getSelected(listbox):
    print("getSelected", listbox)

    selected_indices = listbox.curselection()
    if (selected_indices):
        return listbox.get(selected_indices[0])
    else:
        return None

root = tk.Tk()
root.title("editor")
root.geometry('1400x800+100+0')
root.bind_all("<Button-1>", lambda event: event.widget.focus())

topColors = [[0,0,0],[0,0,0],[0,0,0]]
sideColors = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
currentColor = 0
caseSelected = None

df = pd.DataFrame(columns = ['name','top', 'side', 'algs']).astype({'name': 'string','top': 'object', 'side': 'object', 'algs': 'object'})

width = 400
height = 300

# ================================================ #

frame1 = tk.LabelFrame(root, width = width, height = height, text = "Case editor")
frame1.grid(row = 0, column = 0, padx = 10)

frame11 = tk.Frame(frame1)
frame11.grid(row = 0, column = 0, padx = 5, pady = 5)

lb1 = tk.Label(frame11, text = "Case name:")
lb1.grid(row = 0, column = 0, padx = 5, pady = 5)

txtbox1 = tk.Entry(frame11, takefocus = 0)
txtbox1.grid(row = 0, column = 1, pady = 5)

c3 = c333(300,300, topColors, sideColors)
c3.createCanvas(frame1)
puzzle = c3.getCanvas()
puzzle.bind('<Button-1>', paint)
puzzle.grid(row = 1, column = 0, pady = 5)

c3.draw()
face = c3.getPointsFace()
side = c3.getPointsSide()

tk.Button(frame1, text = "Save case", width = 20, font = ("Helvectia", 14), command = lambda: saveCase(txtbox1.get())).grid(row = 2, column = 0, pady = 5)

# ================================================ #

frame2 = tk.LabelFrame(root, width = width, height = height, text = "Colors")
frame2.grid(row = 0, column = 1, padx = 10)

for idx, (name, color) in enumerate(colors.items()):
    tk.Button(frame2, text = name, fg = "#000000", bg = color, width = 20, font = ("Helvectia", 14), command = lambda x = idx: setColor(x)).pack()

# ================================================ #

frame3 = tk.LabelFrame(root, width = width, height = height, text = "Cases")
frame3.grid(row = 0, column = 2, padx = 10)

frame31 = tk.Frame(frame3)
frame31.grid(row = 0, column = 0)

frame32 = tk.Frame(frame3)
frame32.grid(row = 1, column = 0, pady = 5)

lb2 = tk.Label(frame31, text = "File name:")
lb2.grid(row = 0, column = 0, padx = 5, pady = 5)

txtbox2 = tk.Entry(frame31, takefocus = 0)
txtbox2.grid(row = 0, column = 1)

tk.Button(frame32, text = "Load File", width = 20, font = ("Helvectia", 14), command = lambda: loadCases(txtbox2.get())).grid(row = 0, column = 0, pady = 5)
tk.Button(frame32, text = "Save File", width = 20, font = ("Helvectia", 14), command = lambda: saveCases(txtbox2.get())).grid(row = 1, column = 0)

lstbox1 = tk.Listbox(frame3, width = 35, height = 20)
lstbox1.grid(row = 2, column = 0, pady = 5)

tk.Button(frame3, text = "Choose case", width = 20, font = ("Helvectia", 14), command = lambda: selectCase(lstbox1)).grid(row = 3, column = 0, pady = 5)
tk.Button(frame3, text = "Delete case", width = 20, font = ("Helvectia", 14), command = lambda: deleteCase(getSelected(lstbox1))).grid(row = 4, column = 0, pady = 5)

# ================================================ #

frame4 = tk.LabelFrame(root, width = width, height = height, text = "Algs")
frame4.grid(row = 0, column = 3, padx = 10)

frame41 = tk.Frame(frame4)
frame41.grid(row = 0, column = 0, pady = 5)

lb3 = tk.Label(frame41, text = "Alg:")
lb3.grid(row = 0, column = 0, padx = 5, pady = 5)

txtbox3 = tk.Entry(frame41, takefocus = 0)
txtbox3.grid(row = 0, column = 1, pady = 5)

lstbox2 = tk.Listbox(frame4, width = 35, height = 20)
lstbox2.grid(row = 1, column = 0, pady = 5)

tk.Button(frame4, text = "Add alg", width = 20, font = ("Helvectia", 14), command = lambda: addAlg(caseSelected, txtbox3.get())).grid(row = 2, column = 0, pady = 5)
tk.Button(frame4, text = "Delete alg", width = 20, font = ("Helvectia", 14), command = lambda: deleteAlg(caseSelected, getSelected(lstbox2))).grid(row = 3, column = 0, pady = 5)

# ================================================ #

def updateLabel():
    lb01['text'] = str(topColors)
    lb02['text'] = str(sideColors)
    lb03['text'] = str(currentColor)
    lb04['text'] = str(caseSelected)
    lb05['text'] = str(df)
    root.after(100, updateLabel)


frame0 = tk.LabelFrame(root, width = width, height = height, text = "Case editor")
frame0.grid(row = 0, column = 5, padx = 10)

lb01 = tk.Label(frame0, text = str(topColors))
lb02 = tk.Label(frame0, text = str(sideColors))
lb03 = tk.Label(frame0, text = str(currentColor))
lb04 = tk.Label(frame0, text = str(caseSelected))
lb05 = tk.Label(frame0, text = str(df))

lb01.pack()
lb02.pack()
lb03.pack()
lb04.pack()
lb05.pack()

# ================================================ #

updateLabel()
root.mainloop()