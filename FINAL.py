from tkinter import*
from tkinter import messagebox,ttk
import random
import sqlite3
db=sqlite3.connect("database.db")
try:
       cr=db.cursor()
       cr.execute("""create table prernaairlines(Name text,Contact integer,Date integer,Source text,Destination text,No_of_Tickets integer,Vegetarian integer,
                           Non_Vegetarian integer,Vegan integer,Gluten integer,Diabetic integer,Baby integer)""")
       db.commit()
except:
        print("Successfully Submitted!!!")

w=Tk()
w.title("Safe Airlines")
w.geometry("800x600")
w.config(background=("steel blue"))
w.state("zoomed")

country=["Pakistan","Maldives","China","Russia","Australia",
         "United states","India"]
         
dict={ "India-Pakistan":1452,
       "India-Maldives":2030,
       "India-China":7497.7,
       "India-Russia":4983,
       "India-Australia":7809,
       "India-United_States":13568,
       
       "Pakistan-India":1452,
       "Pakistan-Maldives":3047,
       "Pakistan-China":3283,
       "Pakistan-Russia":4332,
       "Pakistan-Australia":9230,
       "Pakistan-Unites_States":12346,
       
       "China-Pakistan":3283,
       "China-Maldives":4823,
       "China-India":7497.7,
       "China-Russia":2853,
       "China-Australia":7470,
       "China-United_States":11640,

       "Russia-Pakistan":4332,
       "Russia-Maldives":7012,
       "Russia-India":4983,
       "Russia-China":2853,
       "Russia-Australia":9977,
       "Russia-United_States":3.8,

       "Australia-Pakistan":9230,
       "Australia-Maldives":7242,
       "Australia-India":7809,
       "Austraia-China":7470,
       "Australia-Russia":9977,
       "Australia-United_States":15175,

       "United_States-Pakistan":12346,
       "United_States-Maldives":15389,
       "United_States-India":13568,
       "United_States-China":11640,
       "United_States-Australia":15175,
       "United_States-Russia":3.8,

       "Maldives-Pakistan":3047,
       "Maldives-United_States":15389,
       "Maldives-India":2030,
       "Maldives-China":4823,
       "Maldives-Australia":7242,
       "Maldives-Russia":7012
}
#Global Variables
person=IntVar()
name=StringVar()
contact=StringVar()
ticket_no=StringVar()
date=StringVar()
veg=StringVar()
nonveg=StringVar()
vegan=StringVar()
gluten=StringVar()
diabetic=StringVar()
baby=StringVar()

#creating frame1
frame1=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame1.place(x=10,y=10,height=80,width=1510)

#book your flight label
book=Label(frame1,text="BOOK YOUR TICKET",font=("elephant",25,"bold"),bg="black",fg="white")
book.place(x=570,y=15)

#creating frame2
frame2=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame2.place(x=10,y=100,height=110,width=1510)

#passenger details
pas=LabelFrame(frame2,text="PASSENGER DETAILS:",font=("times new roman",15,"bold"),bg="black",fg="yellow")
pas.place(x=20,y=5,height=90,width=1470)

#name
n_label=Label(frame2,text="May I know your good name please...?",font=("times new roman",16,"bold"),bg="black",fg="white")
n_label.place(x=30,y=35)

#entry box for name
e1=Entry(frame2,font=("times new roman",22,"bold"),bg="lightgray",bd=3,textvar=name)
e1.place(x=388,y=33)

#contact
contact_label=Label(frame2,text="Contact No.",font=("times new roman",16,"bold"),bg="black",fg="white")
contact_label.place(x=720,y=35)

#entry box for contact no
e2=Entry(frame2,font=("times new roman",22,"bold"),bg="lightgray",bd=3,textvar=contact)
e2.place(x=850,y=33)

#date
date_label=Label(frame2,text="Date.",font=("times new roman",16,"bold"),bg="black",fg="white")
date_label.place(x=1180,y=35)

#entry box for date
e3=Entry(frame2,font=("times new roman",22,"bold"),bg="lightgray",bd=3,textvar=date)
e3.place(x=1250,y=33,width=200)

#creating frame3
frame3=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame3.place(x=10,y=220,height=400,width=500)

#travel details
pas1=LabelFrame(frame3,text="PASSENGER TRAVEL DETAILS:",font=("times new roman",15,"bold"),bg="black",fg="yellow")
pas1.place(x=13,y=5,height=380,width=470)

