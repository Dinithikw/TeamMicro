#improting tkiner
import tkinter as tk

from tkinter import *
from tkinter import ttk,messagebox
#pip install pillow
from PIL import Image,ImageTk 

#pip istall pymysql
import pymysql


root = Tk()
root.title('Learn to code')
root.geometry("1800x1820")

#create a main frame

frame1 = Frame(root)
frame1.pack(fill=BOTH, expand=1)

#create a canvas

my_canvas = Canvas(frame1)
my_canvas.pack(side=LEFT, fill = BOTH, expand=1)

#add a scroll bar to the canvas

my_scrollbar = ttk.Scrollbar(frame1,orient = VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#configure the canvas

my_canvas.configure(yscrollcommand = my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

#create another frama INSIDE thr canvas

second_frame = Frame(my_canvas, bg = "white")


#add that new frame to a window in the canvas

my_canvas.create_window((0,0), window = second_frame, anchor="nw")

 #background image

#second_frame.bg=Image.Tk.PhotoImage(file="background/2.jpg")
#bg=Label(second_frame.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


for thing in range(100):
    Button(second_frame, text=f'Button {thing} Yo!!').grid(row=thing, column=2000, pady=10, padx=2000)

#my_label = Label(second_frame, text="Know your Customer(KYC) profile form – (Individual)").grid(row=1, column=2500)


#adding  title
title=Label(second_frame,text="Know your Customer(KYC) profile form – (Individual)",font=("times new roman",20,"bold","underline"),bg="white",fg="black").place(x=400,y=30)

#adding section A title
title=Label(second_frame,text="Section A – Identity Information",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=250,y=300)
        
#adding section A titles

#row 1 -------->>>

#Name with Initials
Name_with_Initials=Label(second_frame,text="Name with Initials",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=340)
second_frame.Name_with_Initials=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Name_with_Initials.place(x=500,y=340,width=700)

#row 2------>>>

#Name in Full
Name_in_Full=Label(second_frame,text="Name in Full",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=380)
second_frame.Name_in_Full=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Name_in_Full.place(x=500,y=380,width=700)

#Identity Recognition
ir=Label(second_frame,text="Identity Recognition",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=420)


clicked = StringVar()
clicked.set("<--- Select Category --->")

drop = OptionMenu(second_frame, clicked ,"             NIC             ",
                                 "             Passport             ",
                                 "             Driving License             ")

drop.place(x=500,y=420)
drop.config(width = 27)

#National ID
NIC=Label(second_frame,text="National ID",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=500,y=460)
second_frame.NIC=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.NIC.place(x=500,y=500,width=200)

#Passport
Passport=Label(second_frame,text="Passport No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=500,y=540)
second_frame.Passport=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Passport.place(x=500,y=580,width=200)

#Expiration Date
Exp_pass=Label(second_frame,text="Expiration Date",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=800,y=540)
second_frame.Exp_pass=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Exp_pass.place(x=800,y=580,width=200)

#Driving License No.
Passport=Label(second_frame,text="Driving License No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=500,y=620)
second_frame.Passport=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Passport.place(x=500,y=660,width=200)

#Expiration Date
Exp_drive=Label(second_frame,text="Expiration Date",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=800,y=620)
second_frame.Exp_drive=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Exp_drive.place(x=800,y=660,width=200)

#Nationality
Nationality=Label(second_frame,text="Nationality",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=700)
second_frame.Nationality=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Nationality.place(x=500,y=700,width=500)


#Gender
#Gender=Label(second_frame,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=510)
               
#second_frame.var1 = IntVar()
#Checkbutton(second_frame, text="Male", variable=second_frame.var1,font=("times new roman",15,"bold")).place(x=450,y=510)
        
#second_frame.var2 = IntVar()
#Checkbutton(second_frame, text="Female", variable=second_frame.var2,font=("times new roman",15,"bold")).place(x=600,y=510)
        

#row 5------>>>

#Marital Status
#Marital_Status=Label(second_frame,text="Marital Status",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=510)
       
#second_frame.var1 = IntVar()
#Checkbutton(second_frame, text="Single", variable=second_frame.var1,font=("times new roman",15,"bold")).place(x=350,y=510)
        
#second_frame.var2 = IntVar()
#Checkbutton(second_frame, text="Married", variable=second_frame.var2,font=("times new roman",15,"bold")).place(x=450,y=510)

#second_frame.var3 = IntVar()
#Checkbutton(second_frame, text="Divorced", variable=second_frame.var3,font=("times new roman",15,"bold")).place(x=600,y=510)
        
#second_frame.var4 = IntVar()
#Checkbutton(second_frame, text="Widowed", variable=second_frame.var4,font=("times new roman",15,"bold")).place(x=750,y=510)


    
         
#row 7------>>>

#other residance
#other_residance=Label(second_frame,text="Are you a citizen/resident of any other country",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=590)

#second_frame.var1 = IntVar()
#Checkbutton(second_frame, text="Yes", variable=second_frame.var1,font=("times new roman",15,"bold")).place(x=500,y=590)
        
#second_frame.var2 = IntVar()
#Checkbutton(second_frame, text="No", variable=second_frame.var2,font=("times new roman",15,"bold")).place(x=600,y=590)


#row 8------>>>

#yes state
#yes_state=Label(second_frame,text="If ‘Yes’ please state",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=630)
#second_frame.yes_state=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.yes_state.place(x=350,y=630,width=500) 




#adding section C titles
#title=Label(second_frame,text="Section C – Address Information (Residential/Permanent Address)",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=790)
#row 1 ------>>>

#Address Line 01

#Address_Line_1=Label(second_frame,text="Address_Line_1",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=840)
#second_frame.Address_Line_1=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.Address_Line_1.place(x=350,y=840,width=350)

#row 2 ------>>>

#Address_Line_2=Label(second_frame,text="Address_Line_2",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=880)
#second_frame.Address_Line_2=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.Address_Line_2.place(x=350,y=880,width=350)

#row 3 ------>>>

#Address_Line_3=Label(second_frame,text="Address_Line_3",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=920)
#second_frame.Address_Line_3=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.Address_Line_3.place(x=350,y=920,width=350)

#row 4 ------>>>

#country=Label(second_frame,text="Country",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=960)
#second_frame.country=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.country.place(x=350,y=960,width=350)











root.mainloop()
