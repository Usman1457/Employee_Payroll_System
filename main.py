from database import create_tables
from employee import Employee
from attendance import Attendance
from payroll import Payroll
from report import Report
from auth import Auth

employee = Employee()
attendance = Attendance()
payroll = Payroll()
report = Report()
auth = Auth()


def menu():

    while True:

        print("\n========================================")
        print(" EMPLOYEE ATTENDANCE & PAYROLL SYSTEM ")
        print("========================================")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Employee Login")
        print("5. Check In")
        print("6. Check Out")
        print("7. View Attendance")
        print("8. Calculate Salary")
        print("9. Monthly Report")
        print("10. Export CSV")
        print("11. Export PDF")
        print("12. Exit")
        print("========================================")

        choice = input("Enter Choice : ")

        if choice == "1":
            employee.add_employee()

        elif choice == "2":
            employee.display_employees()

        elif choice == "3":
            employee.search_employee()

        elif choice == "4":

            user = auth.login()

            if user:
                print("Welcome", user[3])

        elif choice == "5":
            attendance.check_in()

        elif choice == "6":
            attendance.check_out()

        elif choice == "7":
            attendance.view_attendance()

        elif choice == "8":
            payroll.calculate_salary()

        elif choice == "9":
            payroll.monthly_report()

        elif choice == "10":
            report.export_csv()

        elif choice == "11":
            report.export_pdf()

        elif choice == "12":

            employee.close()
            attendance.close()
            payroll.close()
            report.close()

            print("\nThank You For Using Employee Payroll System")

            break

        else:
            print("\nInvalid Choice")


def main():

    create_tables()

    print("\n====================================")
    print("Employee Attendance & Payroll System")
    print("====================================")

    menu()


if __name__ == "__main__":
    main()