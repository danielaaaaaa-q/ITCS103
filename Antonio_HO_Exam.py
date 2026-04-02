import tkinter as tk

window = tk.Tk()
window.title("Antonio_HO_Exam")
window.geometry("500x200")
window.config(bg="white", cursor="heart")

def regs():
    popup = tk.Toplevel()
    popup.title("Registration Form")
    popup.geometry("480x300")
    popup.config(bg="light blue", cursor="heart")

    def regs_click():
        username = us.get()
        password = pw.get()

        for i in len(password):
            if password < 9:
                if username == "" and password == "":
                    label1 ['text'] = "You have succesfully registered!"
            else:
                label1 ['text'] = "You didn't meet the required length of password. (8)"

    label1 = tk.Label(popup, text="", bg="light blue", font=(30))
    label1.place(x=90, y=10)

    user = tk.Label(popup, text="Username:", font=(10), bg="light blue")
    user.place(x=20, y=70)

    passw = tk.Label(popup, text="Password:", font=(10), bg="light blue")
    passw.place(x=20, y=120)

    us = tk.Entry(popup, width=20, font=(10))
    us.place(x=195, y=70)
    us.get()

    pw = tk.Entry(popup, width=20, font=(10), show="*")
    pw.place(x=195, y=120)
    pw.get()

    c_btn = tk.Checkbutton(popup, text="See Password", font=(10))
    c_btn.place(x=240, y=170)

    btn = tk.Button(popup, text="Register", bg="White", font=(10), width=20, command=regs_click)
    btn.place(x=110, y=220)

def log():
    popup = tk.Toplevel()
    popup.title("Log In!")
    popup.geometry("480x300")
    popup.config(bg="pink", cursor="heart")

    def log_click():
        username = us.get()
        password = pw.get()

        if username and password:
            label1 ['text'] = "You have succesfully registered!"

    label1 = tk.Label(popup, text="", font=(40), bg="pink")
    label1.place(x=190, y=40)

    label2 = tk.Label(popup, text="Log In", font=(40), bg="pink")
    label2.place(x=190, y=40)

    user = tk.Label(popup, text="Username:", font=(10), bg="pink")
    user.place(x=20, y=100)

    passw = tk.Label(popup, text="Password:", font=(10), bg="pink")
    passw.place(x=20, y=150)

    us = tk.Entry(popup, width=20, font=(10))
    us.place(x=195, y=100)

    pw = tk.Entry(popup, width=20, font=(10), show="*")
    pw.place(x=195, y=150)

    c_btn = tk.Checkbutton(popup, text="See Password", font=(10))
    c_btn.place(x=240, y=200)

    btn = tk.Button(popup, text="Log In", bg="White", font=(10), width=20)
    btn.place(x=110, y=250)


label = tk.Label(window, text="Welcome!", font=(50), bg="white")
label.place(x=200, y=10)

r_btn = tk.Button(window, text="Register", bg="blue", font=(30), width=30, command=regs)
r_btn.place(x=65, y=50)

lo_btn = tk.Button(window, text="Log In", bg="green", font=(30), width=30, command=log)
lo_btn.place(x=65, y=100)


window.mainloop()
