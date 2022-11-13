from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

Label(root, text = " Registration Form", font = "ar 15 bold").grid(row=0, column=3)

name= Label(root, text = "Name")
phone= Label(root, text = "Phone")
gender= Label(root, text = "Gender")
email= Label(root, text = "Email")
paymentmethod= Label(root, text = "Payment method")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
email.grid(row=4, column=2)
paymentmethod.grid(row=5, column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emailvalue = StringVar
paymentmethodvalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emailentry = Entry(root, textvariable=emailvalue)
paymentmethodentry = Entry(root, textvariable=paymentmethodvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
paymentmethodentry.grid(row=5, column=3)

checkbtn = Checkbutton(text="Remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

Button(text="Submit", command=getvals).grid(row=7, column= 3)
root.mainloop()
