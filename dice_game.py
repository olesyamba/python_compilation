import random
import time
from tkinter import *
import sys
from PIL import ImageTk, Image
import pip as pip


def bros():
    x = random.choice(['Dice_1.PNG', 'Dice_2.PNG', 'Dice_3.PNG',
                       'Dice_4.PNG', 'Dice_5.PNG', 'Dice_6.PNG'])
    return x


def img(event):
    global b1, b2
    for i in range(18):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.12)


root = Tk()
root.title('Игра в кости. Сделай бросок!')
root.iconphoto(True, PhotoImage(file='iconka.PNG'))
font = PhotoImage(file='Dice/image.PNG')
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind('<1>', img)
img('event')
root.mainloop()
