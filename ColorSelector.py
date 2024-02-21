import tkinter as tk
import colorsys
import os
import sys
import numpy as np

def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

def hsv_to_rgb(h, s, v):
        """Convert HSV (Hue, Saturation, Value) color space to RGB (Red, Green, Blue)."""
        rgb = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h / 360, s / 100, v / 100))
        # rgb = [int((r + m)*255), int((g + m))*255, int((b + m)*255)]
        return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]), int(rgb[1]), int(rgb[2]))

class ColorWheel(tk.Frame):
    
    def __init__(self,master=None,**kwargs):
        super().__init__(master,**kwargs)
        self.image = tk.PhotoImage(file=resource_path("assets/Triangulo_HSV.png"))
        self.root = self
        self.generateWidgets()
        self.color = '#408080'
    def scaler(self,sliderX: tk.Scale,sliderEntryX: tk.Entry,sliderH,sliderS,sliderV,resultColorLabel):
        # global resultColorLabel
        sliderEntryX.configure(state="normal")
        sliderEntryX.delete(0,tk.END)
        sliderEntryX.insert(0,sliderX.get())
        sliderEntryX.config(state="readonly")
        self.color = hsv_to_rgb(sliderH.get(),sliderS.get(),sliderV.get())
        # print(color)
        resultColorLabel.config(bg=self.color)
    
    def getColor(self):
        return self.color

    def generateWidgets(self):
        label = tk.Label(self, image=self.image)

        labelH = tk.Label(self.root,text="Hue",font=("Verdana",20),pady=5)
        sliderH = tk.Scale(self.root,from_= 0, to=360, orient="horizontal",
                            width=20,length=360,showvalue=0,
                            command=lambda on_change:self.scaler(sliderH,sliderEntryH,
                                                                sliderH,sliderS,sliderV,resultColorLabel))
        sliderH.set(180)
        
        sliderEntryH = tk.Entry(self.root, width=5, font = ("Verdana",20),
                                justify="center", state="readonly",borderwidth=5)
        sliderEntryH.configure(state="normal")
        sliderEntryH.insert(0,sliderH.get())
        sliderEntryH.config(state="readonly")

        labelS = tk.Label(self.root,text="Saturation",font=("Verdana",20),pady=5)
        sliderS = tk.Scale(self.root,from_= 0, to=100, orient="horizontal",
                            width=20,length=360,showvalue=0,
                            command=lambda on_change:self.scaler(sliderS,sliderEntryS,
                                                            sliderH,sliderS,sliderV,resultColorLabel))
        sliderS.set(50)
        sliderEntryS = tk.Entry(self.root, width=5, font = ("Verdana",20),
                                justify="center", state="readonly",borderwidth=5)
        sliderEntryS.configure(state="normal")
        sliderEntryS.insert(0,sliderS.get())
        sliderEntryS.config(state="readonly")

        labelV = tk.Label(self.root,text="Value",font = ("Verdana",20))
        sliderV = tk.Scale(self.root,from_= 0, to=100, orient="horizontal",
                            width=20,length=360,showvalue=0,
                            command=lambda on_change:self.scaler(sliderV,sliderEntryV,
                                                                sliderH,sliderS,sliderV,resultColorLabel))
        sliderV.set(50)

        sliderEntryV = tk.Entry(self.root, width=5, font = ("Verdana",20),
                                justify="center", state="readonly",borderwidth=5)
        sliderEntryV.configure(state="normal")
        sliderEntryV.insert(0,sliderS.get())
        sliderEntryV.config(state="readonly")

        resultColorLabel = tk.Label(self.root, text="Result",font=("Verdana",20),pady=5, 
                                    bg=hsv_to_rgb(sliderH.get(),sliderS.get(),sliderV.get()))
        # root.grid_rowconfigure(7, weight=1)
        # root.grid_columnconfigure(0, weight=1)

        label.grid(row=0,column=0,rowspan=1, columnspan=2, sticky="nsew")
        # root.grid_rowconfigure(0, weight=1)
        # root.grid_columnconfigure(0, weight=1)
        labelH.grid(row=1,column=0,rowspan=1, columnspan=2, sticky="nsw")
        sliderH.grid(row=2,column=0)
        sliderEntryH.grid(row = 2, column = 1)
        labelS.grid(row=3,column=0,rowspan=1, columnspan=2, sticky="nsw")
        sliderS.grid(row=4,column=0)
        sliderEntryS.grid(row = 4, column = 1)
        labelV.grid(row=5,column=0,rowspan=1, columnspan=2, sticky="nsw")
        sliderV.grid(row=6,column=0)
        sliderEntryV.grid(row = 6, column = 1)
        resultColorLabel.grid(row=7,column=0, columnspan=2, sticky="nsew")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x1024")
    # testFrame = tk.LabelFrame(root)
    # testFrame.grid(row = 0, column=1,padx=30,pady = 32, ipadx=62, ipady=62)
    # frameLabel = tk.Label(testFrame,text="Inside frame",font=("Verdana",25))
    # frameLabel.grid(row=0,column=0)
    colorWidget = ColorWheel(root)
    colorWidget.grid(row=0,column=0)
    root.mainloop()
