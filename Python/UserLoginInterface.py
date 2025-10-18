from tkinter import *
import mysql.connector as S
conn=S.connect(host="localhost",user="root",passwd="chikuSQL@123",database="chiku") #Information to be entered by user.
cursor=conn.cursor()
root=Tk()
root.geometry("500x300")
root.title("VVV Project")

#Storing Data from File onto Database
def storevals(a,b,c,d):
    sql1='''CREATE TABLE Std_Info(
          Name varchar(20),
          Class varchar(6),
          Section varchar(2),
          Roll_Number varchar(2) primary key,
          Gender varchar(6)
          )'''
    cursor.execute(sql1)
    sql="INSERT INTO Std_Info(Name,Class,Section,Roll_Number,Gender) VALUES(%s,%s,%s,%s,%s)"
    vals=(a,b,c,d,"U")
    cursor.execute(sql,vals)
    conn.commit()
    print("data saved")
    conn.close()
    
#Trigger Function Storing Values in a Binary File
def getvals():
    print("Accepted")
    d={}
    a=nameentry.get()
    b=stdentry.get()
    c=sectionentry.get()
    d=rollentry.get()
    storevals(a,b,c,d)
    print("Data Stored")
    print(a)
    
#Heading
Label(root, text="Sign Up Portal", font="calibri 20 bold").grid(row=0,column=3)

#Field Name
name=Label(root, text="Name of the student")
std=Label(root, text="Class")
section=Label(root, text="Section")
roll=Label(root, text="Roll Number")
sex=Label(root, text="Sex")

#Packing Fields
name.grid(row=1, column=2)
std.grid(row=2, column=2)
section.grid(row=3, column=2)
roll.grid(row=4, column=2)
sex.grid(row=5,column=2)

#Variable for storing Data
namevalue=StringVar
stdvalue=StringVar
sectionvalue=StringVar
rollvalue=StringVar
malevalue=IntVar
femalevalue=IntVar


#Creating Entry Field
nameentry= Entry(root, textvariable=namevalue)
stdentry= Entry(root, textvariable=stdvalue)
sectionentry= Entry(root, textvariable=sectionvalue)
rollentry= Entry(root, textvariable=rollvalue)

#Packing Entry Field
nameentry.grid(row=1, column=3)
stdentry.grid(row=2, column=3)
sectionentry.grid(row=3, column=3)
rollentry.grid(row=4, column=3)


#Creating checkbox
checkbtn=Checkbutton(text="Male", variable = malevalue)
checkbtn.grid(row=5, column=3)
checkbtn2=Checkbutton(text="Female", variable = femalevalue)
checkbtn2.grid(row=5, column=4)

#Submit button
Button(text="Submit",command=getvals).grid(row=6,column=3)

root.mainloop()
