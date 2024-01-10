import tkinter as tk

import sys
sys.path.append('../')

from utils.colors import colors

class c333:
    def __init__(self, width, height, face, side):
        self.n = 3
        self.s = 4
        self.width = width
        self.height = height
        self.offx = 0.15 * self.width
        self.offy = 0.15 * self.height
        self.spacex = (self.width - 2 * self.offx)/self.n
        self.spacey = (self.height - 2 * self.offy)/self.n
        self.stroke = 0.015 * self.width
        self.face = face
        self.side = side

    def createCanvas(self, parent):
        self.parent = parent
        self.canvas = tk.Canvas(self.parent, width = self.width, height = self.height, bg = "#cccccc")

    def getCanvas(self):
        return self.canvas
    
    def setFace(self, face):
        self.face = face

    def setSide(self, side):
        self.side = side

    def getPointsFace(self):

        face = []

        for i in range(self.n):

            line = []

            for j in range(self.n):

                line.append([(self.offx + self.spacex * j, self.offy + self.spacey * i),
                (self.offx + self.spacex * (j+1), self.offy + self.spacey * i),
                (self.offx + self.spacex * (j+1), self.offy + self.spacey * (i+1)),
                (self.offx + self.spacex * j, self.offy + self.spacey * (i+1))])

            face.append(line)

        return face
    
    def getPointsSide(self):

        side = []

        for i in range(self.n):
            side.append([[(self.offx + self.spacex * i, self.offy-20), 
            (self.offx + self.spacex * (i+1), self.offy-20), 
            (self.offx + self.spacex * (i+1), self.offy),
            (self.offx + self.spacex * i, self.offy)],
            
            [(self.offx-20, self.offy + self.spacey * i), 
            (self.offx-20, self.offy + self.spacey * (i+1)), 
            (self.offx, self.offy + self.spacey * (i+1)), 
            (self.offx, self.offy + self.spacey * i)],

            [(self.width-self.offx+20, self.offy + self.spacey * i), 
             (self.width-self.offx+20, self.offy + self.spacey * (i+1)), 
             (self.width-self.offx, self.offy + self.spacey * (i+1)), 
             (self.width-self.offx, self.offy + self.spacey * i)],

             [(self.offx + self.spacex * i, self.height-self.offy+20), 
              (self.offx + self.spacex * (i+1), self.height-self.offy+20), 
              (self.offx + self.spacex * (i+1), self.height-self.offy),
              (self.offx + self.spacex * i, self.height-self.offy)]])
            
        return [j if (idx < 2) else [[k[-1]] + k[:len(k)-1] for k in j] for idx, j in enumerate([[side[0][i],side[1][i], side[2][i]] for i in range(self.s)])]
        
    def draw(self):

        self.canvas.delete("all")

        for i in range(self.n):
            for j in range(self.n):

                self.canvas.create_polygon((self.offx + self.spacex * j, self.offy + self.spacey * i), 
                                (self.offx + self.spacex * (j+1), self.offy + self.spacey * i), 
                                (self.offx + self.spacex * (j+1), self.offy + self.spacey * (i+1)), 
                                (self.offx + self.spacex * j, self.offy + self.spacey * (i+1)), 
                                fill = list(colors.values())[int(self.face[i][j])], 
                                outline = "#000000", 
                                width = self.stroke
                                )

        for i in range(self.n):

            self.canvas.create_polygon((self.offx + self.spacex * i, self.offy-20), 
                            (self.offx + self.spacex * (i+1), self.offy-20), 
                            (self.offx + self.spacex * (i+1), self.offy),
                            (self.offx + self.spacex * i, self.offy),
                            fill = list(colors.values())[int(self.side[0][i])], 
                            outline="#000000", 
                            width = self.stroke
                            )
            
            self.canvas.create_polygon((self.offx-20, self.offy + self.spacey * i), 
                            (self.offx-20, self.offy + self.spacey * (i+1)), 
                            (self.offx, self.offy + self.spacey * (i+1)), 
                            (self.offx, self.offy + self.spacey * i), 
                            fill = list(colors.values())[int(self.side[1][i])], 
                            outline="#000000", 
                            width = self.stroke
                            )

            self.canvas.create_polygon((self.width-self.offx+20, self.offy + self.spacey * i), 
                            (self.width-self.offx+20, self.offy + self.spacey * (i+1)), 
                            (self.width-self.offx, self.offy + self.spacey * (i+1)), 
                            (self.width-self.offx, self.offy + self.spacey * i), 
                            fill = list(colors.values())[int(self.side[2][i])], 
                            outline="#000000", 
                            width = self.stroke
                            )
            
            self.canvas.create_polygon((self.offx + self.spacex * i, self.height-self.offy+20), 
                            (self.offx + self.spacex * (i+1), self.height-self.offy+20), 
                            (self.offx + self.spacex * (i+1), self.height-self.offy),
                            (self.offx + self.spacex * i, self.height-self.offy),
                            fill = list(colors.values())[int(self.side[3][i])], 
                            outline="#000000", 
                            width = self.stroke
                            )