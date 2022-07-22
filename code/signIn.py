from msilib.schema import File
import sqlite3
from tkinter import *
from tkinter import font
from tkinter import messagebox

root = Tk()

# configuring some ui for the main window 

root.geometry("1200x700+100+50")
root.title("Todo Application")


# background image for the main window
bg = PhotoImage(file = "C:\\Users\\ACER\\Desktop\\TodoApplication\\images\\groundOne.png")

# spanning the background image all across the window
backgroundImg = Label(root,image=bg)
backgroundImg.place(x=0,y=0)

# creating a center frame for the login 
centerFrame = LabelFrame(root,width=300,height=500,bg='#f1f3f5').place(x=800,y=100)

# creating various labels and entry boxes for the login form
welcome = Label(centerFrame,text="Welcome!",bg='#f1f3f5')
welcome.config(font=("Helvetica",20))
welcome.place(x=885,y=110)

email = Label(centerFrame,text="Email",bg="#f1f3f5")
email.place(x=850,y=175)

emailBox = Entry(centerFrame,width=32)
emailBox.place(x=850,y=205)

password = Label(centerFrame,text="Password",bg="#f1f3f5")
password.place(x=850,y=240)

passwordBox = Entry(centerFrame,width=32,show='*')
passwordBox.place(x=850,y=270)

loginBtn = Button(centerFrame,text="Login",bg="#0c8599",fg="white",padx=50)
loginBtn.place(y=340,x=880)

# function to show the hidden password
def showPassword():
   isChecked = checkVal.get()
   if (isChecked==1):
      passwordBox.config(show='')
   else:
      passwordBox.config(show='*')   

      
# show password checkbox
checkVal = IntVar()
showPassCheckbox = Checkbutton(centerFrame,text="",bg='#f1f3f5',variable=checkVal,onvalue=1,offvalue=0,command=showPassword)
showPassCheckbox.place(y=300,x=895)

showPassLabel = Label(centerFrame,text="Show Password",bg="#f1f3f5")
showPassLabel.place(y=301,x=910)




# establishing a connection with the database

# code to show up a new window and various widgets for the signup form
def signUp():
   conn = sqlite3.connect("users.db")


   
   top = Toplevel()
   top.title("Sign Up Form")
   top.geometry("600x700")
   top.config(bg="#fff")
   signUpFrame = LabelFrame(top,width=300,height=500,bg="#f1f3f5")
   signUpFrame.place(x=150,y=100)



   # inserting various widgets into the sign up form
   fName = Label(signUpFrame,text="First Name",bg="#f1f3f5")
   fName.place(x=30,y=25)

   fNameBox = Entry(signUpFrame,width=30)
   fNameBox.place(x=30,y=50)

   lName = Label(signUpFrame,text="Last Name",bg="#f1f3f5")
   lName.place(x=30,y=75)

   lNameBox = Entry(signUpFrame,width=30)
   lNameBox.place(x=30,y=100)

   newEmail = Label(signUpFrame,text="Email",bg="#f1f3f5")
   newEmail.place(x=30,y=125)

   newEmailBox = Entry(signUpFrame,width=30)
   newEmailBox.place(x=30,y=150)

   newPassword = Label(signUpFrame,text="New Password",bg="#f1f3f5")
   newPassword.place(x=30,y=175)

   newPasswordBox = Entry(signUpFrame,width=30)
   newPasswordBox.place(x=30,y=200)

   confirmNewPassword = Label(signUpFrame,text="Confirm new password",bg="#f1f3f5")
   confirmNewPassword.place(x=30,y=225)

   confirmNewPasswordBox = Entry(signUpFrame,width=30)
   confirmNewPasswordBox.place(x=30,y=250)


   c = conn.cursor()

   def registerUser():
      c.execute("INSERT INTO users VALUES(:f_name,:l_name,:email,:password)",{
         'f_name':fNameBox.get(),
         'l_name':lNameBox.get(),
         'email':newEmailBox.get(),
         'password':confirmNewPasswordBox.get()
      })

      fNameBox.delete(0,END)
      lNameBox.delete(0,END)
      newEmailBox.delete(0,END)
      confirmNewPasswordBox.delete(0,END)
      

      messagebox.showinfo("Signed up successfully")
      messagebox.Message("Hello world")


   signBtn = Button(signUpFrame,text="SignUp",bg="#12b886",fg="white",padx=50,command=registerUser)
   signBtn.place(x=51,y=300)
   conn.commit()
   # conn.close()

   
   # # backgoround for signup page
   # signUp_bg=PhotoImage("C:\\Users\\ACER\\Desktop\\TodoApplication\\images\\bluebackground.png")
   # signUp_bg = Label(top,image=bg)
   # signUp_bg.place(x=0,y=0)



noAccountOne = Label(centerFrame,text="Don't have an account?")
noAccountOne.place(x=880,y=400)

# creating a sign up button
signUpBtn = Button(centerFrame,command=signUp,text="SignUp",fg="blue",bg="#f1f3f5",borderwidth=0)
signUpBtn.place(x=920,y=430)

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("SELECT *, oid FROM users")

records = c.fetchall()
print(records)

conn.commit()
conn.close()


root.mainloop()