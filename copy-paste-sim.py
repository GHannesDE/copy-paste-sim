from pynput.keyboard import Controller
import time
import tkinter as tk
from tkinter import *
from pynput import keyboard


root = Tk()
root.title("copy-paste-sim")
root.geometry("500x140+-10+0")
root.resizable(width=False, height=False)
root.attributes('-topmost', True)
root.configure(bg="#282828")
root.iconbitmap('./icon.ico')
root.overrideredirect(True)


def code():
    i = input1.get()
    if i == "":
        fail_tl.config(fg="#282828")
        fail_ts.config(fg="red")
    else:
        if len(i) > 500:
            fail_ts.config(fg="#282828")
            fail_tl.config(fg="red")
        else:
            fail_ts.config(fg="#282828")
            fail_tl.config(fg="#282828")
            letters = list(i)
            keyboard = Controller()
            try:
                c = 0
                to_loop = 501
                time.sleep(5)
                while c < to_loop:
                    keyboard.press(letters[c])
                    keyboard.release(letters[c])
                    c += 1
                    if c == to_loop:
                        c = 0
            except IndexError:
                pass


def onenter(event):
    code()


def onclick():
    code()


def onclear():
    input1.delete(0, END)


def quit():
    root.destroy()


def minimize():
    root.overrideredirect(False)
    root.state('iconic')


def un_minimize():
    root.geometry("500x120+-10+0")
    root.overrideredirect(True)


text = tk.Label(root, text="Here you can paste stuff and the program will simulate key "
                           "presses after 5 seconds:", bg="#282828", fg="white")
text.pack(pady=(15, 5))
input1 = tk.Entry(width=70, bg="#282828", fg="white", textvariable="max")
input1.pack(pady=(5, 10))

top = Frame(root, bg="#282828")
bottom = Frame(root, bg="#282828")
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)
enter = tk.Button(text="Enter", command=onclick, bg="#282828", fg="white")
clear = tk.Button(text="Clear", command=onclear, bg="#282828", fg="white")
un_minimizeButton = tk.Button(text="Remove Title", command=un_minimize, bg="#282828", fg="white")
minimizeButton = tk.Button(text="Minimize", command=minimize, bg="#282828", fg="white")
quitButton = tk.Button(text="Quit", command=quit, bg="#282828", fg="white")
enter.pack(in_=top, side=LEFT, padx="5")
clear.pack(in_=top, side=LEFT, padx="5")
un_minimizeButton.pack(in_=top, side=LEFT, padx="5")
minimizeButton.pack(in_=top, side=LEFT, padx="5")
quitButton.pack(in_=top, side=LEFT, padx="5")

fail_tl = tk.Label(root, text="Error: String to long!", fg="#282828", bg="#282828")
fail_ts = tk.Label(root, text="Error: No Input!", fg="#282828", bg="#282828")
fail_tl.pack()
fail_ts.pack()

root.bind('<Return>', onenter)
root.mainloop()
