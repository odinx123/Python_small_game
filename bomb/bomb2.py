from threading import Timer
from tkinter import*
from random import randint  # for random bomb
from PIL import Image, ImageTk  # for image
from time import time
import os
import queue

from pyparsing import col

def openMap(pos):
    q = queue.Queue()
    hash = [False for i in range(height*width)]
    q.put_nowait(pos)
    hash[pos] = True
    while True:
        position = q.get_nowait()
        if bt[position]['image'] != str(flagsImg):
            bt[position].config(bg='white', text=bombMap[position])
        if getLeftPos(position) != NONE and bombMap[position] == ' ':
            if not hash[getLeftPos(position)]:
                q.put_nowait(getLeftPos(position))
                hash[getLeftPos(position)] = True
        if getRightPos(position) != NONE and bombMap[position] == ' ':
            if not hash[getRightPos(position)]:
                q.put_nowait(getRightPos(position))
                hash[getRightPos(position)] = True
        if getUpPos(position) != NONE and bombMap[position] == ' ':
            if not hash[getUpPos(position)]:
                q.put_nowait(getUpPos(position))
                hash[getUpPos(position)] = True
        if getDownPos(position) != NONE and bombMap[position] == ' ':
            if not hash[getDownPos(position)]:
                q.put_nowait(getDownPos(position))
                hash[getDownPos(position)] = True
        if getLeftUpPos(position) != NONE and bombMap[position] == ' ':
            if not hash[getLeftUpPos(position)] and bombMap[getLeftUpPos(position)] != ' ':
                q.put_nowait(getLeftUpPos(position))
                hash[getLeftUpPos(position)] = True
        if getRightUpPos(position) != NONE and bombMap[position] == ' ':
            if not hash[getRightUpPos(position)] and bombMap[getRightUpPos(position)] != ' ':
                q.put_nowait(getRightUpPos(position))
                hash[getRightUpPos(position)] = True
        if getLeftDownPos(position) != NONE and bombMap[position] == ' ':
            if not hash[getLeftDownPos(position)] and bombMap[getLeftDownPos(position)] != ' ':
                q.put_nowait(getLeftDownPos(position))
                hash[getLeftDownPos(position)] = True
        if getRightDownPos(position) != NONE and bombMap[position] == ' ':
            if not hash[getRightDownPos(position)] and bombMap[getRightDownPos(position)] != ' ':
                q.put_nowait(getRightDownPos(position))
                hash[getRightDownPos(position)] = True
        if q.empty(): break

def getLeftPos(pos):
    if (pos-1)%width != width-1 and pos - 1 >= 0:
        return pos - 1
    return NONE

def getRightPos(pos):
    if (pos+1)%width != 0 and pos + 1 < height*width:
        return pos + 1
    return NONE

def getDownPos(pos):
    if pos + width < height*width:
        return pos + width
    return NONE

def getUpPos(pos):
    if pos - width >= 0:
        return pos - width
    return NONE

def getLeftUpPos(pos):
    upPos = getUpPos(pos)
    if upPos == NONE: return NONE
    if (upPos - 1)%width == width-1 or upPos - 1 < 0:return NONE
    return upPos - 1

def getRightUpPos(pos):
    upPos = getUpPos(pos)
    if upPos == NONE: return NONE
    if (upPos + 1)%width == 0: return NONE
    return upPos + 1

def getLeftDownPos(pos):
    downPos = getDownPos(pos)
    if downPos == NONE: return NONE
    if (downPos-1)%width == width-1: return NONE
    return downPos - 1

def getRightDownPos(pos):
    downPos = getDownPos(pos)
    if downPos == NONE: return NONE
    if (downPos+1)%width == 0 or downPos+1 >= height*width: return NONE
    return downPos + 1

def press(pos, item):
    global t
    global Titlee
    global gameState
    if bt[pos]['image'] == str(flagsImg) or gameState: return
    if item != '💣':
        bt[pos].config(text=item)
        if bombMap[pos] == ' ' and bt[pos]['bg'] != 'white':
            openMap(pos)
        bt[pos].config(bg='white')
    else:
        bt[pos].config(bg='red', image=bombImg)
        Titlee.set(f"game over, you use {int(time()-star)}s loss the game")
        t.cancel()
        gameState = 1
    if gameState: return
    openNum = 0
    for i in range(height*width):
        if bt[i]['bg'] == 'white': openNum += 1
    if openNum == height*width-n:
        gameState = 1
        for i in range(height*width):
            if bombMap[i] == '💣':
                bt[i].config(image=bombImg, bg='Chartreuse')
        t.cancel()
        Titlee.set(f"you win in {int(time()-star)}s!!!")

