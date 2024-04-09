from tkinter import*
from random import randint

def setAns():
    n = 0
    num = [0 for i in range(10)]
    while True:
        randNum = randint(0, 9)
        if num[randNum] < 10:
            ans.append(randNum)
            num[randNum] += 1
            if num[randNum] == 10: n += 1
        if n == 10:
            break

def press(k):
    global Titlee
    global pairs
    global preNum
    bt[k].config(state=DISABLED)
    if previous[1] == 0:
        previous[0] = k
        previous[1] += 1
    else:
        if bt[previous[0]]['text'] == bt[k]['text']:
            pairs -= 1
        else:
            bt[k].config(state=NORMAL)
            bt[previous[0]].config(state=NORMAL)
        print(bt[previous[0]]['text'], bt[k]['text'])
        previous[0] = -1
        previous[1] = 0
    Titlee.set(f'剩餘配對數:{pairs}')
    if pairs == 0:
        Titlee.set(f'剩餘配對數:{pairs}，恭喜獲勝')

# create a window
root = Tk()
root.title("homework")

# create varible
ans = []
setAns()
Titlee = StringVar()
bt = [0 for i in range(100)]
pairs = 50
previous = [-1, 0]
preNum = -1

# create label
Label(root, textvariable=Titlee, width=18, height=2, font="微軟正黑體 15").grid(column=0, row=10, columnspan=10)
Titlee.set(f'剩餘配對數:{pairs}')

# create button
k = 0
for i in range(10):
    for j in range(10):
        bt[k] = Button(root, width=6, text=str(ans[k]), height=3, font="微軟正黑體 9", \
            command=lambda k=k: press(k))
        bt[k].grid(row=i, column=j)
        k += 1

# execute
root.mainloop()