from tkinter import *
import tkinter as tk

num1 = 0
number2 = 0
operator = ""


def btn_clicked():
    # entry0.
    print("Button Clicked")


window = Tk()

v = tk.StringVar()


def set_text(value):
    # text1=entry1.get()
    entry1.insert(1000, value)
    # entry1.entry1
    # v.set(word)


def button_1():
    set_text("1")


def button_2():
    set_text("2")


def button_3():
    set_text("3")


def button_4():
    set_text("4")


def button_5():
    set_text("5")


def button_6():
    set_text("6")


def button_7():
    set_text("7")


def button_8():
    set_text("8")


def button_9():
    set_text("9")


def button_0():
    set_text("0")


def button_plus():
    operator = "+"
    num1 = int(entry1.get())
    set_text("+")
    print(num1)


def button_minas():
    operator = "-"
    num1 = int(entry1.get())
    set_text("-")
    print(num1)


def button_division():
    operator = "/"
    num1 = int(entry1.get())
    set_text("/")
    print(num1)


# def button_multiply():
#     set_text("*")


def calculate():
    num2 = int(entry1.get())
    if operator == "+":
        plus = num1 + number2
    elif operator == "-":
        minez = number2 - num1
    else:
        division = num1 / number2


window.geometry("350x500")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=500,
    width=350,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    175.0, 250.0,
    image=background_img)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=button_1,
    relief="flat")

b0.place(
    x=25, y=200,
    width=87,
    height=39)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=button_plus,
    relief="flat")

b1.place(
    x=8, y=20,
    width=70,
    height=40)

img2 = PhotoImage(file=f"img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=button_minas,
    relief="flat")

b2.place(
    x=90, y=20,
    width=70,
    height=40)

img3 = PhotoImage(file=f"img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=button_division,
    relief="flat")

b3.place(
    x=170, y=20,
    width=70,
    height=40)

img4 = PhotoImage(file=f"img4.png")
b4 = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=button_2,
    relief="flat")

b4.place(
    x=140, y=200,
    width=87,
    height=39)

img5 = PhotoImage(file=f"img5.png")
b5 = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=button_3,
    relief="flat")

b5.place(
    x=250, y=200,
    width=87,
    height=39)

img6 = PhotoImage(file=f"img6.png")
b6 = Button(
    image=img6,
    borderwidth=0,
    highlightthickness=0,
    command=button_4,
    relief="flat")

b6.place(
    x=25, y=270,
    width=87,
    height=39)

img7 = PhotoImage(file=f"img7.png")
b7 = Button(
    image=img7,
    borderwidth=0,
    highlightthickness=0,
    command=button_5,
    relief="flat")

b7.place(
    x=140, y=270,
    width=87,
    height=39)

img8 = PhotoImage(file=f"img8.png")
b8 = Button(
    image=img8,
    borderwidth=0,
    highlightthickness=0,
    command=button_6,
    relief="flat")

b8.place(
    x=250, y=270,
    width=87,
    height=41)

img9 = PhotoImage(file=f"img9.png")
b9 = Button(
    image=img9,
    borderwidth=0,
    highlightthickness=0,
    command=button_7,
    relief="flat")

b9.place(
    x=25, y=340,
    width=87,
    height=41)

img10 = PhotoImage(file=f"img10.png")
b10 = Button(
    image=img10,
    borderwidth=0,
    highlightthickness=0,
    command=button_8,
    relief="flat")

b10.place(
    x=140, y=340,
    width=87,
    height=41)

img11 = PhotoImage(file=f"img11.png")
b11 = Button(
    image=img11,
    borderwidth=0,
    highlightthickness=0,
    command=button_9,
    relief="flat")

b11.place(
    x=250, y=340,
    width=87,
    height=41)

img12 = PhotoImage(file=f"img12.png")
b12 = Button(
    image=img12,
    borderwidth=0,
    highlightthickness=0,
    command=button_0,
    relief="flat")

b12.place(
    x=180, y=425,
    width=87,
    height=39)

img13 = PhotoImage(file=f"img13.png")
b13 = Button(
    image=img13,
    borderwidth=0,
    highlightthickness=0,
    command=calculate,
    relief="flat")

b13.place(
    x=80, y=425,
    width=87,
    height=39)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    -179.5, -143.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0)

entry0.place(
    x=40.0, y=120,
    width=281.0,
    height=35)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    179.5, 84.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0,
    textvariable=v)

entry1.place(
    x=40.0, y=68,
    width=281.0,
    height=35)

window.resizable(False, False)
window.mainloop()
