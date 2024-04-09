from tkinter import*
from random import randint
from threading import Timer

def press(event):
    global e, score, remainBullet, t
    if ans.get() == "GameOver ! ! !":
        reset()
        return
    if e.get() == ans.get():
        score += 1; remainBullet -= 1
        sc.set(f'score: {score}')
        for i in range(height-1, -1, -1):
            if board[i] != -1:
                bt[i*width+board[i]].config(text='')
                board[i] = -1
                ans.set(''.join(chr(randint(97, 122)) for i in range(randint(1, 7))))
                break
    if remainBullet == 0:
        t.cancel()
        ans.set("GameOver ! ! !")
    e.set('')

def fall():
    global t, bullet
    t = Timer(1, fall)
    print(board)
    if remainBullet == 0:
        t.cancel()
        ans.set("GameOver ! ! !")
    for i in range(height-1, -1, -1):
        if board[i] != -1 and i != height-1 and i != 9:
            bt[(i)*width+board[i]].config(text='')
            bt[(i+1)*width+board[i]].config(text='⌛')
            board[i+1] = board[i]
            board[i] = -1
        if i == 9 and board[i] != -1:
            bt[(i)*width+board[i]].config(text='')
            ans.set("GameOver ! ! !")
            t.cancel()
    if bullet > 0:
        board[0] = randint(0, width-1)
        bt[board[0]].config(text='⌛')
        bullet -= 1
    t.start()

def reset():
    global ans, score, t, bullet, remainBullet
    bullet = remainBullet = 10
    t.cancel()
    t = Timer(1, fall)
    score = 0
    sc.set(f'score: {score}')
    ans.set(''.join(chr(randint(97, 122)) for i in range(randint(1, 7))))
    for i in bt:
        i.config(text='')
    for i in range(height+1):
        board[i] = -1
    t.start()

# create windows
root = Tk()
root.title("TOD")
root.geometry("+500+100")

# create variable
bullet = 10
remainBullet = 10
width = 10
height = 10
t = Timer(1, fall)
fruitImg = []
bt = []
board = [-1 for i in range(height+1)]
ans = StringVar(value=''.join(chr(randint(97, 122)) for i in range(randint(1, 7))))
e = StringVar()
score = 0
sc = StringVar(value=f'score: {score}')

# create entry
ent = Entry(root, textvariable=e)
ent.focus()
ent.grid(row=height, column=3, columnspan=3)
# ⌛ i*width+j

# create button
for i in range(height):
    for j in range(width):
        bt.append(Button(root, width=3, text=' ', state=DISABLED, font="微軟正黑體 20"))
        bt[i*width+j].grid(row=i, column=j)
root.bind('<Return>', press)

# create label
lb = Label(root, textvariable=sc)
lb.grid(row=height, column=width-2, columnspan=3, sticky="nsew")
ansLb = Label(root, textvariable=ans)
ansLb.grid(row=height, column=0, columnspan=3, sticky='nsew')

# game start
t.start()
root.mainloop()