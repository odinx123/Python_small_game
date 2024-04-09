from tkinter import*

def press(i, j, k):
    global frequency
    global Titlee
    if checkerboard[i][j] != ' ': return
    if frequency % 2 == 0:
        checkerboard[i][j] = 'O'
        bt[k].config(text='O')
        playerWin = isWin(i, j, 'O')
    else:
        checkerboard[i][j] = 'X'
        bt[k].config(text='X')
        playerWin = isWin(i, j, 'X')
    if playerWin:
        Titlee.set("玩家"+str(frequency%2)+"獲得勝利")
        for b in bt:
            b.config(state=DISABLED)
        return
    if frequency == len(bt)-1:
        Titlee.set("平手")
        for b in bt:
            b.config(state=DISABLED)
        return
    frequency += 1
    Titlee.set("輪到玩家"+str(frequency%2))
    print(checkerboard)

def isWin(i, j, c):
    length = len(checkerboard[0])
    rowCount = columnCount =rightCount = leftCount = 0
    for pos in range(length):
        if checkerboard[i][pos] == c:
            columnCount += 1
        if checkerboard[pos][j] == c:
            rowCount += 1
        if checkerboard[pos][pos] == c:
            rightCount += 1
        if checkerboard[pos][length-pos-1] == c:
            leftCount += 1
    if rowCount == length or columnCount == length or rightCount == length or leftCount == length:
        return True
    return False

def changeDifficulty():
    global frequency
    global nef
    if nef == 6: return
    frequency = 0
    Size = len(checkerboard[0])
    lb.config(width=6*(Size+1))
    lb.grid(columnspan=Size+1)
    Titlee.set("遊戲開始!!請玩家0先下")

    for bu in bt: bu.destroy()
    [bt.append(0) for i in range(Size*2+1)]

    for i in range(Size):
        for j in range(Size):
            checkerboard[i][j] = ' '
    checkerboard.append([' ' for i in range(Size)])
    [checkerboard[i].append(' ') for i in range(Size+1)]

    print(checkerboard)
    k = 0
    for i in range(1, Size+2):  # 1 ~ 4
        for j in range(0, Size+1):  # 0 ~ 3
            bt[k] = Button(root, width=9, text=' ', height=4, font="微軟正黑體 9", \
                command=lambda i=i, j=j, k=k: press(i-1, j, k))
            bt[k].grid(row=i, column=j)
            k += 1
    nextB.grid(row=Size+2, column=Size)
    nextC.config(width=nextC['width']+10)
    nextC.grid(row=Size+2, column=0, columnspan=Size)
    nef += 1

def clear():
    global Titlee
    global frequency
    for i in checkerboard:
        for j in range(len(i)):
            i[j] = ' '
    for t in bt:
        t.config(text=' ')
        t.config(state=NORMAL)
    Titlee.set("遊戲開始!!請玩家0先下")
    frequency = 0
    print(checkerboard)

# create a window
root = Tk()
root.title("homework")

# declare varible
checkerboard = [[' ' for i in range(3)] for j in range(3)]
Titlee = StringVar()
frequency = 0
nef = 0
bt = [0 for i in range(9)]

#create label
lb = Label(root, textvariable=Titlee, width=18, height=2, font="微軟正黑體 15", bg="yellow")
lb.grid(column=0, row=0, columnspan=3)
Titlee.set("遊戲開始!!請玩家0先下")

# create button
k = 0
for i in range(1, 4):
    for j in range(0, 3):
        bt[k] = Button(root, width=9, text=' ', height=3, font="微軟正黑體 9", \
            command=lambda i=i, j=j, k=k: press(i-1, j, k))
        bt[k].grid(row=i, column=j)
        k += 1
nextB = Button(root, text='下一關', width=9, height=2, font="微軟正黑體 9", command=changeDifficulty)
nextB.grid(row=4, column=2)
nextC = Button(root, text='Restart', width=20, height=2, font="微軟正黑體 9", command=clear)
nextC.grid(row=4, column=0, columnspan=2)

# execute
root.mainloop()