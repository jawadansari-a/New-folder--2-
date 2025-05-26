import tkinter as tk

class AddSubtractApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Add and Subtract")
        self.root.geometry("300x200")
        self.root.configure(bg="#e6f2ff")

        self.value = 0

        # Label to show the current value
        self.value_label = tk.Label(root, text=str(self.value), font=("Arial", 36, "bold"), bg="#e6f2ff", fg="#003366")
        self.value_label.pack(pady=20)

        button_frame = tk.Frame(root, bg="#e6f2ff")
        button_frame.pack()

        # Add button
        add_btn = tk.Button(button_frame, text="Add", font=("Arial", 14), bg="#4CAF50", fg="white", width=8, command=self.add)
        add_btn.grid(row=0, column=0, padx=10)

        # Subtract button
        subtract_btn = tk.Button(button_frame, text="Subtract", font=("Arial", 14), bg="#f44336", fg="white", width=8, command=self.subtract)
        subtract_btn.grid(row=0, column=1, padx=10)

    def add(self):
        self.value += 1
        self.value_label.config(text=str(self.value))

    def subtract(self):
        self.value -= 1
        self.value_label.config(text=str(self.value))


if __name__ == "__main__":
    root = tk.Tk()
    app = AddSubtractApp(root)
    root.mainloop()

