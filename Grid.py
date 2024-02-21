import tkinter as tk
from math import ceil
from PIL import Image, ImageTk
import io
from ColorSelector import ColorWheel

root = tk.Tk()
CANV_WIDTH = 500
CANV_HEIGHT = 500
root.resizable(False, False)
canvas = tk.Canvas(root, bg="white", width=CANV_WIDTH, height=CANV_HEIGHT)
canvas.grid(row=0,column=0)

coords = {"x":0,"y":0,"x2":0,"y2":0}
# keep a reference to all lines by keeping them in a list 
lines = []
xDiv = 20
yDiv = 20
def create_grid(xDiv:int = 5,yDiv:int = 5):
    for i in range(xDiv):
        canvas.create_line(CANV_WIDTH//xDiv*i,0,CANV_WIDTH//xDiv*i, CANV_HEIGHT)
    for i in range(yDiv):
        canvas.create_line(0,CANV_HEIGHT//yDiv*i,CANV_WIDTH, CANV_HEIGHT//yDiv*i)

create_grid(xDiv,yDiv)

colorWheelFrame = tk.Frame(root)
colorWheelFrame.grid(row=0,column=1)
colorWheel = ColorWheel(colorWheelFrame)
colorWheel.grid(row=0,column = 0)

def click(e):
    global colorWheel
    # define start point for line
    coords["x"] = e.x
    coords["y"] = e.y
    tamDivX = (CANV_WIDTH/xDiv)
    tamDivY = (CANV_HEIGHT/yDiv)

    
    canvas.create_rectangle(tamDivX*(e.x//tamDivX), tamDivY*(e.y//tamDivY), 
                            tamDivX*ceil(e.x/tamDivX), tamDivY*ceil(e.y/tamDivY), width=1,
                            fill=colorWheel.getColor())
    # create a line on this point and store it in the list
    # lines.append(canvas.create_line(coords["x"],coords["y"],coords["x"],coords["y"]))

def drag(e):
    # update the coordinates from the event
    coords["x2"] = e.x
    coords["y2"] = e.y

    # Change the coordinates of the last created line to the new coordinates
    canvas.coords(lines[-1], coords["x"],coords["y"],coords["x2"],coords["y2"])

def save_canvas_as_image(canvas, filename):
    # PostScript representation of the canvas
    ps = canvas.postscript(colormode='color')

    # Convert to PIL Image
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    
    # Save the image
    img.save(filename)

canvas.bind("<ButtonPress-1>", click)
# canvas.bind("<B1-Motion>", drag) 

saveButton = tk.Button(root, text="Save Canvas",
                        command=lambda: save_canvas_as_image(canvas, "canvas_image.png"),
                        font=('Verdana',20))
saveButton.grid(row=1,column=0)

root.mainloop()