#Source 
source=Label(frame3,text="Source:",font=("times new roman",18,"bold"),bg="black",fg="steel blue")
source.place(x=40,y=60,width=100,height=39)
combo_s=ttk.Combobox(frame3,font=("times new Roman",22),state="readonly",value=country,width=18)
combo_s.grid(row=0,column=1,padx=190,pady=60)
combo_s.set("        Select Source")

#destination
des=Label(frame3,text="Destination:",font=("times new roman",18,"bold"),bg="black",fg="steel blue")
des.place(x=40,y=156,width=120,height=39)
combo_d=ttk.Combobox(frame3,font=("times new Roman",22),state="readonly",value=country,width=18)
combo_d.grid(row=2,column=1,padx=190)
combo_d.set("    Select Destination")

#number of ticket
no_of_ticket=Label(frame3,text="No. of Ticket:",font=("times new roman",18,"bold"),bg="black",fg="steelblue")
no_of_ticket.place(x=40,y=260)

#entry box for number of ticket
e4=Entry(frame3,font=("times new roman",22,"bold"),bg="lightgray",bd=3,textvar=person)
e4.place(x=193,y=250,width=263)

#creating frame 4
frame4=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame4.place(x=10,y=630,height=150,width=1510)

#creating frame 5
frame5=Frame(w,background="black",highlightbackground="white",highlightthickness=2)
frame5.place(x=525,y=220,height=400,width=500)

