from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from itertools import *
from random import randint

temp = 0
after_id = ''
after_id2 = ''


def tick():
    global temp, after_id
    after_id = tk.after(500, tick)
    if temp == 0:
        canvas.itemconfigure(card_id, image=card_images[1])
        temp = 1
    else:
        canvas.itemconfigure(card_id, image=card_images[0])
        temp = 0


def stop_tick():
    tk.after_cancel(after_id)


def closing_app():
    if messagebox.askokcancel("Выход из банкомата", "Вы действительно хотите выйти?"):
        tk.destroy()


def change_card():
    global temp, after_id
    after_id = tk.after(500, change_card)
    if temp < 7:
        canvas.itemconfigure(card_id, image=card_images[temp])
        temp += 1
    else:
        stop_tick()
        canvas.itemconfigure(card_id, image=card_images[0])
        get_pasword()
        temp = 0


def get_pasword():
    canvas.itemconfigure(screen_id, image=screen_images[3])
    pasword_b.tkraise()
    pasword.tkraise()
    state_nuber_button(1)


def submit():
    if pasword_b.var.get():
        pasword.config(show='')
    else:
        pasword.config(show='*')


def execute_telephone():
    get_sum.delete(0, END)
    get_sum.lower()
    get_telephone.delete(0, END)
    get_telephone.lower()
    change_receipt()


def change_receipt():
    canvas.itemconfigure(screen_id, image=screen_images[6])
    global temp, after_id
    after_id = tk.after(500, change_receipt)
    if temp < 5:
        canvas.itemconfigure(receipt_id, image=receipt_images[temp])
        temp += 1
    else:
        stop_tick()
        canvas.itemconfigure(receipt_id, image=receipt_images[0])
        want_to_exit()
        temp = 0


def change_cash():
    canvas.itemconfigure(screen_id, image=screen_images[2])
    get_sum.lower()
    global temp, after_id
    after_id = tk.after(500, change_cash)
    if temp < 7:
        canvas.itemconfigure(cash_id, image=cash_images[temp])
        temp += 1
    else:
        stop_tick()
        canvas.itemconfigure(cash_id, image=cash_images[0])
        want_to_exit()
        temp = 0


def add_cash():
    canvas.itemconfigure(screen_id, image=screen_images[2])
    get_sum.lower()
    global temp, after_id
    after_id = tk.after(500, add_cash)
    if temp + 6 > 0:
        canvas.itemconfigure(cash_id, image=cash_images[temp + 6])
        temp -= 1
    else:
        stop_tick()
        canvas.itemconfigure(cash_id, image=cash_images[0])
        want_to_exit()
        temp = 0


def add_char_pasword(char):
    value = pasword.get() + char
    if char.isdigit() and len(value) < 5:
        pasword.delete(0, END)
        pasword.insert(0, value)
    else:
        messagebox.showerror(title="Error", message="Недопустимый ввод")


def add_char_sum(char):
    val = get_sum.get() + char
    if char.isdigit():
        get_sum.delete(0, END)
        get_sum.insert(0, val)
    else:
        messagebox.showerror(title="Error", message="Недопустимый ввод")


def add_char_tel(char):
    l = get_telephone.get() + char
    if (char == '+' and len(l) == 1) or (char.isdigit() and len(l) > 1 and len(l) < 13):
        get_telephone.delete(0, END)
        get_telephone.insert(0, l)
    else:
        messagebox.showerror(title="Error", message="Недопустимый ввод")


def card():
    start_b.lower()
    stop_tick()
    canvas.itemconfigure(screen_id, image=screen_images[2])
    change_card()


def fun_char_pasword(char):
    value = pasword.get()
    if char == 'e' and len(value) == 4:
        pasword.lower()
        pasword_b.lower()
        pasword.delete(0, END)
        # canvas.delete("password")
        canvas.itemconfigure(screen_id, image=screen_images[4])
        state_screen_button(1)
        state_nuber_button(0)
    elif char == 'a':
        value = pasword.get()
        pasword.delete(0, END)
        pasword.insert(0, value[:-1])
    elif char == 'd':
        pasword.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="Недопустимый ввод")


