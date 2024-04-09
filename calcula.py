from tkinter import*

def excute(i, j):
    global ans
    if strlist[i][j] == '=':
        ans.set(eval(str(ans.get())))
        temp.clear()
        return
    if strlist[i][j] == 'C':
        ans.set('')
        return
    temp.append(strlist[i][j])
    t = ans.get()
    for k in temp:
        ans.set(t+k)

# create a window
root = Tk()
root.title("homework")
root.geometry()

# declare varible
strlist = [['C', '/', '*', '-'], ['7', '8', '9', '+'], ['4', '5', '6'], ['1', '2', '3'], ['=', '0', '.']]
ans = StringVar()
temp = []

# create button
for i in range(1, 5):
    for j in range(3):
        Button(root, width=10, height=5, text=strlist[i-1][j], command=lambda i=i-1,j=j:excute(i, j)).grid(row=i, column=j)
        if (i == 1, j == 2):
            Button(root, text='-', width=10, height=5, command=lambda i=0,j=3:excute(i, j)).grid(row=1, column=3)
la = Label(root, width=20, height=5, textvariable=ans).grid(row=0, column=0, columnspan=4)
add = Button(root, text='+', width=10, height=11, command=lambda i=1,j=3:excute(i, j)).grid(row=2, column=3, rowspan=2)
eq = Button(root, text='=', width=10, height=11, command=lambda i=4,j=0:excute(i, j)).grid(row=4, column=3, rowspan=2)
zero = Button(root, text='0', width=21, height=5, command=lambda i=4,j=1:excute(i, j)).grid(row=5, column=0, columnspan=2)
dott = Button(root, text='.', width=10, height=5, command=lambda i=4,j=2:excute(i, j)).grid(row=5, column=2)

# execute
root.mainloop()