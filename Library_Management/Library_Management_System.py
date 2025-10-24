from tkinter import *
from datetime import date
base = Tk()     #global "base" object to switch frame using one base only.

def exop(event):exit(0)
def issue_book_frame(event):
    global base

    old_base = base
    old_base.destroy()

    base = Tk()
    base.title("Issue Book")
    base.geometry("550x500")
    base.configure(bg="#FFF8DE")

    def issue_book():
        enroll = etxt.get()
        book_no = btxt.get()
        issue_date = date.today()
        return_status = "not returned"

        fobj = open("all_books.txt", "r")
        book_ls = fobj.readlines()
        fobj.close()

        fobj = open("all_stud.txt", "r")
        stud_ls = fobj.readlines()
        fobj.close()

        i = j = 0
        while i <= 5:
            b = book_ls[i].split(",")
            if b[0] == book_no:
                bno_lb.configure(text=b[1] + " - " + b[2])
                check1.configure(fg="green")
                while j <= 4:
                    e = stud_ls[j].split(",")
                    if e[0] == enroll:
                        print(e[0], enroll)
                        eno_lb.configure(text=e[1] + " - " + e[2] + " - " + e[3])
                        check2.configure(fg="green")
                        break
                    j += 1
            i+=1

        fobj = open("all_issued.txt.txt", "a")
        fobj.write(enroll + "," + book_no + "," + str(issue_date) + "," + "NA" + "," + return_status + "\n")
        fobj.close()

        iss_lb.configure(text="BOOK IS ISSUED")

    bno = Label(base, text="ENTER BOOK NO : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    bno.place(x=30, y=40)

    bno_lb = Label(base,font=("Times New Roman", 14, "bold"), bg="#FFF8DE", fg="brown")
    bno_lb.place(x=160, y=110)

    btxt = Entry(base,font=("Times New Roman", 14, "bold"))
    btxt.place(x=230,y=40)

    check1 = Label(base,text="CHECK", font=("Times New Roman", 14, "bold"), bg="#FFF8DE", fg="red")
    check1.place(x=450, y=40)

    eno = Label(base, text="ENTER ENR. NO : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    eno.place(x=30, y=190)

    eno_lb = Label(base, font=("Times New Roman", 14, "bold"), bg="#FFF8DE", fg="brown")
    eno_lb.place(x=160, y=250)

    etxt = Entry(base, font=("Times New Roman", 14, "bold"))
    etxt.place(x=230, y=190)

    check2 = Label(base,text="CHECK", font=("Times New Roman", 14, "bold"), bg="#FFF8DE", fg="red")
    check2.place(x=450, y=190)

    issue = Button(base, text="ISSUE", font=("Times New Roman", 14, "bold"), bg="black",fg="#FFF8DE",width= 10)
    issue.configure(command=issue_book)
    issue.place(x=200,y=300)

    iss_lb = Label(base,font=("Times New Roman", 14, "bold"),bg="#FFF8DE",fg="green")
    iss_lb.place(x=180,y=370)

    main_menu = Label(base, text="MAIN MENU", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    main_menu.bind("<Button>",main_frame_menu)
    main_menu.place(x=300, y=430)

    exitb = Label(base, text="EXIT", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    exitb.bind("<Button>", exop)
    exitb.place(x=460, y=430)

    base.mainloop()

def return_book_frame(event):
    global base

    old_base = base
    old_base.destroy()

    base = Tk()
    base.title("Return Book")
    base.geometry("550x500")
    base.configure(bg="#FFF8DE")

    def return_book():
        book_no = btxt.get()

        fobj = open("all_issued.txt", "r")
        book_ls = fobj.readlines()
        fobj.close()

        i = 0
        while i <= 5:
            b = book_ls[i].split(",")
            if b[1] == book_no:
                b[3] = str(date.today())
                b[4] = "Returned"
                book_ls[i] = b[0] + "," + b[1] + "," + b[2] + "," + b[3] + "," + b[4] + "\n"
                bno_lb.configure(text="Book No: "+book_no + " \n " + "Issue date: "+b[2] + " \n " + "Return date: "+b[3])
                check1.configure(fg="green")
                book_found = True
                break
            i += 1

        if book_found == True:
            fobj = open("all_issued.txt", "w")
            fobj.writelines(book_ls)
            fobj.close()
            ret_lb.configure(text="BOOK IS RETURNED")
        else:
            ret_lb.configure(text="Invalid Credentials...")

    bno = Label(base, text="ENTER BOOK NO : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    bno.place(x=30, y=40)

    bno_lb = Label(base, font=("Times New Roman", 14, "bold"), bg="#FFF8DE", fg="brown")
    bno_lb.place(x=110, y=110)

    btxt = Entry(base, font=("Times New Roman", 14, "bold"))
    btxt.place(x=230, y=40)

    check1 = Label(base, text="CHECK", font=("Times New Roman", 14, "bold"), bg="#FFF8DE", fg="red")
    check1.place(x=450, y=40)

    returnb = Button(base, text="RETURN", font=("Times New Roman", 14, "bold"), bg="black", fg="#FFF8DE", width=10)
    returnb.configure(command=return_book)
    returnb.place(x=200, y=300)

    ret_lb = Label(base, font=("Times New Roman", 14, "bold"), bg="#FFF8DE", fg="green")
    ret_lb.place(x=160, y=370)

    main_menu = Label(base, text="MAIN MENU", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    main_menu.bind("<Button>", main_frame_menu)
    main_menu.place(x=300, y=430)

    exitb = Label(base, text="EXIT", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    exitb.bind("<Button>", exop)
    exitb.place(x=460, y=430)

    base.mainloop()

def add_stud_frame(event):
    global base

    old_base = base
    old_base.destroy()

    base = Tk()
    base.title("Return Book")
    base.geometry("550x500")
    base.configure(bg="#FFF8DE")

    def add_stud():
        enroll = etxt.get()
        name = stxt.get()
        s_class = ctxt.get()
        mob = mtxt.get()
        fobj = open("all_stud.txt", "a")
        fobj.write(enroll + "," + name + "," + s_class + "," + mob + "\n")
        fobj.close()
        save_lb.configure(text="Student Data Saved Successfully...!")

    eno = Label(base, text="ENTER ENROLLMENT NO : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    eno.place(x=30, y=40)
    etxt = Entry(base, font=("Times New Roman", 14, "bold"))
    etxt.place(x=300, y=40)

    snm = Label(base, text="ENTER STUDENT NAME : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    snm.place(x=30, y=90)
    stxt = Entry(base, font=("Times New Roman", 14, "bold"))
    stxt.place(x=300, y=90)

    sc = Label(base, text="ENTER STUDENT CLASS : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    sc.place(x=30, y=140)
    ctxt = Entry(base, font=("Times New Roman", 14, "bold"))
    ctxt.place(x=300, y=140)

    mobl = Label(base, text="ENTER MOBILE NO : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    mobl.place(x=30, y=190)
    mtxt = Entry(base, font=("Times New Roman", 14, "bold"))
    mtxt.place(x=300, y=190)

    main_menu = Label(base, text="MAIN MENU", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    main_menu.bind("<Button>", main_frame_menu)
    main_menu.place(x=300, y=430)

    exitb = Label(base, text="EXIT", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    exitb.bind("<Button>", exop)
    exitb.place(x=460, y=430)

    saveb = Button(base, text="SAVE DATA", font=("Times New Roman", 14, "bold"), bg="black", fg="#FFF8DE", width=10)
    saveb.configure(command=add_stud)
    saveb.place(x=200, y=270)

    save_lb = Label(base, font=("Times New Roman", 14, "bold"), bg="#FFF8DE", fg="green")
    save_lb.place(x=140, y=370)

    base.mainloop()

def add_book_frame(event):
    global base

    old_base = base
    old_base.destroy()

    base = Tk()
    base.title("Return Book")
    base.geometry("550x500")
    base.configure(bg="#FFF8DE")

    def add_book():
        b_no = btxt.get()
        b_title = ttxt.get()
        b_author = atxt.get()
        b_pub = ptxt.get()

        fobj = open("all_books.txt", "a")
        fobj.write(b_no + "," + b_title + "," + b_author + "," + b_pub + "\n")
        fobj.close()

        add_lb.configure(text="Book Added Successfully...!")

    bno = Label(base, text="ENTER BOOK NO : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    bno.place(x=30, y=40)
    btxt = Entry(base, font=("Times New Roman", 14, "bold"))
    btxt.place(x=330, y=40)

    btit = Label(base, text="ENTER BOOK TITLE : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    btit.place(x=30, y=90)
    ttxt = Entry(base, font=("Times New Roman", 14, "bold"))
    ttxt.place(x=330, y=90)

    bauth = Label(base, text="ENTER BOOK AUTHOR : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    bauth.place(x=30, y=140)
    atxt = Entry(base, font=("Times New Roman", 14, "bold"))
    atxt.place(x=330, y=140)

    bpub = Label(base, text="ENTER BOOK PUBLICATION : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    bpub.place(x=30, y=190)
    ptxt = Entry(base, font=("Times New Roman", 14, "bold"))
    ptxt.place(x=330, y=190)

    addb = Button(base, text="ADD BOOK", font=("Times New Roman", 14, "bold"), bg="black", fg="#FFF8DE", width=10)
    addb.configure(command=add_book)
    addb.place(x=200, y=270)

    add_lb = Label(base, font=("Times New Roman", 14, "bold"), bg="#FFF8DE", fg="green")
    add_lb.place(x=140, y=370)

    main_menu = Label(base, text="MAIN MENU", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    main_menu.bind("<Button>", main_frame_menu)
    main_menu.place(x=300, y=430)

    exitb = Label(base, text="EXIT", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    exitb.bind("<Button>", exop)
    exitb.place(x=460, y=430)

    base.mainloop()
'''
def not_return_frame(event):
    global base

    old_base = base
    old_base.destroy()

    def view_not_returned_books():
        book_found = False
        fobj = open("all_issued.txt", "r")
        book_ls = fobj.readlines()
        fobj.close()

        i = 0
        while i <= 5:
            b = book_ls[i].split(",")
            if b[4] == "not returned\n":
                ret_lb.configure(text="Enrollment no: " +b[0]+"   "+"Issue Date: " + b[2])
                book_found = True
                
                if book_ls[i] == book_ls[-1]:
                    break
            i += 1

        if book_found == False:
            ret_lb.configure(text="No Books are remaining to return...!", fg="green")

    base = Tk()
    base.title("Return Book")
    base.geometry("550x500")
    base.configure(bg="#FFF8DE")

    bno = Label(base, text="List of Returned Books : ", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    bno.place(x=50, y=40)

    show = Button(base, text="SHOW", font=("Times New Roman", 14, "bold"), bg="black", fg="#FFF8DE", width=10)
    show.configure(command=view_not_returned_books)
    show.place(x=290, y=35)

    ret_lb = Label(base, font=("Times New Roman", 14, "bold"), bg="white", fg="BROWN")
    ret_lb.place(x=50, y=100)

    main_menu = Label(base, text="MAIN MENU", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    main_menu.bind("<Button>", main_frame_menu)
    main_menu.place(x=300, y=430)

    exitb = Label(base, text="EXIT", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    exitb.bind("<Button>", exop)
    exitb.place(x=460, y=430)

    base.mainloop()
'''
def main_frame_menu(event):
    global base

    base.destroy()
    base = Tk()
    base.title("Library Management System")
    base.geometry("550x500")
    base.configure(bg="#FFF8DE")

    menu = Label(base,text="MAIN MENU",font=("Times New Roman",18,"bold"),bg="#FFF8DE")
    menu.place(x=210,y=40)

    menu1 = Label(base,text="1)    ISSUE BOOK",font=("Times New Roman",14,"bold"),bg="#FFF8DE")
    menu1.bind("<Button>",issue_book_frame)
    menu1.place(x=90,y=90)

    menu2 = Label(base, text="2)    RETURN BOOK", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    menu2.bind("<Button>", return_book_frame)
    menu2.place(x=90, y=130)

    menu3 = Label(base, text="3)    ADD NEW STUDENT", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    menu3.bind("<Button>", add_stud_frame)
    menu3.place(x=90, y=170)

    menu4 = Label(base, text="4)    ADD NEW BOOK", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    menu4.bind("<Button>", add_book_frame)
    menu4.place(x=90, y=210)

    menu5 = Label(base, text="5)    SHOW NOT RETURNED BOOKS", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    menu5.bind("<Button>", "")
    menu5.place(x=90, y=250)

    menu6 = Label(base, text="6)    STUDENT HISTORY", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    menu6.bind("<Button>", "")
    menu6.place(x=90, y=290)

    menu7 = Label(base, text="7)    BOOK HISTORY", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    menu7.bind("<Button>", "")
    menu7.place(x=90, y=330)

    menu8 = Label(base, text="8)    SEARCH BOOK", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    menu8.bind("<Button>", "")
    menu8.place(x=90, y=370)

    menu9 = Label(base, text="9)    SEARCH STUDENT", font=("Times New Roman", 14, "bold"), bg="#FFF8DE")
    menu9.bind("<Button>", "")
    menu9.place(x=90, y=410)

    exitb = Label(base, text="EXIT", font=("Times New Roman", 18, "bold"), bg="#FFF8DE")
    exitb.bind("<Button>", exop)
    exitb.place(x=450, y=450)

    base.mainloop()

main_frame_menu("")