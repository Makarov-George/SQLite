import _sqlite3

try:
    sqlite_connection = _sqlite3.connect('sqlite.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_create_table_students = '''CREATE TABLE Students (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                surname TEXT NOT NULL,
                                age INTEGER NOT NULL,
                                city TEXT NOT NULL);'''
    
    sqlite_create_table_courses = '''CREATE TABLE Courses (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                time_start TEXT NOT NULL,
                                time_end TEXT NOT NULL);'''
    
    sqlite_create_table_student_courses = '''CREATE TABLE Student_courses (
                                student_id INTEGER,
                                course_id INTEGER,
                                FOREIGN KEY(student_id) REFERENCES Students(id),
                                FOREIGN KEY(course_id) REFERENCES Courses(id));'''
    
    cursor.execute(sqlite_create_table_students)
    cursor.execute(sqlite_create_table_courses)
    cursor.execute(sqlite_create_table_student_courses)
    sqlite_connection.commit()
    print("Таблицы созданы")
    cursor.close()

except _sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")