def fun_char_sum(char):
    val = int(get_sum.get())
    if char == 'e' and val % 100 == 0 and val > 99 and val < 500001:
        b_s3.config(state=NORMAL)
        b_s6.config(state=NORMAL)
        state_nuber_button(0)
    elif char == 'a':
        val = get_sum.get()
        get_sum.delete(0, END)
        get_sum.insert(0, val[:-1])
    elif char == 'd':
        get_sum.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="Недопустимый ввод")


def fun_char_tel(char):
    l = get_telephone.get()
    if char == 'e' and len(l) == 12:
        button_get_sum()
    elif char == 'a':
        val = get_sum.get()
        get_telephone.delete(0, END)
        get_telephone.insert(0, val[:-1])
    elif char == 'd':
        get_telephone.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="Недопустимый ввод")


def screen_button_menu(n):
    if n == 1:
        withdrow()
    elif n == 2:
        balance()
    elif n == 3:
        telephone()
    elif n == 4:
        deposit()
    elif n == 5:
        balance()
    else:
        want_to_exit()


def state_screen_button(n):
    if n == 1:
        b_s1.config(state=NORMAL)
        b_s2.config(state=NORMAL)
        b_s3.config(state=NORMAL)
        b_s4.config(state=NORMAL)
        b_s5.config(state=NORMAL)
        b_s6.config(state=NORMAL)
    elif n == 0:
        b_s1.config(state=DISABLED)
        b_s2.config(state=DISABLED)
        b_s3.config(state=DISABLED)
        b_s4.config(state=DISABLED)
        b_s5.config(state=DISABLED)
        b_s6.config(state=DISABLED)


def state_nuber_button(n):
    if n == 1:
        b_n1.config(state=NORMAL)
        b_n2.config(state=NORMAL)
        b_n3.config(state=NORMAL)
        b_n4.config(state=NORMAL)
        b_n5.config(state=NORMAL)
        b_n6.config(state=NORMAL)
        b_n7.config(state=NORMAL)
        b_n8.config(state=NORMAL)
        b_n9.config(state=NORMAL)
        b_minus.config(state=NORMAL)
        b_null.config(state=NORMAL)
        b_plus.config(state=NORMAL)
        b_cancel.config(state=NORMAL)
        b_clear.config(state=NORMAL)
        b_enter.config(state=NORMAL)
        b_empty.config(state=NORMAL)

    elif n == 0:
        b_n1.config(state=DISABLED)
        b_n2.config(state=DISABLED)
        b_n3.config(state=DISABLED)
        b_n4.config(state=DISABLED)
        b_n5.config(state=DISABLED)
        b_n6.config(state=DISABLED)
        b_n7.config(state=DISABLED)
        b_n8.config(state=DISABLED)
        b_n9.config(state=DISABLED)
        b_minus.config(state=DISABLED)
        b_null.config(state=DISABLED)
        b_plus.config(state=DISABLED)
        b_cancel.config(state=DISABLED)
        b_clear.config(state=DISABLED)
        b_enter.config(state=DISABLED)
        b_empty.config(state=DISABLED)


def deposit():
    canvas.itemconfigure(screen_id, image=screen_images[8])
    b_s1.config(state=DISABLED)
    b_s2.config(state=DISABLED)
    b_s3.config(state=DISABLED)
    b_s4.config(state=DISABLED)
    b_s5.config(command=add_cash)
    b_s6.config(command=menu)


def withdrow():
    canvas.itemconfigure(screen_id, image=screen_images[11])
    b_s1.config(command=change_cash)
    b_s2.config(command=change_cash)
    b_s3.config(command=get_withdrow_sum)
    b_s4.config(command=change_cash)
    b_s5.config(command=change_cash)
    b_s6.config(command=menu)


