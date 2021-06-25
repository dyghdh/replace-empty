import tkinter
import pyperclip


def onClick1():
    txt = en.get()
    txt = txt.replace("-", "")
    la.configure(text=txt)
    pyperclip.copy(txt)

tk = tkinter.Tk()
tk.title("Replace")
tk.geometry("400x200")

en = tkinter.Entry(width=35)
en.place(x=80,y=30)

la = tkinter.Label(tk,width=35, text="Ready")
la.place(x=80,y=80)

button = tkinter.Button(width=35, text="Copy",command=onClick1)
button.place(x=80,y=130)

tk.mainloop()