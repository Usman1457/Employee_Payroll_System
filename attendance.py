import sqlite3
from datetime import datetime

DATABASE = "employees.db"


class Attendance:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()

    # Check In
  
    def check_in(self):

        employee_id = int(input("Employee ID : "))

        today = datetime.now().strftime("%Y-%m-%d")

        time = datetime.now().strftime("%H:%M:%S")

        self.cursor.execute(
            """
            INSERT INTO attendance
            (employee_id,date,check_in,check_out,overtime)
            VALUES(?,?,?,?,?)
            """,
            (
                employee_id,
                today,
                time,
                "",
                0
            )
        )

        self.conn.commit()

        print("\nAttendance Marked Successfully.\n")

   
    # Check Out

    def check_out(self):

        employee_id = int(input("Employee ID : "))

        today = datetime.now().strftime("%Y-%m-%d")

        current_time = datetime.now()

        self.cursor.execute(
            """
            SELECT id,check_in
            FROM attendance
            WHERE employee_id=?
            AND date=?
            AND check_out=''
            """,
            (
                employee_id,
                today
            )
        )

        row = self.cursor.fetchone()

        if row is None:

            print("\nNo Check-In Found.\n")
            return

        attendance_id = row[0]

        check_in = datetime.strptime(
            row[1],
            "%H:%M:%S"
        )

        checkout = current_time.strftime("%H:%M:%S")

        worked_hours = (
            current_time - check_in
        ).seconds / 3600

        overtime = 0

        if worked_hours > 8:

            overtime = worked_hours - 8

        self.cursor.execute(
            """
            UPDATE attendance
            SET check_out=?,
                overtime=?
            WHERE id=?
            """,
            (
                checkout,
                overtime,
                attendance_id
            )
        )

        self.conn.commit()

        print("\nChecked Out Successfully")

        print("Worked Hours :", round(worked_hours,2))

        print("Overtime :", round(overtime,2),"Hours")

    # View Attendance


    def view_attendance(self):

        self.cursor.execute(
            "SELECT * FROM attendance"
        )

        rows = self.cursor.fetchall()

        if len(rows)==0:

            print("\nNo Attendance Found\n")

            return

        print("\n========== ATTENDANCE ==========\n")

        for row in rows:

            print("Record ID :",row[0])
            print("Employee ID :",row[1])
            print("Date :",row[2])
            print("Check In :",row[3])
            print("Check Out :",row[4])
            print("Overtime :",row[5],"Hours")
            print("--------------------------")

    def close(self):

        self.conn.close()