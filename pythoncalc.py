import tkinter as tk
BG_COLOR = "#1e1e2e"
DISPLAY_BG = "#2a2a3d"
BTN_NUM_BG = "#313244"
BTN_OP_BG = "#f38ba8"
BTN_EQ_BG = "#a6e3a1"
BTN_CLR_BG = "#fab387"
TEXT_COLOR = "#cdd6f4"
FONT_MAIN = ("Courier New",22,"bold")
FONT_BTN = ("Courier New",16,"bold")

def press(symbol):
    current=display_var.get()
    display_var.set(current+symbol)

def clear():
    display_var.set("")

def backspace():
    current=display_var.get()
    display_var.set(current[:-1])

def calculate():
    expression=display_var.get()
    try:
        result=eval(expression)
        if isinstance(result,float) and result.is_integer():
            result=int(result)

        display_var.set(str(result))
    except ZeroDivisionError:
        display_var.set("Error: / by 0")
    except Exception:
        display_var.set("Error")

root = tk.Tk()
root.title("Simple Calculator")
root.resizable(False,False)
root.configure(bg=BG_COLOR)
display_var=tk.StringVar()
display_var.set("")

display = tk.Label(
    root,
    textvariable=display_var,
    font=FONT_MAIN,
    bg=DISPLAY_BG,
    fg=TEXT_COLOR,
    anchor="e",
    padx=12,
    pady=14,
    width=16,
    relief="flat",
)
display.grid(row=0,column=0,columnspan=4,padx=12,pady=(12,4),sticky="ew")

def make_button(label,row,col,command,color=BTN_NUM_BG,colspan=1):
    btn=tk.Button(
        root,
        text=label,
        font=FONT_BTN,
        bg=color,
        fg=TEXT_COLOR,
        activebackground=TEXT_COLOR,
        activeforeground=BG_COLOR,
        relief="flat",
        cursor="hand2",
        width=4,
        height=1,
        command=command,
    )
    btn.grid(
        row=row, column=col,
        columnspan=colspan,
        padx=5,pady=5,
        sticky="nsew",
        ipady=8,
    )
    return btn

make_button("C",1,0,clear,          color=BTN_CLR_BG)
make_button("<-",1,1,backspace,    color=BTN_CLR_BG)
make_button("%",1,2,lambda:press("%"),color=BTN_OP_BG)
make_button("/",1,3,lambda:press("/"),color=BTN_OP_BG)

make_button("7",2,0,lambda:press("7"))
make_button("8",2,1,lambda:press("8"))
make_button("9",2,2,lambda:press("9"))
make_button("*",2,3,lambda:press("*"),color=BTN_OP_BG)

make_button("4",3,0,lambda:press("4"))
make_button("5",3,1,lambda:press("5"))
make_button("6",3,2,lambda:press("6"))
make_button("-",3,3,lambda:press("-"),color=BTN_OP_BG)

make_button("1",4,0,lambda:press("1"))
make_button("2",4,1,lambda:press("2"))
make_button("3",4,2,lambda:press("3"))
make_button("+",4,3,lambda:press("+"),color=BTN_OP_BG)

make_button("0",5,0,lambda:press("0"),colspan=2)
make_button(".",5,2,lambda:press("."))
make_button("=",5,3,calculate,color=BTN_OP_BG)

for i in range(4):
    root.columnconfigure(i,weight=1)
root.mainloop()
