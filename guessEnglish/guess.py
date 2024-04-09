from tkinter import*
from random import randint

def press():
    global a, s
    if e.get() == enLis[sPos]:
        a += 1
        setAns()
    an.set(f"答對數目: {a}")

def setAns():
    global dic, en, ch, sPos, enLis
    with open("D:\\programfile\\Python\\Test\\guessEnglish\\t.txt", 'r', encoding="utf-8") as file_in:
        arr = [data.strip('\n') for data in file_in.readlines()]
    dic = {data.split(" ")[0]:data.split(" ")[1] for data in arr}
    enLis = [data.split(" ")[0] for data in arr]
    sPos = randint(0, len(dic))
    enString = ''
    for i in range(len(enLis[sPos])):
        if randint(0, 2) == 0:
            enString += '*'
        else:
            enString += enLis[sPos][i]
    print(enLis[sPos], dic[enLis[sPos]])
    en.set(f"英文: {enString}")
    ch.set(f"中文: {dic[enLis[sPos]]}")

# create windows
root = Tk()
root.title("HomeWork")
root.geometry("200x300")

# create variable
e = StringVar()
ch = StringVar(value="中文: ")
en = StringVar(value="英文: ")
a = 0
an = StringVar(value=f"答對數目: {a}")
enLis = []
sPos = 0

# create label
chLb = Label(root, textvariable=ch, height=2, font="微軟正黑體 15")
chLb.pack()
enLb = Label(root, textvariable=en, height=2, font="微軟正黑體 15")
enLb.pack()
ans = Label(root, textvariable=an, height=2, font="微軟正黑體 15")
ans.pack()

# create entry
ent = Entry(root, textvariable=e)
ent.pack()

# create Button
bt = Button(root, text="確定", font="微軟正黑體 10", command=press)
bt.pack()

# game start
setAns()
root.mainloop()