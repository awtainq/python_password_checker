import uuid
from tkinter import *
from tkinter import messagebox
import hashlib

table = []
def hash_password(password,salt):
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()

# def hash_password(password, salt):
#     s=1
#     l=0
#     for i in password.encode()+salt.encode():
#         l+=(i*131071**s)
#         s+=1
#     return format(l%2**128,'x')

def check_password(hashed_password, user_password, salt):
    return hashed_password == hash_password(user_password,salt)
root = Tk()

def up():
    signup.pack_forget()
    signin.pack_forget()
    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    ok.pack()

def in_():
    up()
    ok.pack_forget()
    ok_in.pack()
    exit.pack()


def safe():
    salt = uuid.uuid4().hex
    table.append((entry1.get(), hash_password(entry2.get(),salt),salt))
    label1.pack_forget()
    entry1.pack_forget()
    label2.pack_forget()
    entry2.pack_forget()
    ok.pack_forget()
    signup.pack()
    signin.pack()
    entry1.delete(0, END)
    entry2.delete(0, END)
    messagebox.showinfo("Saved", "Credentials saved successfully")

def cls():
    label1.pack_forget()
    label2.pack_forget()
    entry1.pack_forget()
    entry2.pack_forget()
    ok_in.pack_forget()
    signup.pack()
    signin.pack()
    entry1.delete(0, END)
    entry2.delete(0, END)
    exit.pack_forget()

def check():
    username = entry1.get()
    password = entry2.get()
    for user, hashed_password, salt in table:
        if user == username:
            if check_password(hashed_password, password, salt):
                messagebox.showinfo("Success", "Login successful")
                cls()
                return
            else:
                messagebox.showerror("Error", "Incorrect password")
                return
    messagebox.showerror("Error", "User not found")

root.title('Passwords')
root.geometry('250x150')
label1 = Label(root, text='login:', anchor='center')
label2 = Label(root, text='password:', anchor='center')
entry1 = Entry(root)
entry2 = Entry(root, show='*')
signup = Button(root, text='Sign up', command=up)
signin = Button(root, text='Sign in',command=in_)
ok = Button(root, text='Ok', command=safe)
ok_in = Button(root, text='Ok',command=check)
exit = Button(root, text='Exit', command=cls)

signup.pack()
signin.pack()

root.mainloop()