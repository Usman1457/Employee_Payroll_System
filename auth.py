import sqlite3

DATABASE = "employees.db"


class Auth:

    def login(self):

        username = input("Username : ")
        password = input("Password : ")

        conn = sqlite3.connect(DATABASE)

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM employees
            WHERE username=? AND password=?
            """,
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            print("\nLogin Successful\n")
            return user

        else:

            print("\nInvalid Username or Password\n")
            return None