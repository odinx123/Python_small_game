from tkinter import*

def pressBef():
    global pos
    pos = pos - 1 if pos - 1 >= 0 else len(data)-1
    for i in range(5):
        if i < 2:
            enVari[i].set(data[pos][i])
        else:
            gender.set(0) if data[pos][2] == gen[0] else gender.set(1)
            enVari[i].set(data[pos][i+1])

def pressAft():
    global pos
    pos = pos + 1 if pos + 1 < len(data) else 0
    for i in range(5):
        if i < 2:
            enVari[i].set(data[pos][i])
        else:
            gender.set(0) if data[pos][2] == gen[0] else gender.set(1)
            enVari[i].set(data[pos][i+1])

# create windows
root = Tk()
root.title("TOD")
root.geometry("+500+100")

# create variable
gender = IntVar()
rdBt = [0, 1]
en = []
data = []
enVari = [StringVar() for i in range(5)]
pos = 0

# create radiobutton
for i in range(len(rdBt)):
    gen = ['男', '女']
    rdBt[i] = Radiobutton(root, variable=gender, value=i, text=gen[i], font="標楷體 14")
    rdBt[i].grid(row=2, column=i, sticky='nsew')

# # create entry
j = 0
with open(file='D:\\programfile\\Python\\Test\\dataSerch\\data.txt', mode='r', encoding='utf-8') as file_in:
    for i in [datas.strip('\n') for datas in file_in.readlines()]:
        data.append(i.split(' '))
for i in range(5):
    en.append(Entry(root, textvariable=enVari[i], width=25, font="標楷體 14"))
    en[i].grid(row=i if i < 2 else i+1, column=1, sticky='nsew')
    if i < 2:
        enVari[i].set(data[pos][i])
    else:
        gender.set(0) if data[pos][2] == gen[0] else gender.set(1)
        enVari[i].set(data[pos][i+1])

# create button
preBt = Button(root, text='前一筆', font="標楷體 16", command=pressBef)
preBt.grid(row=6, column=0)
aftBt = Button(root, text='下一筆', font="標楷體 16", command=pressAft)
aftBt.grid(row=6, column=1)

# create label
Label(root, text='學號:', font="標楷體 16").grid(row=0, column=0)
Label(root, text='姓名:', font="標楷體 16").grid(row=1, column=0)
Label(root, text='系所:', font="標楷體 16").grid(row=3, column=0)
Label(root, text='地址:', font="標楷體 16").grid(row=4, column=0)
Label(root, text='電話:', font="標楷體 16").grid(row=5, column=0)

# game start
root.mainloop()