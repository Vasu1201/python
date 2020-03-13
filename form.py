#Form

from tkinter  import *
root=Tk()

#Submit button command

def callback():
  print("form submitted")

#Making frame
  
L1=Label(root,text="Enter your good name :")
ent_1=Entry(root)
L1.grid(row=0,column=0)
ent_1.grid(row=0,column=1)

L2=Label(root,text="Enter your email :")
ent_2=Entry(root)
L2.grid(row=1,column=0)
ent_2.grid(row=1,column=1)

L3=Label(root,text="Enter your contact number ")
ent_3=Entry(root)
L3.grid(row=2,column=0)
ent_3.grid(row=2,column=1)

frame=Frame(root)
L4=Label(root,text="your hobbies")

#Making check button

C1=Check_button(frame,text="Outdoor games")
C2=Check_button(frame,text="Indoor Games")
C3=Check_button(frame,text="Reading")
L4.grid(row=3,column=0)
frame.grid(row=3,column=1)
b=Button(root,text="SUBMIT",command= callback)
b.grid(row=4,column=1)

#This is to call function

C1.pack(side=LEFT)
C2.pack(side=LEFT)
C3.pack(side=LEFT)
