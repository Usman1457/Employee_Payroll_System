import sqlite3

DATABASE = "employees.db"


class Payroll:

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()


    # Calculate Salary

    def calculate_salary(self):

        employee_id = int(input("Enter Employee ID : "))

        self.cursor.execute(
            """
            SELECT *
            FROM employees
            WHERE id=?
            """,
            (employee_id,)
        )

        employee = self.cursor.fetchone()

        if employee is None:

            print("\nEmployee Not Found\n")
            return

        basic_salary = employee[5]

        self.cursor.execute(
            """
            SELECT SUM(overtime)
            FROM attendance
            WHERE employee_id=?
            """,
            (employee_id,)
        )

        overtime = self.cursor.fetchone()[0]

        if overtime is None:
            overtime = 0

        overtime_rate = 500

        overtime_salary = overtime * overtime_rate

        total_salary = basic_salary + overtime_salary

        print("\n========== PAYROLL ==========\n")
        print("Employee :", employee[3])
        print("Department :", employee[4])
        print("Basic Salary :", basic_salary)
        print("Overtime Hours :", round(overtime, 2))
        print("Overtime Salary :", overtime_salary)
        print("------------------------------")
        print("Total Salary :", total_salary)

    # --------------------------
    # Monthly Report
    # --------------------------

    def monthly_report(self):

        self.cursor.execute(
            """
            SELECT
            employees.id,
            employees.name,
            employees.department,
            employees.basic_salary,
            IFNULL(SUM(attendance.overtime),0)

            FROM employees

            LEFT JOIN attendance

            ON employees.id=attendance.employee_id

            GROUP BY employees.id
            """
        )

        rows = self.cursor.fetchall()

        print("\n========== MONTHLY REPORT ==========\n")

        for row in rows:

            overtime_salary = row[4] * 500

            total_salary = row[3] + overtime_salary

            print("Employee ID :", row[0])
            print("Name :", row[1])
            print("Department :", row[2])
            print("Basic Salary :", row[3])
            print("Overtime :", round(row[4],2), "Hours")
            print("Total Salary :", total_salary)
            print("------------------------------------")

    def close(self):
        self.conn.close()