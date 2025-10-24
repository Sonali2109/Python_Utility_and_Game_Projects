from tkinter import *

base = Tk()
base.geometry("700x400")
base.title("Editor for C")

txt = Text(base,font=("Arial Bold",12))
txt.pack()

def eventmethod1(e): m1.tk_popup(e.x_root, e.y_root)
def header(): txt.insert(txt.index(INSERT),"#include<stdio.h>\n")
def main_fun(): txt.insert(txt.index(INSERT),"void main(){"+"\n...\n...\n"+"}\n")
def if_fun(): txt.insert(txt.index(INSERT),"   if(condition){"+"\n    ...\n    ...\n"+"    }\n")
def if_else_fun(): txt.insert(txt.index(INSERT),"   if(condition){"+"\n    ...\n    ...\n"+"    }\n"+"    else{\n"+"    ...\n"+"    }\n")
def if_elseif(): txt.insert(txt.index(INSERT),"   if(condition){"+"\n    ...\n    ...\n"+"    }\n"+"    elseif(condition){\n"+"    ...\n"+"    }\n"+"    else{\n"+"    ...\n"+"    }\n")
def switch_fun(): txt.insert(txt.index(INSERT),"   switch(condition){"+"\n\n        case 1:\n"+"            statements"+"\n        case 2:\n"+"            statements"+"\n        case n:\n"+"            statements"+"\n        default:\n"+"            statements"+"\n\n    }\n")

def for_fun(): txt.insert(txt.index(INSERT),"    for(initalization;condition;incr/decr){\n\n"+"        statements\n"+"        ...\n        ..."+"\n    }\n")
def while_fun(): txt.insert(txt.index(INSERT),"    initalization;\n"+"    while(condition){\n\n"+"        statements\n"+"        ...\n        ...\n        incr/decr;\n"+"\n    }\n")
def dowhile_fun(): txt.insert(txt.index(INSERT),"    initalization;\n" + "    do{\n\n" + "        statements\n" + "        ...\n        ...\n        incr/decr;\n" + "\n    }while(condition)\n")

m2 = Menu(base,tearoff = 0)
m2.add_command(label="If statement",command=if_fun)
m2.add_command(label = "If-else statement",command = if_else_fun)
m2.add_command(label = "If-elseif-else statement",command = if_elseif)
m2.add_command(label = "Switch statement",command=switch_fun)

m3 = Menu(base,tearoff = 0)
m3.add_command(label="For loop",command=for_fun)
m3.add_command(label = "While loop",command=while_fun)
m3.add_command(label = "Do-While loop",command=dowhile_fun)

m1 = Menu(base, tearoff=0)
m1.add_command(label="Include header file",command=header)
m1.add_command(label="Add main method",command=main_fun)
m1.add_cascade(label="Looping Structure",menu = m3)
m1.add_cascade(label="Decision-making Structure",menu = m2)

base.bind("<Button-3>", eventmethod1)
base.mainloop()