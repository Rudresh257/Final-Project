from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Mobile_no",width=20,font=("bold", 10))
label_3.place(x=70,y=230)


label_4 = Label(root, text="Address",width=20,font=("bold", 10))
label_4.place(x=400,y=500)

label_5 = Label(root, text="Password",width=20,font=("bold", 10))
label_5.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=280)

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
root.mainloop()
print("registration form  seccussfully created...")
