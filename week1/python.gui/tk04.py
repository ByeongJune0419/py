from tkinter import *
from PIL import Image, ImageTk

# pip install pillow

app = Tk()
canvas = Canvas(app, width=400, height=400)
canvas.pack()

x = 20
y = 30
tk_tiger = None

def create_img(canvas):
    global tk_tiger
    img = Image.open('tiger.png')
    img = img.resize((50, 50)) # 사이즈 조정
    tk_tiger = ImageTk.PhotoImage(img)
    canvas.create_image(100, 350, image=tk_tiger, tag='tiger')

def move_right(event):
    canvas.move('tiger', x, 0)
    canvas.after(100)
    canvas.update()

def move_left(event):
    canvas.move('tiger', -x, 0)
    canvas.after(100)
    canvas.update()

def move_up(event):
    canvas.move('tiger', 0, -y)
    canvas.after(100)
    canvas.update()

def move_down(event):
    canvas.move('tiger', 0, y)
    canvas.after(100)
    canvas.update()

def move_space(event):
    canvas.move('tiger', 0, -100)
    canvas.after(100)
    canvas.update()

create_img(canvas)
canvas.bind('<Right>', move_right)
canvas.bind('<Left>', move_left)
canvas.bind('<Up>', move_up)
canvas.bind('<Down>', move_down)
canvas.bind('<space>', move_space)
canvas.focus_set()
app.mainloop()
