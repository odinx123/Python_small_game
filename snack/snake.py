from tkinter import*
from random import randint
from threading import Timer

def setMap():
    for i in range(height):
        for j in range(width):
            bt.append(Button(root, bg='Chartreuse', width=2))
            bt[i*width+j].grid(row=i+1, column=j)

def getXYPos(pos):
    return [pos%width, pos//width]

def getPos(x, y):
    pos = y*width + x
    return pos if pos >= 0 and pos < listLength else -1

def getUpPos(pos):
    xy = getXYPos(pos)
    return getPos(xy[0], xy[1] - 1)

def getDownPos(pos):
    xy = getXYPos(pos)
    return getPos(xy[0], xy[1] + 1)

def getRightPos(pos):
    xy = getXYPos(pos)
    return getPos(xy[0] + 1, xy[1]) if xy[0] + 1 < width else -1

def getLeftPos(pos):
    xy = getXYPos(pos)
    return getPos(xy[0] - 1, xy[1]) if xy[0] - 1 >= 0 else -1

def initScack():
    global previousPos
    snack.clear()
    snack.append(width//2+height//2*width)
    previousPos = snack[-1]
    bt[snack[0]].config(bg='yellow', text='⛋')

def moveSnack(event):
    global direction, unit, fs
    key = event.keysym
    if key == 'Up' or key == 'w':
        direction = 'y'
        unit = 1
    elif key == 'Down' or key == 's':
        direction = 'y'
        unit = -1
    elif key == 'Left' or key == 'a':
        direction = 'x'
        unit = -1
    elif key == 'Right' or key == 'd':
        direction = 'x'
        unit = 1
    if not fs: Move()
    fs = True

def Move():
    global tm, previousPos, score, game, sc, time
    if not game: return
    tm.cancel()
    tm = Timer(time, Move)

    previousPos = snack[-1]
    bt[previousPos].config(bg='Chartreuse', text=' ')
    for i in range(len(snack)-1, 0, -1):
        snack[i] = snack[i-1]
        bt[snack[i]].config(bg='yellow', text=' ')

    newPos = 0
    if direction == 'x':
        newPos = getRightPos(snack[0]) if unit == 1 else getLeftPos(snack[0])
    elif direction == 'y':
        newPos = getUpPos(snack[0]) if unit == 1 else getDownPos(snack[0])

    snack[0] = newPos
    if newPos == -1 or newPos in snack[1:] or newPos == previousPos:
        score.set(f'game over ! ! !, score: {sc}')
        game = False
        return
    bt[newPos].config(bg='yellow', text='⛋')

    if newPos == applePos:
        sc += 1
        score.set(f'score: {sc}')
        time *= 0.9
        snack.append(previousPos)
        bt[previousPos].config(bg='yellow')
        randAppleSet()

    tm.start()

def randAppleSet():
    global applePos
    while True:
        applePos = randint(0, listLength-1)
        if applePos not in snack:
            bt[applePos].config(text='🍎', bg='red')
            return

def reset():
    global sc, score, time, game, fs
    fs = False
    game = True
    time = 0.5
    sc = 0
    score.set(f'score: {sc}')
    for i in range(len(bt)): bt[i].destroy()
    bt.clear()
    setMap()
    initScack()
    randAppleSet()

# create windows
root = Tk()
root.title("HomeWork")

# create variable
game = True
fs = False
bt = []
width = 31
height = 21
listLength = width*height
snack = []
previousPos = 0
applePos = 0
score = StringVar(value='score: 0')
operate = ['w', 'a', 's', 'd', '<Left>', '<Up>', '<Right>', '<Down>']
time = 0.5
tm = Timer(time, Move)
direction = ''
unit = 0
sc = 0

# create label
Label(root, textvariable=score, font="微軟正黑體 15").grid(row=0, column=0, columnspan=width)

# create Button
for i in range(len(operate)):
    root.bind(operate[i], moveSnack)

# initial game
menu = Menu(root)
menu.add_command(label='重新開始', font="標楷體", command=reset)
root.config(menu=menu)
setMap()
initScack()
randAppleSet()

# game start
root.mainloop()