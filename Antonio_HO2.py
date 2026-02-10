import tkinter as tk

window = tk.Tk()

window.title("profile")
window.geometry("600x600")
window.resizable(False,True)
window.configure(bg="pink", cursor="hand2")

label = tk.Label(window, text="Student Profile",
    font = ("times new roman", 43),
    fg = "red",
    bg = "pink",
    anchor = "center")

label_1 = tk.Label(window, text="Name: Dynneal E. Antonio",
    font = ("times new roman", 17),
    fg = "red",
    bg = "pink")

label_2 = tk.Label(window, text="Age: 19",
    font = ("times new roman", 17),
    fg = "red",
    bg = "pink")

label_3 = tk.Label(window, text="Course and Section: BSIT 1A",
    font = ("times new roman", 17),
    fg = "red",
    bg = "pink")

label_4 = tk.Label(window, text="Birthday: November 07, 2006",
    font = ("times new roman", 17),
    fg = "red",
    bg = "pink")

label_5 = tk.Label(window, text="Motto: Treat yourself as kindly as you treat others.",
    font = ("times new roman", 17),
    fg = "red",
    bg = "pink")

label.pack(pady=50)
label_1.pack(padx=30, pady=10, anchor="w")
label_2.pack(padx=30, pady=10, anchor="w")
label_3.pack(padx=30, pady=10, anchor="w")
label_4.pack(padx=30, pady=10, anchor="w")
label_5.pack(padx=30, pady=10, anchor="w")

window.mainloop()