def button_get_sum():
    state_screen_button(0)

    b_s6.config(state=NORMAL)

    b_n1.config(command=lambda: add_char_sum('1'))
    b_n2.config(command=lambda: add_char_sum('2'))
    b_n3.config(command=lambda: add_char_sum('3'))
    b_n4.config(command=lambda: add_char_sum('4'))
    b_n5.config(command=lambda: add_char_sum('5'))
    b_n6.config(command=lambda: add_char_sum('6'))
    b_n7.config(command=lambda: add_char_sum('7'))
    b_n8.config(command=lambda: add_char_sum('8'))
    b_n9.config(command=lambda: add_char_sum('9'))
    b_minus.config(command=lambda: add_char_sum('-'))
    b_null.config(command=lambda: add_char_sum('0'))
    b_plus.config(command=lambda: add_char_sum('+'))

    b_cancel.config(command=lambda: fun_char_sum('a'))
    b_clear.config(command=lambda: fun_char_sum('d'))
    b_enter.config(command=lambda: fun_char_sum('e'))

    b_s1.config(state=DISABLED)
    b_s2.config(state=DISABLED)
    b_s4.config(state=DISABLED)
    b_s5.config(state=DISABLED)
    state_nuber_button(1)


def button_get_telephone():
    state_screen_button(0)
    b_s6.config(state=NORMAL)
    b_n1.config(command=lambda: add_char_tel('1'))
    b_n2.config(command=lambda: add_char_tel('2'))
    b_n3.config(command=lambda: add_char_tel('3'))
    b_n4.config(command=lambda: add_char_tel('4'))
    b_n5.config(command=lambda: add_char_tel('5'))
    b_n6.config(command=lambda: add_char_tel('6'))
    b_n7.config(command=lambda: add_char_tel('7'))
    b_n8.config(command=lambda: add_char_tel('8'))
    b_n9.config(command=lambda: add_char_tel('9'))
    b_minus.config(command=lambda: add_char_tel('-'))
    b_null.config(command=lambda: add_char_tel('0'))
    b_plus.config(command=lambda: add_char_tel('+'))

    b_cancel.config(command=lambda: fun_char_tel('a'))
    b_clear.config(command=lambda: fun_char_tel('d'))
    b_enter.config(command=lambda: fun_char_tel('e'))

    b_s3.config(command=execute_telephone)
    b_s6.config(command=menu)
    state_nuber_button(1)


def get_withdrow_sum():
    b_s3.config(command=change_cash)
    canvas.itemconfigure(screen_id, image=screen_images[10])
    get_sum.lift()
    button_get_sum()


def menu():
    canvas.itemconfigure(screen_id, image=screen_images[4])
    get_sum.lower()
    get_telephone.lower()
    state_nuber_button(0)
    state_screen_button(1)
    menu_bottom()
    get_telephone.delete(0, END)
    get_sum.delete(0, END)


def menu_bottom():
    b_s1.config(command=lambda: screen_button_menu(1))
    b_s2.config(command=lambda: screen_button_menu(2))
    b_s3.config(command=lambda: screen_button_menu(3))
    b_s4.config(command=lambda: screen_button_menu(4))
    b_s5.config(command=lambda: screen_button_menu(5))
    b_s6.config(command=lambda: screen_button_menu(6))


def balance():
    change_receipt()
    state_screen_button(0)


def telephone():
    state_screen_button(0)
    canvas.itemconfigure(screen_id, image=screen_images[7])
    state_nuber_button(1)
    get_sum.tkraise()
    button_get_telephone()
    get_telephone.tkraise()


def want_to_exit():
    canvas.itemconfigure(screen_id, image=screen_images[5])
    b_s3.config(command=return_card)
    b_s3.config(state=NORMAL)
    b_s6.config(command=menu)
    b_s6.config(state=NORMAL)


def return_card():
    global temp, after_id
    after_id = tk.after(500, return_card)
    if temp + 6 > -1:
        canvas.itemconfigure(card_id, image=card_images[temp + 6])
        temp -= 1
    else:
        stop_tick()
        canvas.itemconfigure(card_id, image=card_images[0])
        start()
        temp = 0


def start():
    canvas.itemconfigure(screen_id, image=screen_images[1])
    tick()
    start_b.tkraise()
    start_b.configure(state=NORMAL)
    state_screen_button(0)
    state_nuber_button(0)
    start_button()


