import sqlite3

DATABASE = "employees.db"


def connect_db():
    return sqlite3.connect(DATABASE)


def create_tables():

    conn = connect_db()
    cursor = conn.cursor()

    # Employee Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        name TEXT,
        department TEXT,
        basic_salary REAL
    )
    """)

    # Attendance Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        date TEXT,
        check_in TEXT,
        check_out TEXT,
        overtime REAL,
        FOREIGN KEY(employee_id) REFERENCES employees(id)
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database Created Successfully")