#creating frame 6(the ticket)
frame6=Frame(w,background="white",highlightbackground="grey",highlightthickness=5)
frame6.place(x=1040,y=220,height=400,width=478)
t=Label(frame6,text="TICKET",font=("times new roman",15,"bold"),bg="white",fg="Black")
t.pack()
scrol_y=Scrollbar(frame6,orient=VERTICAL)
textarea=Text(frame6,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()

#refreshments in flight
food=LabelFrame(frame5,text="REFRESHMENTS IN FLIGHT:",font=("times new roman",15,"bold"),bg="black",fg="yellow")
food.place(x=13,y=5,height=380,width=459)

#veg
veg_label=Label(frame5,text="Vegeterian meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
veg_label.place(x=25,y=40)

#Veg entry box
e12=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3,textvar=veg)
e12.place(x=250,y=40,height=40,width=200)
e12.insert(END,0)
#nonveg
nonveg_label=Label(frame5,text="Non-Vegeterian meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
nonveg_label.place(x=25,y=90)

#Non-Veg entry box
e13=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3,textvar=nonveg)
e13.place(x=250,y=90,height=40,width=200)
e13.insert(END,0)

#vegan 
vegan_label=Label(frame5,text="Vegan meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
vegan_label.place(x=25,y=140)

#Vegan entry box
e14=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3,textvar=vegan)
e14.place(x=250,y=140,height=40,width=200)
e14.insert(END,0)

#gluten-free 
glu=Label(frame5,text="Gluten-free meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
glu.place(x=25,y=190)

#gluten entry box
e15=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3,textvar=gluten)
e15.place(x=250,y=190,height=40,width=200)
e15.insert(END,0)

#diabetic-free 
dia=Label(frame5,text="Diabetic meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
dia.place(x=25,y=240)

#Diabetic entry box
e16=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3,textvar=diabetic)
e16.place(x=250,y=240,height=40,width=200)
e16.insert(END,0)

#baby meal 
baby_label=Label(frame5,text="Baby meal-",font=("times new roman",16,"bold"),bg="black",fg="powder blue")
baby_label.place(x=25,y=290)

#baby entry box
e17=Entry(frame5,font=("times new roman",22,"bold"),bg="light grey",fg="black",bd=3,textvar=baby)
e17.place(x=250,y=290,height=40,width=200)
e17.insert(END,0)


def Verify():
    global dis
    a=combo_s.get()
    b=combo_d.get()
    p=person.get()
    d=a+"-"+b
    e=b+"-"+a
    if name.get()!="" or contact.get()!="" or date.get()!="" :
        if contact.get()=="":
            messagebox.showerror("Error","Please enter the contact number")
            return
        elif date.get()=="":
            messagebox.showerror("Error","Please enter the date")
            return
            
    else:
         messagebox.showwarning("Warning","Passenger details are must")
         return

    if a!=b:
     if d in dict:
        dis=dict[d]
     elif e in dict:
        dis=dict[e]
    else:
     messagebox.showwarning("Warning","Kindly select the right travel root")
     return
    messagebox.showinfo("Checked","Succesfully verified")
    
def gticket():
    try:
        welcome()
        p=person.get()
        textarea.insert(END,f"\n {55*'*'}")
        textarea.insert(END, f"\n\n From :\t\t      {combo_s.get()}")
        textarea.insert(END, f"\n To :\t\t      {combo_d.get()}")
        textarea.insert(END, f"\n Date :\t\t      {date.get()}")
        textarea.insert(END, f"\n No. of person:               {p} ")
        textarea.insert(END, f"\n Total distance :          {dis}"+"km")
        textarea.insert(END, f"\n {35*'='}")
        textarea.insert(END, f"\n Ticket Price :               {5*p*dis}"+"Rs.")
        textarea.insert(END,f"\n Refreshment Price:      {500*p}"+"Rs.")
        textarea.insert(END, f"\n {35*'='}")
        textarea.insert(END,f"\n Total Amount:              {(5*p*dis)+(500*p)}"+"Rs.")
        textarea.insert(END, f"\n\n {55*'*'}")
        save_ticket()
    except Exception:
        messagebox.showwarning('Warrning','Pleaes varify the details first')
        clear()

def clear():
    name.set('')
    contact.set('')
    combo_s.set('select Source')
    combo_d.set('select destination')
    person.set(0)
    veg.set(0)
    nonveg.set(0)
    gluten.set(0)
    diabetic.set(0)
    vegan.set(0)
    baby.set(0)
    
    welcome()

def exit():
    op = messagebox.askyesno("Exit", "Do you really want to exit?")
    if op > 0:
        w.destroy()

def save_ticket():
    op=messagebox.askyesno("Save ticket","Do you want to download ticket ?")
    if op>0:
        ticket_details=textarea.get('1.0',END)
        f1=open("ticket.txt","w")
        f1.write(ticket_details)
        f1.close()
        messagebox.showinfo("Saved",f"Ticket no, :{ticket_no.get()} Saved Successfully")
    else:
        return

def welcome():
    x = random.randint(1000, 9999)
    ticket_no.set(str(x))
    textarea.delete(1.0,END)
    textarea.insert(END,"         ...........Have A Safe journey...........")
    textarea.insert(END, f"\n {63*'-'}")
    textarea.insert(END,f"\n\nTicket Number:\t\t{ticket_no.get()}")
    textarea.insert(END,f"\nPassenger Name:\t\t{name.get()}")
    textarea.insert(END,f"\nPhone Number:\t\t{contact.get()}")
    textarea.configure(font='arial 15 bold')

#data insertion
def submit():
  a=name.get()
  b=contact.get()
  c=date.get()
  d=combo_s.get()
  e=combo_d.get()
  f=person.get()
  g=veg.get()
  h=nonveg.get()
  i=vegan.get()
  j=gluten.get()
  k=diabetic.get()
  l=baby.get()
  cr.execute("insert into prernaairlines(Name,Contact,Date,Source,Destination,No_of_Tickets,Vegetarian,Non_Vegetarian,Vegan,Gluten,Diabetic,Baby)values(?,?,?,?,?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h,i,j,k,l))
  db.commit()
  print("Data is inserted Successfully")
  
  #Verify button
Verify=Button(frame4,text="Check",font=("britannic bold",16,"bold"),bg="blue",fg="white",command=Verify)
Verify.place(x=15,y=33,height=90,width=180)

#submit button
sbutton=Button(frame4,text="Submit",font=("britannic bold",16,"bold"),bg="violet",fg="white",command=submit)
sbutton.place(x=315,y=33,height=90,width=180)
        
#Generate BUTTON
Generate_Ticket=Button(frame4,text="Generate Ticket",font=("britannic bold",16,"bold"),bg="green",fg="white",command=gticket)
Generate_Ticket.place(x=650,y=33,height=90,width=180)


#clear BUTTON
clear_button=Button(frame4,text="Reset",font=("britannic bold",16,"bold"),bg="purple",fg="white",command=clear)
clear_button.place(x=945,y=33,height=90,width=180)


#exit BUTTON
exit_button=Button(frame4,text="Exit",font=("britannic bold",16,"bold"),bg="red",fg="white",command=exit)
exit_button.place(x=1300,y=33,height=90,width=180)
w.mainloop()
