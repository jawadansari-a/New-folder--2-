import tkinter as tk
count  = 0
def sub():
    global count
    count -= 1
    label.config(text=f"{count}")

def add():
    global count
    count += 1
    label.config(text=f"{count}")

def reset():
    global count
    count = 0
    label.config(text=f"{0}")

root = tk.Tk()
root.geometry("100x110")
root.title("Counter")

label = tk.Label(root, text="0",foreground="blue")
label.grid(row=0,columnspan=2,pady=5)

button1 = tk.Button(root, text="+", command=add, foreground="blue")
button1.grid(row=1, column=0, padx=20,pady=10)

button2 = tk.Button(root, text="-", command=sub)
button2.grid(row=1, column=1,padx=20,pady=10)

button3 = tk.Button(root, text="RESET", command=reset)
button3.grid(row=2, columnspan=2)

root.mainloop()