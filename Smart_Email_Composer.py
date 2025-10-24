from tkinter import *

base = Tk()
base.geometry("698x450")
base.title("Smart Email Composer")
base.configure(bg="#FFF8DE")

def event1(e): m1.tk_popup(e.x_root, e.y_root)
def clear(): msg.delete(0.0, END)
def school_leave():
    str1 = "With due respect, I want to say that I am student of class ... in your school.\nI am not feeling well today and also have some weakness.\nHence I request you to please grant me 2 days leave.\n\n"+"I hope you will consider my appliation.I will definitely try to remain present \nafter 2 days.\n\n"+"Thanking You."
    msg.insert(END, str1)
def office_leave():
    str1 = "With humble respect, this is to inform you that due to my severe health conditions\nI am unable to join the office for tomorrow. Because I have been facing an extreme\nheadache and fever since last few days.\n\n"+"Kindly grant me leave on ... so that I can visit the doctor and take proper \nmedication.Thank you for your consideration.\n\n"+"Thanking You."
    msg.insert(END, str1)
def subject_fun():
    clear()
    if "leave" in subjectt.get().casefold():
        m2 = Menu(subjectt, tearoff=0)
        m2.add_command(label="School",command=school_leave)
        m2.add_command(label="Office",command=office_leave)
        m2.tk_popup(x=720,y=420)
    elif "refund" in subjectt.get().casefold():
        msg.insert(END,"I want refund")
    elif "job" in subjectt.get().casefold():
        str1 = "My name is ... and I am writing this email to apply for an opening at your companyfor the position of Data Anaylist. I came to know about the opening from a friend\nof mine. After reading the detailed job description, I am very confident that I have the neccessary skiils and experience to give it a try.\n\n"+"I have attached my resume to this letter for your reference. Kindly let me know if\nyou need any additional details. I will share it at the earlier.\n\nThank You for your time and consideration in reading this Letter. I will look forwar to your response."
        msg.insert(END,str1)
    elif "paper publish" in subjectt.get().casefold():
        msg.insert(END, "Please publish our paper")
    elif "scholarship" in subjectt.get().casefold():
        msg.insert(END, "I want to fill scholarship from")

ft = ("Arial Bold",12)
from_user = Label(base,text="FROM :",font=ft,bg="#FFF8DE")
from_user.place(x=20,y=20)
from_usert = Entry(base,width=93)
from_usert.place(x=120,y=24)
to_user = Label(base,text="TO :",font=ft,bg="#FFF8DE")
to_user.place(x=20,y=60)
to_usert = Entry(base,width=93)
to_usert.place(x=120,y=64)
subject = Label(base,text="SUBJECT :",font=ft,bg="#FFF8DE")
subject.place(x=20,y=100)
subjectt = Entry(base,width=93)
subjectt.place(x=120,y=104)
msg = Text(base,width=82,height=15)
msg.place(x=20,y=140)
msg.bind("<Button-3>", event1)
compose = Button(base,text="COMPOSE",font=ft,bd=4,command=subject_fun)
compose.place(x=580,y=399)

def elaborate():
    clear()
    str1 = "My name is ... and I am writing this email to apply for an opening at your companyfor the position of Data Anaylist. I came to know about the opening from a friend\nof mine. After reading the detailed job description, I am very confident that I have the neccessary skiils and experience to give it a try. I am very enthusiastic \nat the prospect of joining your team and leveraging knowledge in section of coding\nto help you to bring more profit to your company.\n\n"+"I have attached my resume to this letter for your reference. Kindly let me know if\nyou need any additional details. I will share it at the earlier.\n\nThank You for your time and consideration in reading this Letter. I will look forward to your response."
    msg.insert(END,str1)
m1 = Menu(base, tearoff=0)
m1.add_command(label="ELABORATE",command=elaborate)
m1.add_command(label="CLEAR",command=clear)

base.mainloop()