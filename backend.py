import sqlite3

class BankSystem:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                first_name TEXT,
                last_name TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cashiers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT,
                first_name TEXT,
                last_name TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                cashier_id INTEGER,
                amount REAL,
                FOREIGN KEY (customer_id) REFERENCES customers (id),
                FOREIGN KEY (cashier_id) REFERENCES cashiers (id)
            )
        """)
        self.conn.commit()

    def register_user(self, username, password, first_name, last_name, role):
        if role == "customer":
            table_name = "customers"
            user_class = Customer
        elif role == "cashier":
            table_name = "cashiers"
            user_class = Cashier
        else:
            return None

        try:
            self.cursor.execute(f"""
                INSERT INTO {table_name} (username, password, first_name, last_name)
                VALUES (?, ?, ?, ?)
            """, (username, password, first_name, last_name))
            self.conn.commit()
            return user_class(username, password, first_name,last_name)  # Create the user instance without the 'role' parameter
        except sqlite3.IntegrityError:
            return None

    def get_user(self, username, password):
        self.cursor.execute("""
            SELECT * FROM customers WHERE username=? AND password=?
        """, (username, password))
        result = self.cursor.fetchone()
        if result:
            return Customer(*result[1:])

        self.cursor.execute("""
            SELECT * FROM cashiers WHERE username=? AND password=?
        """, (username, password))
        result = self.cursor.fetchone()
        if result:
            return Cashier(*result[1:])

        return None


class Customer:
    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name


class Cashier:
    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name