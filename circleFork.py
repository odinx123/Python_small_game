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
    print(frequency)
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
        if checkerboard[pos][2-pos] == c:
            leftCount += 1
    if rowCount == length or columnCount == length or rightCount == length or leftCount == length:
        return True
    return False

# create a window
root = Tk()
root.title("homework")

# declare varible
checkerboard = [[' ' for i in range(3)] for j in range(3)]
Titlee = StringVar()
frequency = 0
bt = [0]*9

# create label
Label(root, textvariable=Titlee, width=18, height=2, font="微軟正黑體 15", bg="yellow").grid(column=0, row=0, columnspan=3)
Titlee.set("遊戲開始!!請玩家0先下")

# create button
k = 0
for i in range(1, 4):
    for j in range(0, 3):
        bt[k] = Button(root, width=9, text=' ', height=4, font="微軟正黑體 9", \
            command=lambda i=i, j=j, k=k: press(i-1, j, k))
        bt[k].grid(row=i, column=j)
        k += 1

# execute
root.mainloop()