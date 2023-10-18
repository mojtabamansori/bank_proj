from tkinter import Tk, Label, Entry, Button, messagebox, Toplevel, Radiobutton, StringVar, simpledialog
from backend import BankSystem, Cashier

class BankApp:
    def __init__(self, bank_name):
        self.bank_system = BankSystem(bank_name)
        self.login_window = None
        self.registration_window = None
        self.cashier_window = None
        self.create_login_window()
        self.role_var = StringVar()

    def create_login_window(self):
        self.login_window = Tk()
        self.login_window.title("Login")

        self.create_login_labels()
        self.create_login_entries()
        self.create_login_button()
        self.create_register_button()
        self.create_exit_button(self.login_window)  # Add exit button

    def create_login_labels(self):
        Label(self.login_window, text="Username: ").grid(row=0, column=0)
        Label(self.login_window, text="Password: ").grid(row=1, column=0)

    def create_login_entries(self):
        self.login_username_entry = Entry(self.login_window)
        self.login_username_entry.grid(row=0, column=1)

        self.login_password_entry = Entry(self.login_window, show="*")
        self.login_password_entry.grid(row=1, column=1)

    def create_login_button(self):
        button = Button(self.login_window, text="Login", command=self.login)
        button.grid(row=2, column=0, columnspan=2)

    def create_register_button(self):
        button = Button(self.login_window, text="Register", command=self.open_registration_window)
        button.grid(row=3, column=0, columnspan=2)

    def open_registration_window(self):
        self.login_window.withdraw()  # Hide login window
        self.create_registration_window()

    def create_registration_window(self):
        self.registration_window = Toplevel(self.login_window)
        self.registration_window.title("Registration")

        self.create_registration_labels()
        self.create_registration_entries()
        self.create_role_selection()
        self.create_registration_button()
        self.create_exit_button(self.registration_window)  # Add exit button

    def create_registration_labels(self):
        Label(self.registration_window, text="Username: ").grid(row=0, column=0)
        Label(self.registration_window, text="Password: ").grid(row=1, column=0)
        Label(self.registration_window, text="First Name: ").grid(row=2, column=0)
        Label(self.registration_window, text="Last Name: ").grid(row=3, column=0)

    def create_registration_entries(self):
        self.registration_username_entry = Entry(self.registration_window)
        self.registration_username_entry.grid(row=0, column=1)

        self.registration_password_entry = Entry(self.registration_window, show="*")
        self.registration_password_entry.grid(row=1, column=1)

        self.registration_first_name_entry = Entry(self.registration_window)
        self.registration_first_name_entry.grid(row=2, column=1)

        self.registration_last_name_entry = Entry(self.registration_window)
        self.registration_last_name_entry.grid(row=3, column=1)

    def create_role_selection(self):
        Label(self.registration_window, text="Role: ").grid(row=4, column=0)
        Radiobutton(self.registration_window, text="Cashier", variable=self.role_var, value="cashier").grid(row=5, column=1, sticky="w")

    def create_registration_button(self):
        button = Button(self.registration_window, text="Register", command=self.register)
        button.grid(row=6, column=0, columnspan=2)

    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        if not username or not password:
            messagebox.showwarning("Login Failed", "Please enter username and password.")
            return

        user = self.bank_system.get_user(username, password)

        if user is None:
            messagebox.showerror("Login Failed", "Invalid username or password.")
        else:
            messagebox.showinfo("Login Successful", "Welcome, " + user.first_name + " " + user.last_name)
            self.login_window.withdraw()  # Hide login window


            self.open_cashier_window(user)

    def register(self):
        username = self.registration_username_entry.get()
        password = self.registration_password_entry.get()
        first_name = self.registration_first_name_entry.get()
        last_name = self.registration_last_name_entry.get()
        role = self.role_var.get()

        if not username or not password or not first_name or not last_name:
            messagebox.showwarning("Registration Failed", "Please fill in all fields.")
            return

        result = self.bank_system.register_user(username, password, first_name, last_name, role)

        if result:
            messagebox.showinfo("Registration Successful", "User registration successful.")
            self.create_login_window()
            self.registration_window.destroy()  # Close registration window
        else:
            messagebox.showerror("Registration Failed", "Username already exists.")


    def view_profile(self):
        # Example functionality: Display a message box with the customer's profile information
        messagebox.showinfo("Profile", "Name: John Doe\nAccount Number: 123456\nAccount Value: $1000")

    def open_cashier_window(self, user):
        self.cashier_window = Toplevel(self.login_window)
        self.cashier_window.title("Cashier Window")
        self.cashier_window.geometry("300x300")

        Label(self.cashier_window, text="Welcome, " + user.first_name + " " + user.last_name).grid(row=0, column=0)

        # Add cashier-specific widgets and functionality here
        self.create_change_value_button()
        self.create_exit_button(self.cashier_window)  # Add exit button

    def create_change_value_button(self):
        button = Button(self.cashier_window, text="اصول مخابرات", command=self.change_value)
        button.grid(row=1, column=0, columnspan=2)
        button = Button(self.cashier_window, text="تحلیل 1", command=self.change_value)
        button.grid(row=2, column=0, columnspan=2)
        button = Button(self.cashier_window, text="تحلیل 2", command=self.change_value)
        button.grid(row=3, column=0, columnspan=2)
        button = Button(self.cashier_window, text="رله و حفاظت", command=self.change_value)
        button.grid(row=4, column=0, columnspan=2)

    def change_value(self):
        messagebox.askokcancel("انتخاب واحد", "از انتخاب این واحد مطمئن هستید؟")


    def create_exit_button(self, window):
        button = Button(window, text="Exit", command=self.exit_app)
        button.grid(row=99, column=0, columnspan=2)

    def exit_app(self):
        if messagebox.askokcancel("خروج", "از اینکه می خواهید از انتخاب واحد خارج شوید مطمئن هستید؟"):
            self.login_window.destroy()

    def run(self):
        self.login_window.deiconify()  # Show the login window
        self.login_window.mainloop()

