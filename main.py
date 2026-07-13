import tkinter as tk
from tkinter import ttk, messagebox

from password import generate_password


class PasswordGenerator:

    def __init__(self, root):

        self.root = root
        self.root.title("Password Generator Pro")
        self.root.geometry("520x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#EAF4FC")

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Password Generator Pro",
            font=("Segoe UI", 22, "bold"),
            bg="#EAF4FC",
            fg="#0F4C81"
        )
        title.pack(pady=15)

        frame = tk.Frame(
            self.root,
            bg="white",
            bd=2,
            relief="ridge"
        )
        frame.pack(padx=20, pady=10, fill="both", expand=True)

        tk.Label(
            frame,
            text="Password Length",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).pack(pady=(20,5))

        self.length = tk.IntVar(value=12)

        ttk.Scale(
            frame,
            from_=4,
            to=30,
            orient="horizontal",
            variable=self.length
        ).pack(fill="x", padx=40)

        self.length_label = tk.Label(
            frame,
            text="12 Characters",
            bg="white",
            font=("Segoe UI",10)
        )
        self.length_label.pack(pady=5)

        self.length.trace_add("write", self.update_length)

        self.upper = tk.BooleanVar(value=True)
        self.lower = tk.BooleanVar(value=True)
        self.digits = tk.BooleanVar(value=True)
        self.symbols = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            frame,
            text="Uppercase Letters",
            variable=self.upper
        ).pack(anchor="w", padx=40, pady=3)

        ttk.Checkbutton(
            frame,
            text="Lowercase Letters",
            variable=self.lower
        ).pack(anchor="w", padx=40, pady=3)

        ttk.Checkbutton(
            frame,
            text="Numbers",
            variable=self.digits
        ).pack(anchor="w", padx=40, pady=3)

        ttk.Checkbutton(
            frame,
            text="Symbols",
            variable=self.symbols
        ).pack(anchor="w", padx=40, pady=3)

        ttk.Button(
            frame,
            text="Generate Password",
            command=self.generate
        ).pack(pady=20)

        self.password_entry = ttk.Entry(
            frame,
            font=("Consolas",14),
            justify="center",
            width=30
        )
        self.password_entry.pack(pady=10)

        ttk.Button(
            frame,
            text="Copy Password",
            command=self.copy_password
        ).pack(pady=5)

        ttk.Button(
            frame,
            text="Reset",
            command=self.reset
        ).pack(pady=5)

        tk.Label(
            self.root,
            text="Developed using Python & Tkinter",
            bg="#EAF4FC",
            fg="gray"
        ).pack(pady=10)

    def update_length(self, *args):

        self.length_label.config(
            text=f"{self.length.get()} Characters"
        )

    def generate(self):

        try:

            password = generate_password(
                length=self.length.get(),
                use_upper=self.upper.get(),
                use_lower=self.lower.get(),
                use_digits=self.digits.get(),
                use_symbols=self.symbols.get()
            )

            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_password(self):

        password = self.password_entry.get()

        if password:

            self.root.clipboard_clear()
            self.root.clipboard_append(password)

            messagebox.showinfo(
                "Copied",
                "Password copied to clipboard!"
            )

    def reset(self):

        self.length.set(12)

        self.upper.set(True)
        self.lower.set(True)
        self.digits.set(True)
        self.symbols.set(True)

        self.password_entry.delete(0, tk.END)


if __name__ == "__main__":

    root = tk.Tk()

    PasswordGenerator(root)

    root.mainloop()