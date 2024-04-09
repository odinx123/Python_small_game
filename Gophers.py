from tkinter import*
from random import randint
from threading import Timer

def setAns():
    global Gophers
    global GophersNum
    Gophers = randint(2, 20)
    for i in range(100):
        ans[i] = ' '
    for i in range(Gophers):
        ans[randint(0, 99)] = 'o'
    GophersNum.set(f'地鼠數量: {Gophers}')

def press(k):
    global GophersNum
    global scopeNum
    global scope
    global Gophers
    if bt[k]['text'] == 'o':
        scope += 1
        scopeNum.set(f'總分: {scope}')
        bt[k].config(text=' ')
        ans[k] = ' '
        if Gophers > 0:
            Gophers -= 1
            GophersNum.set(f'地鼠數量: {Gophers}')

def timeOut():
    global GophersNum
    global StageNum
    global Stage
    if Stage >= 5:
        StageNum.set('End')
        for b in bt:
            b.config(state=DISABLED, text=' ')
    else:
        Stage += 1
        StageNum.set(f'Stage: {Stage}')
        setAns()
        for i in range(100):
            bt[i].config(text=ans[i], state=DISABLED)
            if ans[i] == 'o':
                bt[i].config(state=ACTIVE)
        GophersNum.set(f'地鼠數量: {Gophers}')
        t = Timer(3, timeOut)
        t.start()

# create a window
root = Tk()
root.title("homework")

# create varible
ans = [' ' for i in range(100)]
bt = [0 for i in range(100)]
t = Timer(3, timeOut)
Stage = 1
StageNum = StringVar(value=f'Stage: {Stage}')
Gophers = 0
GophersNum = StringVar(value=f'地鼠數量: {Gophers}')
scope = 0
scopeNum = StringVar(value=f'總分: {scope}')
setAns()

# create label
Label(root, textvariable=StageNum, width=18, height=1, font="微軟正黑體 15").grid(column=0, row=10, columnspan=5)
Label(root, textvariable=GophersNum, width=18, height=1, font="微軟正黑體 15").grid(column=5, row=10, columnspan=5)
Label(root, textvariable=scopeNum, width=18, height=1, font="微軟正黑體 15").grid(column=0, row=11, columnspan=10)

# create button
k = 0
for i in range(10):
    for j in range(10):
        bt[k] = Button(root, width=6, text=ans[k], height=3, font="微軟正黑體 9", \
            command=lambda k=k: press(k))
        bt[k].grid(row=i, column=j)
        if ans[k] != 'o': bt[k].config(state=DISABLED)
        k += 1

# execute
t.start()
root.mainloop()