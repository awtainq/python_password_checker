import uuid
from tkinter import *
from tkinter import messagebox
import hashlib
salt = uuid.uuid4().hex

# def hash_password(password):
#     global salt
#     return hashlib.sha256(salt.encode() + password.encode()).hexdigest()

def hash_password(password):
    global salt
    s=1
    l=0
    for i in password.encode()+salt.encode():
        l+=(i*131071**s)
        s+=1
    return format(l%2**128,'x')

def check_password(hashed_password, user_password):
    global salt
    return hashed_password == hash_password(user_password)

psswrd = hash_password("password")
root = Tk()

def check(event):
    global psswrd
    if check_password(psswrd, entry.get()):
        messagebox.showinfo("Correct", "Correct password")
    else:
        messagebox.showerror("Incorrect", "Incorrect password")

root.title('Passwords')
label = Label(root, text='Enter password:', anchor='center')
label.pack()
entry = Entry(root, show='*')
entry.pack()
root.bind('<Return>', check)

root.mainloop()