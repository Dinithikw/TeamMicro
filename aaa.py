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

second_frame = Frame(my_canvas, bg = "red")


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

#date
#date=Label(second_frame,text="Date",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=900,y=100)
#second_frame.date=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.date.place(x=1100,y=100)

#account no.
#account_no=Label(second_frame,text="A/C No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=900,y=140)
#second_frame.account_no=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.account_no.place(x=1100,y=140)

#Branch No
#Branch_No=Label(second_frame,text="Branch No",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=900,y=180)
#second_frame.Branch_No=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.Branch_No.place(x=1100,y=180)

#Officer’s S/No
#account_no=Label(second_frame,text="Officer’s S/No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=900,y=220)
#second_frame.Officer_S_No=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.Officer_S_No.place(x=1100,y=220)


#Manager’s INTL
#Branch_No=Label(second_frame,text="Manager’s INTL",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=900,y=260)
#second_frame.Manager_INTL=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.Manager_INTL.place(x=1100,y=260)

#Identification code
#account_no=Label(second_frame,text="Identification code",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=900,y=300)
#second_frame.Identification_code=Entry(second_frame,font=("times new roman",15),bg="lightgray")
#second_frame.Identification_code.place(x=1100,y=300)






#adding section A title
title=Label(second_frame,text="Section A – Identity Information",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=250,y=100)
        
#adding section A titles

#row 1 -------->>>

#Name with Initials
Name_with_Initials=Label(second_frame,text="Name with Initials",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=1400)
second_frame.Name_with_Initials=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Name_with_Initials.place(x=500,y=400,width=700)

#row 2------>>>

#Initials Standard For
Initials_Standard_For=Label(second_frame,text="Initials Standard For",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=440)
second_frame.Initials_Standard_For=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Initials_Standard_For.place(x=500,y=440,width=700)     
        
#row 3------>>>

#Date of Birth
DOB=Label(second_frame,text="Date of Birth",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=470)
second_frame.DOB=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.DOB.place(x=500,y=470,width=500) 

#row 4------>>>

#Gender
Gender=Label(second_frame,text="Gender",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=250,y=510)
               
second_frame.var1 = IntVar()
Checkbutton(second_frame, text="Male", variable=second_frame.var1,font=("times new roman",15,"bold")).place(x=450,y=510)
        
second_frame.var2 = IntVar()
Checkbutton(second_frame, text="Female", variable=second_frame.var2,font=("times new roman",15,"bold")).place(x=600,y=510)
        

#row 5------>>>

#Marital Status
Marital_Status=Label(second_frame,text="Marital Status",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=510)
       
second_frame.var1 = IntVar()
Checkbutton(second_frame, text="Single", variable=second_frame.var1,font=("times new roman",15,"bold")).place(x=350,y=510)
        
second_frame.var2 = IntVar()
Checkbutton(second_frame, text="Married", variable=second_frame.var2,font=("times new roman",15,"bold")).place(x=450,y=510)

second_frame.var3 = IntVar()
Checkbutton(second_frame, text="Divorced", variable=second_frame.var3,font=("times new roman",15,"bold")).place(x=600,y=510)
        
second_frame.var4 = IntVar()
Checkbutton(second_frame, text="Widowed", variable=second_frame.var4,font=("times new roman",15,"bold")).place(x=750,y=510)

 #row 6------>>>

#Nationality
Nationality=Label(second_frame,text="Nationality",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=550)
second_frame.Nationality=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Nationality.place(x=350,y=550,width=500)    
         
#row 7------>>>

#other residance
other_residance=Label(second_frame,text="Are you a citizen/resident of any other country",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=590)

second_frame.var1 = IntVar()
Checkbutton(second_frame, text="Yes", variable=second_frame.var1,font=("times new roman",15,"bold")).place(x=500,y=590)
        
second_frame.var2 = IntVar()
Checkbutton(second_frame, text="No", variable=second_frame.var2,font=("times new roman",15,"bold")).place(x=600,y=590)


#row 8------>>>

#yes state
yes_state=Label(second_frame,text="If ‘Yes’ please state",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=630)
second_frame.yes_state=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.yes_state.place(x=350,y=630,width=500) 

#adding section B title
title=Label(second_frame,text="Section B – Proof of Identity (if you have)",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=670)
        
#adding section B titles

#row 1 -------->>>

#National ID Card No.
NIC=Label(second_frame,text="National ID Card No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=710)
second_frame.NIC=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.NIC.place(x=350,y=710,width=500)

#row 2------>>>

#Passport No.
Passport_No=Label(second_frame,text="Passport No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=750)
second_frame.Passport_No=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Passport_No.place(x=350,y=750,width=250)     
        
#Expiration
Expiration=Label(second_frame,text="Expiration Date",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=700,y=750)
second_frame.Expiration=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Expiration.place(x=350,y=750,width=250)

#row 3------>>>

#Driving License No.
Driving_License_No=Label(second_frame,text=" Driving License No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=770)
second_frame.Driving_License_No=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Driving_License_No.place(x=350,y=750,width=250) 

#Expirations
Expirations=Label(second_frame,text="Expiration Date",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=700,y=770)
second_frame.Expirations=Entry(frame1,font=("times new roman",15),bg="lightgray")
second_frame.Expirations.place(x=350,y=750,width=250)


#adding section C titles
title=Label(second_frame,text="Section C – Address Information (Residential/Permanent Address)",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=50,y=790)
#row 1 ------>>>

#Address Line 01

Address_Line_1=Label(second_frame,text="Address_Line_1",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=840)
second_frame.Address_Line_1=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Address_Line_1.place(x=350,y=840,width=350)

#row 2 ------>>>

Address_Line_2=Label(second_frame,text="Address_Line_2",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=880)
second_frame.Address_Line_2=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Address_Line_2.place(x=350,y=880,width=350)

#row 3 ------>>>

Address_Line_3=Label(second_frame,text="Address_Line_3",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=920)
second_frame.Address_Line_3=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.Address_Line_3.place(x=350,y=920,width=350)

#row 4 ------>>>

country=Label(second_frame,text="Country",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=960)
second_frame.country=Entry(second_frame,font=("times new roman",15),bg="lightgray")
second_frame.country.place(x=350,y=960,width=350)











root.mainloop()
