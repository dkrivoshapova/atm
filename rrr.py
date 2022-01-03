from tkinter import *
from tkinter import messagebox

def closing_app():
    if messagebox.askokcancel("Выход из банкомата", "Вы действительно хотите выйти?"):
        tk.destroy()
def get_1():
    pass
def get_1():
    pass

tk = Tk()
#tk.protocol("WM_DELETE_WINDOW", closing_app)
tk.title("Банкомат")
tk.resizable(0,0)
#tk.wm_attributes("-topmost", 1)
tk.iconbitmap("logo.ico")

canvas = Canvas(tk, width=1200, height=800, bg="grey", highlightthickness=0)
canvas.pack()

grey_rectangle = PhotoImage(file = "grey_rectangle.png")
grey_rectangle_id = canvas.create_image(600, 400, image=grey_rectangle)

atm = PhotoImage(file="ATM.png")
atm_id = canvas.create_image(600, 50, image=atm)



image3 = PhotoImage(file='white_rectangle.png')
img_id = canvas.create_image(100, 300, image = image3)


#add_buttom_1
bottom_n1 = PhotoImage(file="n1.png")
id_bt_n1 = canvas.create_image(100,100, image = bottom_n1)
Button(tk, image=bottom_n1, highlightthickness=0, bd=0, command=get_1).place(x=100, y=100)

#add_buttom_2
bottom_n2 = PhotoImage(file="n2.png")
label = Label(tk, image=bottom_n2)
label.place(x=190,y=100)

tk.mainloop()