from tkinter import*
from random import randint
from threading import Timer

def press():
    global frequency, t
    t.cancel()
    frequency = 0.00000000001
    t = Timer(frequency, change, [randint(0, fruitNum-1)])
    for i in range(fruitNum):
        lb[i].config(bg="white")
    t.start()

def change(pos):
    global frequency, t
    if frequency > 1:
        t.cancel()
        return
    lb[pos].config(bg='red')
    lb[pos-1 if pos - 1 >= 0 else fruitNum-1].config(bg='white')
    pos = (pos + 1) if (pos+1) < fruitNum else 0
    frequency *= 1.2
    t = Timer(frequency, change, [pos])
    t.start()

# create a window
root = Tk()
root.title("homework")

# declare varible
width = 7
height = 7
fruitNum = width * 2 + (height-2) * 2
frequency = 0.00000000001
t = Timer(frequency, change)
lb = [0 for i in range(fruitNum)]
fruImg = [0 for i in range(8)]
fruImg[0] = PhotoImage(file='D:\programfile\Python\\randFruit\\apple.png')
fruImg[1] = PhotoImage(file='D:\programfile\Python\\randFruit\\betelnut.png')
fruImg[2] = PhotoImage(file='D:\programfile\Python\\randFruit\\double7.png')
fruImg[3] = PhotoImage(file='D:\programfile\Python\\randFruit\\grape.png')
fruImg[4] = PhotoImage(file='D:\programfile\Python\\randFruit\\orange.png')
fruImg[5] = PhotoImage(file='D:\programfile\Python\\randFruit\\ring.png')
fruImg[6] = PhotoImage(file='D:\programfile\Python\\randFruit\\star.png')
fruImg[7] = PhotoImage(file='D:\programfile\Python\\randFruit\\watermelon.png')

# 0~6  7~12  13~17  18~23
#create label
k = 0
for i in range(height):
    for j in range(width):
        if i == 0:
            lb[j] = Label(root, image=fruImg[randint(0, 7)], bg='white')
            lb[j].grid(row=i, column=j, sticky='nswe')
        elif j == width - 1:
            lb[width-1+i] = Label(root, image=fruImg[randint(0, 7)], bg='white')
            lb[width-1+i].grid(row=i, column=j, sticky='nswe')
        elif j == 0:
            num = width * 2 + (height-2) * 2
            lb[num-i] = Label(root, image=fruImg[randint(0, 7)], bg='white')
            lb[num-i].grid(row=i, column=j, sticky='nswe')
        elif i == height - 1:
            num = width * 2 - 1 + height - 2
            lb[num-j] = Label(root, image=fruImg[randint(0, 7)], bg='white')
            lb[num-j].grid(row=i, column=j, sticky='nswe')

# create Button
bt = Button(root, bg='Chartreuse', command=press, text='Go', font="微軟正黑體 9")
bt.grid(row=height//2, column=width//2, sticky='nswe')

# execute
root.mainloop()