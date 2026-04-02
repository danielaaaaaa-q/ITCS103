import tkinter as tk

window = tk.Tk()
window.title("Profile Builder")
window.geometry("800x400")
window.configure(bg="white", cursor="heart")

def show():
    popup = tk.Toplevel()
    popup.title("Profile")
    popup.geometry("200x200")
    popup.configure(bg="light blue", cursor="heart")

    frame = tk.Frame(popup)
    frame.pack()

    popup_label = tk.Label(frame, text="Student ID")
    popup_label.pack()

    popup_label1 = tk.Label(frame, text="Name:")
    popup_label1.pack()

    popup_label2 = tk.Label(frame, text="Gender:")
    popup_label2.pack()

    by_ent = by_entry.get()
    age = int(2026) - int(by_ent)

    com ['text'] = f'You are {age} years old.'

def change_color():
    gender = int(rad_val.get())
    if gender == 1:
        window ['bg'] = "pink"
        label ['bg'] = "pink"
    else:
        window ['bg'] = "light blue"
        label ['bg'] = "light blue"


label = tk.Label(window, text="Profile Builder", font=("times new roman", 20, "bold"), bg="white")
label.grid(row=0, pady=10, columnspan=2)

frame = tk.Frame(window, bg="pink1")
frame.grid(padx=50)

fname_entry = tk.Entry(frame, width=30)
fname_entry.grid(row=1, column=0, padx=5, pady=5)
value_at = fname_entry.get()

f = tk.Label(frame, text="First Name", bg="pink1")
f.grid(row=2, column=0)

mname_entry = tk.Entry(frame, width=30)
mname_entry.grid(row=1, column=1, padx=5, columnspan=2)

m = tk.Label(frame, text="Middle Name", bg="pink1")
m.grid(row=2, column=1, columnspan=2)

lname_entry = tk.Entry(frame, width=30)
lname_entry.grid(row=1, column=3, padx=5)

l = tk.Label(frame, text="Last Name", bg="pink1")
l.grid(row=2, column=3)

by_entry = tk.Entry(frame, width=30)
by_entry.grid(row=3, column=0, padx=5, pady=5)
value_at = by_entry.get()

by = tk.Label(frame, text="Birth Year", bg="pink1")
by.grid(row=4, column=0)

g = tk.Label(frame, text="Gender", bg="pink1")
g.grid(row=5, column=0)

rad_val = tk.IntVar()

male = tk.Radiobutton(frame, text="Male", value=0, bg="pink1", variable=rad_val, command=change_color)
male.grid(row=5, column=1)

female = tk.Radiobutton(frame, text="Female", value=1, bg="pink1", variable=rad_val, command=change_color)
female.grid(row=5, column=2)

com = tk.Label(frame, text="Computing Age...", font=("Arial", 20), bg="pink1")
com.grid(row=3, column=2, rowspan=2)

btn = tk.Button(window, text="Submit", bg="pink1", command=show)
btn.grid(pady=20)


window.mainloop()