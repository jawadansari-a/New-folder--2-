import tkinter as tk
from tkinter import messagebox

class SimpleFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Info Form")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f5")
        
        # Title label
        title_lbl = tk.Label(root, text="Enter your information", font=("Arial", 16, "bold"), bg="#f0f0f5")
        title_lbl.pack(pady=10)
        
        # Frame for form inputs
        form_frame = tk.Frame(root, bg="#f0f0f5")
        form_frame.pack(pady=10)
        
        # Name
        name_lbl = tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f0f0f5")
        name_lbl.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Email
        email_lbl = tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#f0f0f5")
        email_lbl.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.email_entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Gender radio buttons
        gender_lbl = tk.Label(form_frame, text="Gender:", font=("Arial", 12), bg="#f0f0f5")
        gender_lbl.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        self.gender_var = tk.StringVar(value="Male")
        genders = ["Male", "Female", "Other"]
        col = 1
        for gender in genders:
            rb = tk.Radiobutton(form_frame, text=gender, variable=self.gender_var, value=gender, bg="#f0f0f5", font=("Arial", 12))
            rb.grid(row=2, column=col, padx=5, pady=5, sticky="w")
            col += 1
        
        # Newsletter subscription checkbox
        self.newsletter_var = tk.BooleanVar()
        newsletter_chk = tk.Checkbutton(root, text="Subscribe to newsletter", variable=self.newsletter_var, bg="#f0f0f5", font=("Arial", 12))
        newsletter_chk.pack(pady=10)
        
        # Submit button
        submit_btn = tk.Button(root, text="Submit", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5, command=self.submit_info)
        submit_btn.pack(pady=10)
        
        # Label to display submitted info
        self.info_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f5", fg="#333333", wraplength=350, justify="left")
        self.info_label.pack(pady=10)
    
    def submit_info(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        gender = self.gender_var.get()
        newsletter = "Yes" if self.newsletter_var.get() else "No"
        
        if not name or not email:
            messagebox.showwarning("Input Error", "Please enter both Name and Email.")
            return
        
        info_text = f"Name: {name}\nEmail: {email}\nGender: {gender}\nNewsletter Subscription: {newsletter}"
        self.info_label.config(text=info_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleFormApp(root)
    root.mainloop()

