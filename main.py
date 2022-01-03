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
#tk.resizable(0,0)
#tk.wm_attributes("-topmost", 1)
tk.iconbitmap("logo.ico")

canvas = Canvas(tk, width=1200, height=800, bg="grey", highlightthickness=0)
canvas.pack()

grey_rectangle = PhotoImage(file="grey_rectangle.png")
grey_rectangle_id = canvas.create_image(600, 400, image=grey_rectangle)

dark_grey = PhotoImage(file="dark.png")
dark_grey_id = canvas.create_image(600, 58, image=dark_grey)


atm = PhotoImage(file="ATM.png")
atm_id = canvas.create_image(600, 20, image=atm)



image2 = PhotoImage(file='Vector 2.png')
img2_id = canvas.create_image(598, 632, image = image2)

image3 = PhotoImage(file='Vector 3.png')
img3_id = canvas.create_image(597, 293, image = image3)


image4 = PhotoImage(file='white_rectangle.png')
img4_id = canvas.create_image(400, 620, image = image4)


#add_buttom_1
bottom_n1 = PhotoImage(file="n1.png")
Button(tk, image=bottom_n1, highlightthickness=0, bd=0, command=get_1).place(x=200, y=520)

#add_buttom_2
bottom_n2 = PhotoImage(file="n2.png")
Button(tk, image=bottom_n2, highlightthickness=0, bd=0, command=get_1).place(x=290, y=520)

#add_buttom_3
bottom_n3 = PhotoImage(file="n3.png")
Button(tk, image=bottom_n3, highlightthickness=0, bd=0, command=get_1).place(x=379, y=520)

#add_buttom_4
bottom_n4 = PhotoImage(file="n4.png")
Button(tk, image=bottom_n4, highlightthickness=0, bd=0, command=get_1).place(x=195, y=570)

#add_buttom_5
bottom_n5 = PhotoImage(file="n5.png")
Button(tk, image=bottom_n5, highlightthickness=0, bd=0, command=get_1).place(x=287, y=570)

#add_buttom_6
bottom_n6 = PhotoImage(file="n6.png")
Button(tk, image=bottom_n6, highlightthickness=0, bd=0, command=get_1).place(x=380, y=570)

#add_buttom_7
bottom_n7 = PhotoImage(file="n7.png")
Button(tk, image=bottom_n7, highlightthickness=0, bd=0, command=get_1).place(x=190, y=620)

#add_buttom_8
bottom_n8 = PhotoImage(file="n8.png")
Button(tk, image=bottom_n8, highlightthickness=0, bd=0, command=get_1).place(x=286, y=620)

#add_buttom_9
bottom_n9 = PhotoImage(file="n9.png")
Button(tk, image=bottom_n9, highlightthickness=0, bd=0, command=get_1).place(x=386, y=620)

#add_buttom_minus
bottom_minus = PhotoImage(file="minus.png")
Button(tk, image=bottom_minus, highlightthickness=0, bd=0, command=get_1).place(x=186, y=670)

#add_buttom_null
bottom_null = PhotoImage(file="null.png")
Button(tk, image=bottom_null, highlightthickness=0, bd=0, command=get_1).place(x=280, y=670)

#add_buttom_plus
bottom_plus = PhotoImage(file="plus.png")
Button(tk, image=bottom_plus, highlightthickness=0, bd=0, command=get_1).place(x=392, y=670)

#add_buttom_cancel
bottom_cancel = PhotoImage(file="cancel.png")
Button(tk, image=bottom_cancel, highlightthickness=0, bd=0, command=get_1).place(x=500, y=520)

#add_buttom_clear
bottom_clear = PhotoImage(file="clear.png")
Button(tk, image=bottom_clear, highlightthickness=0, bd=0, command=get_1).place(x=505, y=570)

#add_buttom_enter
bottom_enter = PhotoImage(file="enter.png")
Button(tk, image=bottom_enter, highlightthickness=0, bd=0, command=get_1).place(x=510, y=620)

#add_buttom_empty
bottom_empty = PhotoImage(file="empty.png")
Button(tk, image=bottom_empty, highlightthickness=0, bd=0, command=get_1).place(x=515, y=670)

#add_screen and buttoms
screen_frame = PhotoImage(file="screen_frame.png")
screen_frame_id = canvas.create_image(404, 295, image=screen_frame)

screen = PhotoImage(file="screen.png")
screen_id = canvas.create_image(400, 295, image=screen)

#add_buttom_s1
bottom_s1 = PhotoImage(file="screen_buttom.png")
Button(tk, image=bottom_s1, highlightthickness=0, bd=0, command=get_1).place(x=135, y=170)

#add_buttom_s2
bottom_s2 = PhotoImage(file="screen_buttom.png")
Button(tk, image=bottom_s2, highlightthickness=0, bd=0, command=get_1).place(x=135, y=270)

#add_buttom_s3
bottom_s3 = PhotoImage(file="screen_buttom.png")
Button(tk, image=bottom_s3, highlightthickness=0, bd=0, command=get_1).place(x=135, y=370)

#add_buttom_s4
bottom_s4 = PhotoImage(file="screen_buttom.png")
Button(tk, image=bottom_s4, highlightthickness=0, bd=0, command=get_1).place(x=633, y=170)

#add_buttom_5
bottom_s5 = PhotoImage(file="screen_buttom.png")
Button(tk, image=bottom_s5, highlightthickness=0, bd=0, command=get_1).place(x=633, y=270)

#add_buttom_6
bottom_s6 = PhotoImage(file="screen_buttom.png")
Button(tk, image=bottom_s6, highlightthickness=0, bd=0, command=get_1).place(x=633, y=370)


cash = PhotoImage(file="for_cash.png")
cash_id = canvas.create_image(900, 495, image=cash)

card = PhotoImage(file="for card.png")
card_id = canvas.create_image(823, 245, image=card)

receipt = PhotoImage(file="for_receipt.png")
receipt_id = canvas.create_image(1000, 245, image=receipt)


tk.mainloop()