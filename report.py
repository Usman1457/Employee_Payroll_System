import sqlite3
import csv
import os

DATABASE = "employees.db"


class Report:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE)
        self.cursor = self.conn.cursor()

    # ----------------------------
    # Export CSV
    # ----------------------------

    def export_csv(self):

        self.cursor.execute("""
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
        """)

        rows = self.cursor.fetchall()

        if not os.path.exists("exports"):
            os.mkdir("exports")

        file = open("exports/monthly_report.csv",
                    "w",
                    newline="")

        writer = csv.writer(file)

        writer.writerow([
            "Employee ID",
            "Name",
            "Department",
            "Basic Salary",
            "Overtime Hours",
            "Total Salary"
        ])

        for row in rows:

            overtime_salary = row[4] * 500

            total_salary = row[3] + overtime_salary

            writer.writerow([
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                total_salary
            ])

        file.close()

        print("\nCSV Report Generated Successfully")

    # ----------------------------
    # Export PDF
    # ----------------------------

    def export_pdf(self):

        try:

            from reportlab.pdfgen import canvas

        except ImportError:

            print("\nInstall ReportLab First")
            print("pip install reportlab")
            return

        if not os.path.exists("reports"):
            os.mkdir("reports")

        pdf = canvas.Canvas("reports/monthly_report.pdf")

        pdf.setFont("Helvetica-Bold",16)

        pdf.drawString(170,800,"Employee Payroll Report")

        self.cursor.execute("""
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
        """)

        rows=self.cursor.fetchall()

        y=760

        pdf.setFont("Helvetica",10)

        for row in rows:

            overtime=row[4]*500

            total=row[3]+overtime

            pdf.drawString(
                30,
                y,
                f"ID:{row[0]}  Name:{row[1]}  Salary:{total}"
            )

            y-=20

            if y<50:

                pdf.showPage()

                y=780

        pdf.save()

        print("\nPDF Report Generated Successfully")

    def close(self):

        self.conn.close()