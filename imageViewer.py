from tkinter import *
from PIL import Image, ImageTk
import os

screen = Tk()
screen.geometry('600x600')
screen.title('Images  Viewer')

def resize_image(event):
    new_height = 600
    new_width = 600
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    labe1.config(image=photo)
    labe1.image = photo

def next_image():
    global n, copy_of_image
    n += 1
    if n >= len(all_images):
        n = 0  
    img = all_images[n]
    image = Image.open('./images/' + img)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    labe1.config(image=photo)
    labe1.image = photo

def previous_image():
    global n, copy_of_image
    n -= 1
    if n < 0:
        n = len(all_images)
    img = all_images[n]
    image = Image.open('./images/' + img)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    labe1.config(image=photo)
    labe1.image = photo

n = 0
all_images = os.listdir('images')
if not all_images:
    raise Exception("No images found in the 'images' directory")
img = all_images[n]

image = Image.open('./images/' + img)
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
labe1 = Label(screen, image=photo)
labe1.bind('<Configure>', resize_image)
labe1.pack(fill=BOTH, expand=YES)

next_button = Button(screen, text='>>', width=5, height=2, command=next_image)
next_button.place(x=560, y=150)

previous_button = Button(screen, text='<<', width=5, height=2, command=previous_image)
previous_button.place(x=0, y=150)

screen.mainloop()
