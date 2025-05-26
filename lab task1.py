import tkinter as tk
def add():
    stri = f"{entry.get()} : {str.get()}"
    listbox.insert(tk.END, stri)
    str.set(value="select one")

root = tk.Tk()
root.geometry("300x300")
root.title("Counter")


label = tk.Label(root, text="EVENT: ")
label.grid(row=0,column=0,pady=5)

entry = tk.Entry(root)
entry.grid(row= 0, column=1, pady=10)

label1 = tk.Label(root, text="Priority: ")
label1.grid(row=1,column=0,pady=5)

list = ["Low", "Medium", "High"]
str = tk.StringVar(value="Select one")

drop = tk.OptionMenu(root,str,*list)
drop.grid(row=1, column=1)

button1 = tk.Button(root, text="Add event", command=add, foreground="blue")
button1.grid(row=2, columnspan=2, padx=20,pady=10)

listbox = tk.Listbox(root,width=50)
listbox.grid(row=3, columnspan=3)

root.mainloop()