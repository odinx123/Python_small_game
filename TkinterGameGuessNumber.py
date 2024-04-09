from tkinter import*
from random import randint

# method
def start():
    try:
        MinN[0] = min_range.get()
        MaxN[0] = Max_range.get()
        answer[0] = randint(int(MinN[0]), int(MaxN[0]))
        Question_lb.config(text='請猜'+MinN[0]+'到'+MaxN[0]+'的數字')
    except:
        print("Input Error!!!")
        return
# Hide obj
    reset_btn.pack_forget()
    Max_range.pack_forget()
    min_range.pack_forget()
    lb.pack_forget()
    start_btn.pack_forget()
    MaxRangeLabel.pack_forget()
    MinRangeLabel.pack_forget()
# show obj
# ************************************************************************** #
    Question_lb.pack()
    ans.pack()
    confirm_btn.pack()
def confirm():
    try:
        if (int(ans.get()) > int(MaxN[0]) or int(ans.get()) < int(MinN[0])):
            return
    except:
        print("Input Error!!!")
    if answer[0] == int(ans.get()):
        confirm_btn.pack_forget()
        ans.pack_forget()
        Question_lb.config(text="恭喜獲勝")
        reset_btn.pack(side="bottom")
        return
    elif answer[0] > int(ans.get()):
        MinN[0] = str(int(ans.get())+1)
    else:
        MaxN[0] = str(int(ans.get())-1)
    Question_lb.config(text='請猜'+MinN[0]+'到'+MaxN[0]+'的數字')
def reset():
    Max_range.delete(0, END)
    min_range.delete(0, END)
# Hide obj
    confirm_btn.pack_forget()  # Hide the confirm button
    ans.pack_forget() # Hide the Entry obj
    Question_lb.pack_forget()
# show obj
# ************************************************************************** #
    lb.pack()  # Show the label obj
    start_btn.pack()    # show the start button
    reset_btn.pack(side="bottom") # show the reset button
    MaxRangeLabel.pack()
    Max_range.pack()
    MinRangeLabel.pack()
    min_range.pack()
    quit_btn.pack(side="bottom")
def quitGame():
    win.quit()
# ************************************************************************** #
# set random integer
answer = [0]  # set random integer
MinN = ['']
MaxN = ['']
# ************************************************************************** #
# create window
win = Tk()
win.title("MyAPP")
win.config(bg="#232323")
win.geometry("220x270+400+200")
# ************************************************************************** #
#create label
lb = Label(text="猜數字遊戲!", bg="#232323", fg="Forestgreen", font="標楷體 24")
Question_lb = Label(bg="#232323", fg="white", font="標楷體 18")
MaxRangeLabel = Label(text="輸入最大值!", bg="#232323", fg="white", font="微軟正黑體 12")
MinRangeLabel = Label(text="輸入最小值!", bg="#232323", fg="white", font="微軟正黑體 12")
# ************************************************************************** #
#create button
# This button for start
start_btn = Button(text="開始", font="標楷體 18", bg="skyBlue"\
            , fg="#ff4500", width=15, command=start)
# This button for confirm
confirm_btn = Button(text="確認", font="標楷體 18", bg="skyBlue"\
            , fg="#ff4500", width=15, command=confirm)
# This button for reset
reset_btn = Button(text="重新", font="標楷體 18", bg="skyBlue"\
            , fg="#ff4500", width=15, command=reset) 
quit_btn = Button(text="結束", font="標楷體 18", bg="skyBlue"\
            , fg="#ff4500", width=15, command=quitGame) 
# ************************************************************************** #
#create Entry
ans = Entry()
Max_range = Entry()
min_range = Entry()
# reset
reset()
# ************************************************************************** #
# Start main loop
win.mainloop()