def start_button():
    menu_bottom()

    b_n1.configure(command=lambda: add_char_pasword('1'))
    b_n2.configure(command=lambda: add_char_pasword('2'))
    b_n3.configure(command=lambda: add_char_pasword('3'))
    b_n4.configure(command=lambda: add_char_pasword('4'))
    b_n5.configure(command=lambda: add_char_pasword('5'))
    b_n6.configure(command=lambda: add_char_pasword('6'))
    b_n7.configure(command=lambda: add_char_pasword('7'))
    b_n8.configure(command=lambda: add_char_pasword('8'))
    b_n9.configure(command=lambda: add_char_pasword('9'))

    b_minus.config(command=lambda: add_char_pasword('-'))
    b_null.config(command=lambda: add_char_pasword('0'))
    b_plus.config(command=lambda: add_char_pasword('+'))

    b_cancel.config(command=lambda: fun_char_pasword('a'))
    b_clear.config(command=lambda: fun_char_pasword('d'))
    b_enter.config(command=lambda: fun_char_pasword('e'))


tk = Tk()
tk.protocol("WM_DELETE_WINDOW", closing_app)
tk.title("Банкомат")
# tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
tk.iconbitmap("logo.ico")

card_images = []
cash_images = []
receipt_images = []
screen_images = []

canvas = Canvas(tk, width=1200, height=800, bg="grey", highlightthickness=0)
canvas.pack()

grey_rectangle = ImageTk.PhotoImage(file="grey_rectangle.png")
grey_rectangle_id = canvas.create_image(600, 400, image=grey_rectangle)

dark_grey = ImageTk.PhotoImage(file="dark.png")
dark_grey_id = canvas.create_image(600, 58, image=dark_grey)

atm = ImageTk.PhotoImage(file="ATM.png")
atm_id = canvas.create_image(600, 20, image=atm)

image2 = ImageTk.PhotoImage(file='Vector 2.png')
img2_id = canvas.create_image(598, 632, image=image2)

image3 = ImageTk.PhotoImage(file='Vector 3.png')
img3_id = canvas.create_image(597, 293, image=image3)

image4 = ImageTk.PhotoImage(file='white_rectangle.png')
img4_id = canvas.create_image(400, 630, image=image4)

nfc = ImageTk.PhotoImage(file="nfc.png")
nfc_id = canvas.create_image(920, 665, image=nfc)

# add_buttom_1
bottom_n1 = ImageTk.PhotoImage(file="n1.png")
b_n1 = Button(tk, image=bottom_n1, highlightthickness=0, bd=0, command=lambda: add_char_pasword('1'))
b_n1_id = canvas.create_window(250, 550, window=b_n1)

# add_buttom_2
bottom_n2 = ImageTk.PhotoImage(file="n2.png")
b_n2 = Button(tk, image=bottom_n2, highlightthickness=0, bd=0, command=lambda: add_char_pasword('2'))
b_n2_id = canvas.create_window(350, 550, window=b_n2)

# add_buttom_3
bottom_n3 = ImageTk.PhotoImage(file="n3.png")
b_n3 = Button(tk, image=bottom_n3, highlightthickness=0, bd=0, command=lambda: add_char_pasword('3'))
b_n3_id = canvas.create_window(450, 550, window=b_n3)

# add_buttom_4
bottom_n4 = ImageTk.PhotoImage(file="n4.png")
b_n4 = Button(tk, image=bottom_n4, highlightthickness=0, bd=0, command=lambda: add_char_pasword('4'))
b_n4_id = canvas.create_window(245, 600, window=b_n4)

# add_buttom_5
bottom_n5 = ImageTk.PhotoImage(file="n5.png")
b_n5 = Button(tk, image=bottom_n5, highlightthickness=0, bd=0, command=lambda: add_char_pasword('5'))
b_n5_id = canvas.create_window(350, 600, window=b_n5)

# add_buttom_6
bottom_n6 = ImageTk.PhotoImage(file="n6.png")
b_n6 = Button(tk, image=bottom_n6, highlightthickness=0, bd=0, command=lambda: add_char_pasword('6'))
b_n6_id = canvas.create_window(450, 600, window=b_n6)

# add_buttom_7
bottom_n7 = ImageTk.PhotoImage(file="n7.png")
b_n7 = Button(tk, image=bottom_n7, highlightthickness=0, bd=0, command=lambda: add_char_pasword('7'))
b_n7_id = canvas.create_window(240, 650, window=b_n7)

