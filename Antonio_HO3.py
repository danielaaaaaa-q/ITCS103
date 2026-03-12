import tkinter as tk

window = tk.Tk()

window.title("Simple Calculator")
window.configure(bg="light blue", cursor="heart")

frame = tk.Frame(window, bg="white")
frame.grid(row=0, column=0, columnspan=3)

label = tk.Label(frame, text="Welcome, User!", bg="white")
label.grid(padx=80, pady=10)

a = tk.Label(window, text="Enter 1st Number:", bg="white")
a.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

a_entry = tk.Entry(window)
a_entry.grid(row=1, column=2)
value_at = a_entry.get()

b = tk.Label(window, text="Enter 2nd Number:", bg="white")
b.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

b_entry = tk.Entry(window)
b_entry.grid(row=2, column=2)
value_at = b_entry.get()

def add():
    first = int(a_entry.get())
    second = int(b_entry.get())

    sum = int((first + second))
    label ['text'] = f"The sum of {first} + {second} is {sum}"

ad = tk.Button(window, text="ADD", command=add)
ad.grid(row=3, column=0, columnspan=2, pady=5)

def sub():
    first = int(a_entry.get())
    second = int(b_entry.get())

    dif = int((first - second))
    label ['text'] = f"The difference of {first} - {second} is {dif}"

su = tk.Button(window, text="SUBTRACTION", command=sub)
su.grid(row=3, column=2, columnspan=2, pady=5)

def multiply():
    first = int(a_entry.get())
    second = int(b_entry.get())

    prod = int((first * second))
    label ['text'] = f"The product of {first} x {second} is {prod}"

pr = tk.Button(window, text="MuULTIPLY", command=multiply)
pr.grid(row=4, column=0, columnspan=2, pady=5)

def div():
    first = int(a_entry.get())
    second = int(b_entry.get())

    qou = int((first / second))
    label ['text'] = f"The qoutient of {first} / {second} is {qou}"

q = tk.Button(window, text="DIVISION", command=div)
q.grid(row=4, column=2, columnspan=2, pady=5)


window.mainloop()
