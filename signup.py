from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
   emailEntry.delete(0,END)
   usernameEntry.delete(0,END)
   passwordEntry.delete(0,END)
   confirmpasswordEntry.delete(0,END)
   check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpasswordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms & Conditions')
    else:
        try:
          con=pymysql.connect(host='localhost',user='root',password='12345')
          mycursor=con.cursor()
        except:
         messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
         return 
       
    try:
        query='create database userdata'
        mycursor.execute(query)
        query='use userdata'
        mycursor.execute(query)
        query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
        mycursor.execute(query)
    except:
       mycursor.execute('use userdata')
    query='select * from data where username=%s'
    mycursor.execute(query,(usernameEntry.get()))

    row=mycursor.fetchone()
    if row !=None:
       messagebox.showerror('Error','Username Already Exists')

    else:   
        query='insert into data(email,username,password) values(%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Registration is successful')
        clear()
        root.destroy()
        import login


def login_page():
    root.destroy()
    import login


root=Tk()
root.title('Signup Page')
root.resizable(False,False)

background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(root,image=background)
bgLabel.grid()

frame=Frame(root,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold')
              ,bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white'
                 ,fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25,)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white'
                 ,fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordeLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white'
                 ,fg='firebrick1')
passwordeLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmpasswordeLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white'
                 ,fg='firebrick1')
confirmpasswordeLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmpasswordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),
                 fg='white',bg='firebrick1')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termsandcondition=Checkbutton(frame,text='I Agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',9,'bold'),
                              fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',
                              cursor='hand2',variable=check)
termsandcondition.grid(row=9,column=0,pady=10,padx=15)

signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white'
                    ,activebackground='firebrick1',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame,text='Already have an account?',font=('Open Sans','9','bold'),
                     bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton=Button(frame,text='Log in',font=('Open Sans',9,'bold underline')
                   ,bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white'
                   ,activeforeground='blue',command=login_page)
loginButton.place(x=177,y=404)

root=mainloop()