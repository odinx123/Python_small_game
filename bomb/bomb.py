from cmath import nan
from threading import Timer
from tkinter import*
from random import randint  # for random bomb
from PIL import Image, ImageTk  # for image
from time import time

def press(pos, item):
    global t
    global Titlee
    global gameState
    if bt[pos]['image'] == str(flagsImg) or gameState: return
    if item != '💣':
        bt[pos].config(text=item)
        if checkerboard[pos] == ' ' and bt[pos]['bg'] != 'white':
            openMap(pos)
        bt[pos].config(bg='white')
    else:
        bt[pos].config(image=bombImg, bg='red')
        Titlee.set(f"game over, you use {int(time()-star)}s loss the game")
        t.cancel()
        gameState = 1
    if gameState: return
    openNum = 0
    for i in range(n*n):
        if bt[i]['bg'] == 'white': openNum += 1
    if openNum == n*n-n:
        gameState = 1
        for i in range(n*n):
            if checkerboard[i] == '💣' and bt[i]['image'] != str(flagsImg):
                bt[i].config(image=bombImg, bg='white')
            elif bt[i]['image'] != str(flagsImg):
                bt[i].config(text=checkerboard[i], bg='white')
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
    pos = randint(0, n*n-1)
    for i in range(n*n): checkerboard[i] = 0
    # set bomb
    for i in range(n):
        while checkerboard[pos] == '💣':
            pos = randint(0, n*n-1)
        checkerboard[pos] = '💣'
    # set Button and number
    for i in range(n*n):
        checkerboard[i] = bombNum(i) if checkerboard[i] != '💣' else '💣'
        if checkerboard[i] != '💣' and not checkerboard[i]: checkerboard[i] = ' '
        bt[i] = Button(root, text=' ', width=5, height=2, font="微軟正黑體 9", \
            bg='Chartreuse', command=lambda i=i: press(i, checkerboard[i]))
        bt[i].bind("<Button-3>", lambda event, i=i: setFlags(event, i))
        bt[i].grid(row=i//n+1, column=i%n, sticky='nswe')  # sticky='nwse'可以往上下左右填滿(解決長寬跟圖片的衝突)

def showMap():
    for i in range(n):
        for j in range(n):
            if checkerboard[i*n+j] != '💣':
                print(f'{checkerboard[i*n+j]:2}', end='')
            else:
                print(checkerboard[i*n+j], end='')
        print()

def isLegal(N):
    if N >= 0 and N < n*n:
        if checkerboard[N] == '💣':
            return True
    return False

def bombNum(i):
    leftUp = -n-1; rightUp = -n+1; midUp = -n; lef = -1
    leftDown = n-1; rightDown = n+1; midDown = n; rigt = 1;   bombN = 0
    if isLegal(i+leftUp) and checkerboard[i] != '💣' and (i+leftUp)%n != n-1:   bombN += 1
    if isLegal(i+rightUp) and checkerboard[i] != '💣' and (i+rightUp)%n != 0:   bombN += 1
    if isLegal(i+midUp) and checkerboard[i] != '💣':   bombN += 1
    if isLegal(i+lef) and checkerboard[i] != '💣' and (i+lef)%n != n-1:   bombN += 1
    if isLegal(i+rigt) and checkerboard[i] != '💣' and (i+rigt)%n != 0:   bombN += 1
    if isLegal(i+leftDown) and checkerboard[i] != '💣' and (i+leftDown)%n != n-1:   bombN += 1
    if isLegal(i+midDown) and checkerboard[i] != '💣':   bombN += 1
    if isLegal(i+rightDown) and checkerboard[i] != '💣' and (i+rightDown)%n != 0:   bombN += 1
    return bombN

def showTime():
    global t
    global Titlee
    if gameState: return
    t = Timer(0.1, showTime)
    Titlee.set(f'time: {int(time()-star):3}s,   flag: {fN}')
    t.start()

def start():
    global t
    global star
    global gameState
    star += 1
    gameState = 0
    t = Timer(0.1, showTime)
    t.start()

def delay(s):
    now = time()
    while time()-now <= s: continue

def openMap(pos):
    iUp = iDw = pos; f1 = f2 = fU = fD = 0; openBlockI = 2
    while True:
        if not isLegal(iUp) and iUp >= 0 and bt[iUp]['image'] != str(flagsImg) and not f1:
            if checkerboard[iUp] != ' ' and checkerboard[iUp] != '💣': f1 = 1
            lTouch = rTouch = False; touchNumTimesR = touchNumTimesL = 0
            bt[iUp].config(bg = 'white', text=checkerboard[iUp])
            for i in range(0, n//openBlockI):
                if (iUp + i < n*n) and not rTouch:
                    if bt[iUp+i]['image'] == str(flagsImg): rTouch = True
                    if not isLegal(iUp+i) and (iUp+i)//n == iUp//n:
                        if checkerboard[iUp+i] != ' ':
                            if touchNumTimesR: rTouch = True
                            touchNumTimesR = 1
                        if not rTouch: bt[iUp+i].config(text=checkerboard[iUp+i], bg = 'white')
                if (iUp - i >= 0) and not lTouch:
                    if bt[iUp-i]['image'] == str(flagsImg): lTouch = True
                    if not isLegal(iUp-i) and (iUp-i)//n == iUp//n:
                        if checkerboard[iUp-i] != ' ':
                            if touchNumTimesL: lTouch = True
                            touchNumTimesL = 1
                        if not lTouch: bt[iUp-i].config(text=checkerboard[iUp-i], bg = 'white')
                if rTouch and lTouch: break
            iUp -= n; fU += 1
            if fU >= n//openBlockI: f1 = 1
        else: f1 = 1
        touchNumTimesR = touchNumTimesL = 0
        if not isLegal(iDw) and iDw < n*n and bt[iDw]['image'] != str(flagsImg) and not f1:
            lTouch = rTouch = False
            if checkerboard[iDw] != ' ' and checkerboard[iDw] != '💣': f2 = 1
            bt[iDw].config(bg = 'white', text=checkerboard[iDw])
            for i in range(0, n//openBlockI):
                if (iDw + i < n*n) and not rTouch:
                    if bt[iDw+i]['image'] == str(flagsImg): rTouch = True
                    if not isLegal(iDw+i) and (iDw+i)//n == iDw//n:
                        if checkerboard[iDw+i] != ' ':
                            if touchNumTimesR: rTouch = True
                            touchNumTimesR = 1
                        if not rTouch: bt[iDw+i].config(text=checkerboard[iDw+i], bg = 'white')
                if (iDw - i >= 0) and not lTouch:
                    if bt[iDw-i]['image'] == str(flagsImg): lTouch = True
                    if not isLegal(iDw-i) and (iDw-i)//n == iDw//n:
                        if checkerboard[iDw-i] != ' ':
                            if touchNumTimesR: lTouch = True
                            touchNumTimesR = 1
                        if not lTouch: bt[iDw-i].config(text=checkerboard[iDw-i], bg = 'white')
                if lTouch and lTouch: break
            iDw += n; fD += 1
            if fD >= n//openBlockI: f2 = 1
        else: f2 = 1
        if f1 and f2: break

def restart():
    global fN
    global star
    global gameState
    gameState = 1
    fN = 0
    t = Timer(1, start)
    Titlee.set("GAME START")
    for i in range(n*n): bt[i].destroy()
    setMap()
    star = time()
    t.start()

# create a window
root = Tk()
root.title("homework")
root.geometry('+520+150')

# declare varible
n = 10
fN = 0
star = 0
gameState = 1
t = Timer(1, start)
checkerboard = [0 for i in range(n*n)]
Titlee = StringVar(value='GAME START')
bt = [0 for i in range(n*n)]
img = Image.open('D:\programfile\Python\\bomb\\bomb.png').resize((25, 25), Image.ANTIALIAS) # 調整大小&抗鋸齒
bombImg = ImageTk.PhotoImage(img)
img = Image.open('D:\programfile\Python\\bomb\\flags.png').resize((25, 25), Image.ANTIALIAS) # 調整大小&抗鋸齒
flagsImg = ImageTk.PhotoImage(img)

#create label
lb = Label(root, textvariable=Titlee, width=int(3.8*n), height=1, font="微軟正黑體 15", bg='skyBlue')
lb.grid(column=0, row=0, columnspan=n)

# create MenuButton
menu = Menu(root)
menu.add_command(label='重新開始', command=restart)

# initialize game
setMap()
showMap()

# execute
t.start()
star = time()
root.config(menu=menu)
root.mainloop()