# add_buttom_8
bottom_n8 = ImageTk.PhotoImage(file="n8.png")
b_n8 = Button(tk, image=bottom_n8, highlightthickness=0, bd=0, command=lambda: add_char_pasword('8'))
b_n8_id = canvas.create_window(350, 650, window=b_n8)

# add_buttom_9
bottom_n9 = ImageTk.PhotoImage(file="n9.png")
b_n9 = Button(tk, image=bottom_n9, highlightthickness=0, bd=0, command=lambda: add_char_pasword('9'))
b_n9_id = canvas.create_window(450, 650, window=b_n9)

# add_buttom_minus
bottom_minus = ImageTk.PhotoImage(file="minus.png")
b_minus = Button(tk, image=bottom_minus, highlightthickness=0, bd=0, command=lambda: add_char_pasword('-'))
b_minus_id = canvas.create_window(235, 700, window=b_minus)

# add_buttom_null
bottom_null = ImageTk.PhotoImage(file="null.png")
b_null = Button(tk, image=bottom_null, highlightthickness=0, bd=0, command=lambda: add_char_pasword('0'))
b_null_id = canvas.create_window(350, 700, window=b_null)

# add_buttom_plus
bottom_plus = ImageTk.PhotoImage(file="plus.png")
b_plus = Button(tk, image=bottom_plus, highlightthickness=0, bd=0, command=lambda: add_char_pasword('+'))
b_plus_id = canvas.create_window(450, 700, window=b_plus)

# add_buttom_cancel
bottom_cancel = ImageTk.PhotoImage(file="cancel.png")
b_cancel = Button(tk, image=bottom_cancel, highlightthickness=0, bd=0, command=lambda: fun_char_pasword('a'))
b_cancel_id = canvas.create_window(550, 550, window=b_cancel)

# add_buttom_clear
bottom_clear = ImageTk.PhotoImage(file="clear.png")
b_clear = Button(tk, image=bottom_clear, highlightthickness=0, bd=0, command=lambda: fun_char_pasword('d'))
b_clear_id = canvas.create_window(555, 600, window=b_clear)

# add_buttom_enter
bottom_enter = ImageTk.PhotoImage(file="enter.png")
b_enter = Button(tk, image=bottom_enter, highlightthickness=0, bd=0, command=lambda: fun_char_pasword('e'))
b_enter_id = canvas.create_window(560, 650, window=b_enter)

# add_buttom_empty
bottom_empty = ImageTk.PhotoImage(file="empty.png")
b_empty = Button(tk, image=bottom_empty, highlightthickness=0, bd=0)
b_empty_id = canvas.create_window(565, 700, window=b_empty)

# add_screen and buttoms
screen_frame = ImageTk.PhotoImage(file="screen_frame.png")
screen_frame_id = canvas.create_image(404, 295, image=screen_frame)

screen_images.append(ImageTk.PhotoImage(file="screen.png"))  # 0
screen_images.append(ImageTk.PhotoImage(file="start_screen.png"))  # 1
screen_images.append(ImageTk.PhotoImage(file="load_screen.png"))  # 2
screen_images.append(ImageTk.PhotoImage(file="enter_pasword.png"))  # 3
screen_images.append(ImageTk.PhotoImage(file="menu_screen.png"))  # 4
screen_images.append(ImageTk.PhotoImage(file="want_to_exit.png"))  # 5
screen_images.append(ImageTk.PhotoImage(file="print_receipt.png"))  # 6
screen_images.append(ImageTk.PhotoImage(file="telephone.png"))  # 7
screen_images.append(ImageTk.PhotoImage(file="depos.png"))  # 8
screen_images.append(ImageTk.PhotoImage(file="please_wait.png"))  # 9
screen_images.append(ImageTk.PhotoImage(file="get_sum.png"))  # 10
screen_images.append(ImageTk.PhotoImage(file="select_sum.png"))  # 11

screen_id = canvas.create_image(400, 295, image=screen_images[1])

