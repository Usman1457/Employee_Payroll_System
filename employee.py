import sqlite3

DATABASE = "employees.db"


class Employee:

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()

    def add_employee(self):

        username = input("Username : ")
        password = input("Password : ")
        name = input("Employee Name : ")
        department = input("Department : ")
        salary = float(input("Basic Salary : "))

        self.cursor.execute("""
        INSERT INTO employees
        (username,password,name,department,basic_salary)
        VALUES(?,?,?,?,?)
        """,
        (
            username,
            password,
            name,
            department,
            salary
        ))

        self.conn.commit()

        print("\nEmployee Added Successfully.\n")

    def display_employees(self):

        self.cursor.execute("SELECT * FROM employees")

        employees = self.cursor.fetchall()

        if not employees:

            print("\nNo Employees Found.\n")
            return

        print("\n========== EMPLOYEE LIST ==========\n")

        for emp in employees:

            print("ID :", emp[0])
            print("Username :", emp[1])
            print("Name :", emp[3])
            print("Department :", emp[4])
            print("Salary :", emp[5])
            print("-----------------------------")

    def search_employee(self):

        emp_id = int(input("Employee ID : "))

        self.cursor.execute(
            "SELECT * FROM employees WHERE id=?",
            (emp_id,)
        )

        emp = self.cursor.fetchone()

        if emp:

            print("\nEmployee Found\n")

            print("ID :", emp[0])
            print("Name :", emp[3])
            print("Department :", emp[4])
            print("Salary :", emp[5])

        else:

            print("\nEmployee Not Found")

    def close(self):

        self.conn.close()