def setFlags(event, pos):
    global fN
    global t
    global Titlee
    global gameState
    if gameState: return
    if event.widget['image'] == '' and event.widget['text'] == ' ':
        fN += 1
        event.widget.config(image=flagsImg)
    elif event.widget['image'] == str(flagsImg):  # event回傳的是字串
        event.widget.config(image='')  # ''可以將圖片消除
        fN -= 1

def setMap():
    pos = randint(0, height*width-1)
    for i in range(height*width): bombMap[i] = 0
    # set bomb
    for i in range(n):
        while bombMap[pos] == '💣':
            pos = randint(0, height*width-1)
        bombMap[pos] = '💣'
    # set Button and number
    for i in range(height*width):
        bombMap[i] = bombNum(i) if bombMap[i] != '💣' else '💣'
        if bombMap[i] != '💣' and not bombMap[i]: bombMap[i] = ' '
        bt[i] = Button(root, text=' ', width=5, height=2, font="微軟正黑體 9", \
            bg='Chartreuse', command=lambda i=i: press(i, bombMap[i]))
        bt[i].bind("<Button-3>", lambda event, i=i: setFlags(event, i))
        bt[i].grid(row=i//width+1, column=i%width, sticky='nswe')  # sticky='nwse'可以往上下左右填滿(解決長寬跟圖片的衝突)

def showMap():
    print('='*width*2+'==')
    for i in range(height):
        print("|", end='')
        for j in range(width):
            if bombMap[i*width+j] != '💣':
                print(f'{bombMap[i*width+j]:2}', end='')
            else:
                print(f'{bombMap[i*width+j]}', end='')
        print("|")
    print('='*width*2+'==')

def isLegal(N):
    if N >= 0 and N < height*width:
        if bombMap[N] == '💣':
            return True
    return False

def bombNum(i):
    leftUp = -width-1; rightUp = -width+1; midUp = -width; lef = -1
    leftDown = width-1; rightDown = width+1; midDown = width; rigt = 1;   bombN = 0
    if isLegal(i+leftUp) and bombMap[i] != '💣' and (i+leftUp)%width != width-1:   bombN += 1
    if isLegal(i+rightUp) and bombMap[i] != '💣' and (i+rightUp)%width != 0:   bombN += 1
    if isLegal(i+midUp) and bombMap[i] != '💣':   bombN += 1
    if isLegal(i+lef) and bombMap[i] != '💣' and (i+lef)%width != width-1:   bombN += 1
    if isLegal(i+rigt) and bombMap[i] != '💣' and (i+rigt)%width != 0:   bombN += 1
    if isLegal(i+leftDown) and bombMap[i] != '💣' and (i+leftDown)%width != width-1:   bombN += 1
    if isLegal(i+midDown) and bombMap[i] != '💣':   bombN += 1
    if isLegal(i+rightDown) and bombMap[i] != '💣' and (i+rightDown)%width != 0:   bombN += 1
    return bombN

def showTime():
    global t
    global Titlee
    if gameState: return
    t = Timer(0.1, showTime)
    Titlee.set(f'time: {int(time()-star):3}s,\t\t\t\tflag: {fN}')
    t.start()

def start():
    global t
    global star
    global gameState
    star += 1
    gameState = 0
    t = Timer(0.1, showTime)
    t.start()

def restart():
    global fN
    global star
    global gameState
    gameState = 1
    fN = 0
    t = Timer(1, start)
    Titlee.set("GAME START")
    for i in range(height*width): bt[i].destroy()
    setMap()
    showMap()
    star = time()
    t.start()

# create a window
root = Tk()
root.title("homework")
root.geometry('+520+150')

# declare varible
height = 10
width = 20
path = os.path.split(os.path.abspath(__file__))[0]
print(path)
n = width*height//7
fN = 0
star = 0
gameState = 1
t = Timer(1, start)
bombMap = [0 for i in range(height*width)]
Titlee = StringVar(value='GAME START')
bt = [0 for i in range(height*width)]
img = Image.open(f'{path}\\bomb.png').resize((25, 25), Image.ANTIALIAS)
bombImg = ImageTk.PhotoImage(img)
img = Image.open(f'{path}\\flags.png').resize((25, 25), Image.ANTIALIAS)
flagsImg = ImageTk.PhotoImage(img)

#create label
lb = Label(root, textvariable=Titlee, width=int(3.8*width), height=1, font="微軟正黑體 15", bg='skyBlue')
lb.grid(column=0, row=0, columnspan=width)

# create MenuButton
menu = Menu(root)
menu.add_command(label='重新開始', font="標楷體", command=restart)
# Button(root, text='重新開始', command=restart).grid(row=0, column=0)

# initialize game
setMap()
showMap()
t.start()
star = time()
root.config(menu=menu)

# execute
root.mainloop()