# add_buttom_s1
bottom_s1 = ImageTk.PhotoImage(file="screen_buttom.png")
b_s1 = Button(tk, image=bottom_s1, highlightthickness=5, bd=0, command=lambda: screen_button_menu(1))
b_s1_id = canvas.create_window(150, 200, window=b_s1)

# add_buttom_s2
b_s2 = Button(tk, image=bottom_s1, highlightthickness=5, bd=0, command=lambda: screen_button_menu(2))
b_s2_id = canvas.create_window(150, 300, window=b_s2)

# add_buttom_s3
b_s3 = Button(tk, image=bottom_s1, highlightthickness=5, bd=0, command=lambda: screen_button_menu(3))
b_s3_id = canvas.create_window(150, 400, window=b_s3)

# add_buttom_s4
b_s4 = Button(tk, image=bottom_s1, highlightthickness=5, bd=0, command=lambda: screen_button_menu(4))
b_s4_id = canvas.create_window(650, 200, window=b_s4)

# add_buttom_5
b_s5 = Button(tk, image=bottom_s1, highlightthickness=5, bd=0, command=lambda: screen_button_menu(5))
b_s5_id = canvas.create_window(650, 300, window=b_s5)

# add_buttom_6
b_s6 = Button(tk, image=bottom_s1, highlightthickness=5, bd=0, command=lambda: screen_button_menu(6))
b_s6_id = canvas.create_window(650, 400, window=b_s6)

state_screen_button(0)

card_images.append(ImageTk.PhotoImage(file="for card0.png"))
card_images.append(ImageTk.PhotoImage(file="for card1.png"))
card_images.append(ImageTk.PhotoImage(file="for card2.png"))
card_images.append(ImageTk.PhotoImage(file="for card3.png"))
card_images.append(ImageTk.PhotoImage(file="for card4.png"))
card_images.append(ImageTk.PhotoImage(file="for card5.png"))
card_images.append(ImageTk.PhotoImage(file="for card6.png"))
card_id = canvas.create_image(823, 245, image=card_images[0])

receipt_images.append(ImageTk.PhotoImage(file="receipt.png"))
receipt_images.append(ImageTk.PhotoImage(file="receipt1.png"))
receipt_images.append(ImageTk.PhotoImage(file="receipt2.png"))
receipt_images.append(ImageTk.PhotoImage(file="receipt3.png"))
receipt_images.append(ImageTk.PhotoImage(file="receipt4.png"))

receipt_id = canvas.create_image(1000, 245, image=receipt_images[0])

cash_images.append(ImageTk.PhotoImage(file="cash.png"))
cash_images.append(ImageTk.PhotoImage(file="cash1.png"))
cash_images.append(ImageTk.PhotoImage(file="cash2.png"))
cash_images.append(ImageTk.PhotoImage(file="cash3.png"))
cash_images.append(ImageTk.PhotoImage(file="cash4.png"))
cash_images.append(ImageTk.PhotoImage(file="cash5.png"))
cash_images.append(ImageTk.PhotoImage(file="cash6.png"))

cash_id = canvas.create_image(900, 495, image=cash_images[0])

pasword = Entry(tk, background='grey', highlightthickness=0, show='*')
pasword.lower()
canvas.create_window(400, 300, window=pasword, tags='pasword_id')

get_sum = Entry(tk, background='grey', highlightthickness=0)
get_sum.lower()
get_sum_id = canvas.create_window(500, 240, window=get_sum)

get_telephone = Entry(tk, background='grey', highlightthickness=0)
get_telephone.lower()
get_telephone_id = canvas.create_window(510, 205, window=get_telephone)

pasword_b = Checkbutton(tk, text="Показать пароль", highlightthickness=0, background='grey', command=submit,
                        onvalue=True, offvalue=False)
pasword_b.lower()
pasword_b.var = BooleanVar(value=False)
pasword_b.configure(variable=pasword_b.var)
canvas.create_window(400, 350, window=pasword_b, tags='password')

start_buttom = ImageTk.PhotoImage(file="start_card.png")
start_b = Button(tk, image=start_buttom, bd=0, highlightthickness=0, command=card)
start_b_id = canvas.create_window(300, 300, window=start_b, tags="start_b_id")
state_nuber_button(0)

tick()

tk.mainloop()
