# use place
from tkinter import*

def loop(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

n = int(input(''))
# create a window
root = Tk()
root.title("homework")
root.geometry(f"{80*n}x{35*n}")

# create label
if n > 0:
    for i in range(0, n+1):
        for j in range(0, i+1):
            ans = loop(i) // (loop(j) * loop(i-j))
            Label(root, text = str(ans)).place(relx=(n-i+j*2)/(n*2+0.3), rely=i*2/(n*2+1))
    # execute
    root.mainloop()

# use grid
# from tkinter import*

# def loop(n):
#     ans = 1
#     for i in range(1, n+1):
#         ans *= i
#     return ans

# n = int(input(''))
# # create a window
# root = Tk()
# root.title("homework")

# # create label
# if n > 0:
#     Max = n//2+1 if n % 2 != 0 else n//2
#     spaceLen = len(str(loop(n) // (loop(Max) * loop(n-Max))))
#     for i in range(0, n+1):
#         for j in range(0, i+1):
#             ans = loop(i) // (loop(j) * loop(i-j))
#             Label(root, text=str(ans), width=spaceLen).grid(row=i, column=n-i+j*2)
#     # execute
#     root.mainloop()