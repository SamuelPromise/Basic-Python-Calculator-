
import tkinter as tk
from tkinter import  ttk
from tkinter.messagebox import showinfo
from math import factorial

def get_result():
    exp = ent_exp.get()
    try:
        result = eval(exp)
        ent_exp.delete(0,tk.END)
        ent_exp.insert(tk.END,result)
    except Exception:
        ent_exp.insert(tk.END,exp)
        ent_exp.insert(tk.END,"Error")

def fact():
    exp = ent_exp.get()
    try:
        result = factorial(int(exp))
        ent_exp.delete(0,tk.END)
        ent_exp.insert(tk.END,result)
    except Exception:
        ent_exp.delete(0,tk.END)
        ent_exp.insert(tk.END,"Error")

def stepBack():
    exp = ent_exp.get()
    if len(exp):
        result = exp[:-1]
        ent_exp.delete(0,tk.END)
        ent_exp.insert(tk.END,result)
    else:
        ent_exp.delete(0,tk.END)
        ent_exp.insert(tk.END,"Error")

   
def get_exp(n):
    ent_exp.insert(tk.END,n)


root = tk.Tk()
root.title("CALCULATOR")
root.resizable(0,0)


#frm_ent_exp = tk.Frame(master=root, relief=tk.FLAT,height=15)
ent_exp = tk.Entry(master=root,bg="white", fg="black")
ent_exp.grid(row=0,columnspan=6,sticky="nsew")

#operands
ttk.Button(root,text="7",width=10,command=lambda:get_exp(7)).grid(row=1,column=0)
ttk.Button(root,text="8",width=10,command=lambda:get_exp(8)).grid(row=1,column=1)
ttk.Button(root,text="9",width=10,command=lambda:get_exp(6)).grid(row=1,column=2)
ttk.Button(root,text="4",width=10,command=lambda:get_exp(4)).grid(row=2,column=0)
ttk.Button(root,text="5",width=10,command=lambda:get_exp(5)).grid(row=2,column=1)
ttk.Button(root,text="6",width=10,command=lambda:get_exp(6)).grid(row=2,column=2)
ttk.Button(root,text="1",width=10,command=lambda:get_exp(1)).grid(row=3,column=0)
ttk.Button(root,text="2",width=10,command=lambda:get_exp(2)).grid(row=3,column=1)
ttk.Button(root,text="3",width=10,command=lambda:get_exp(3)).grid(row=3,column=2)
ttk.Button(root,text="0",width=10,command=lambda:get_exp(0)).grid(row=4,column=1)

#operators
ttk.Button(root,text="+",width=10,command=lambda:get_exp('+')).grid(row=1,column=3)
ttk.Button(root,text="pi",width=10,command=lambda:get_exp('3.142')).grid(row=1,column=4)
ttk.Button(root,text="^",width=10,command=lambda:get_exp('**')).grid(row=1,column=5)

ttk.Button(root,text="-",width=10,command=lambda:get_exp('-')).grid(row=2,column=3)
ttk.Button(root,text="(",width=10,command=lambda:get_exp('(')).grid(row=2,column=4)
ttk.Button(root,text=")",width=10,command=lambda:get_exp(')')).grid(row=2,column=5)

ttk.Button(root,text="*",width=10,command=lambda:get_exp('*')).grid(row=3,column=3)
ttk.Button(root,text=".",width=10,command=lambda:get_exp('.')).grid(row=3,column=4)
ttk.Button(root,text="%",width=10,command=lambda:get_exp('/100')).grid(row=3,column=5)

ttk.Button(root,text="/",width=10,command=lambda:get_exp('/')).grid(row=4,column=3)
ttk.Button(root,text="!",width=10,command=lambda:fact()).grid(row=4,column=4)
ttk.Button(root,text="<--",width=10,command=lambda:stepBack()).grid(row=4,column=5)

ttk.Button(root,text="C",width=10,command=lambda:ent_exp.delete(0,tk.END)).grid(row=4,column=0)
ttk.Button(root,text="=",command=get_result,width=10).grid(row=4,column=2)

root.mainloop()