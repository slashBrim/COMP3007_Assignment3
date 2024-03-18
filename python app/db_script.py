import psycopg
from psycopg.rows import dict_row

def get_connection():
    # Replace these values with your PostgreSQL database details
    conn = psycopg.connect(
        dbname="", 
        user="",
        password="",
        host=""
    )
    return conn

# retrieve and display all records from the students table.
def getAllStudents():
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("SELECT * FROM students")
            students = cur.fetchall()
            for student in students:
                print(student)
# insert a new student record
def addStudent(first_name, last_name, email, enrollment_date):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                        (first_name, last_name, email, enrollment_date))
            conn.commit()
# update the email of a student.
def updateStudentEmail(student_id, new_email):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                        (new_email, student_id))
            conn.commit()

# delete a student record.
def deleteStudent(student_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s",
                        (student_id,))
            conn.commit()

# Example Usage.
#getAllStudents()
#addStudent('Ite', 'Awogbemi', 'ite.awog@example.com', '2024-03-15')
#updateStudentEmail(1, 'new.email@example.com')
#deleteStudent(3)
