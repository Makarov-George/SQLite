import _sqlite3

try:
    sqlite_connection = _sqlite3.connect('sqlite.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
    courses = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]
    students_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]
    cursor.executemany("INSERT INTO Students VALUES(?, ?, ?, ?, ?)", students)
    cursor.executemany("INSERT INTO Courses VALUES(?, ?, ?, ?)", courses)
    cursor.executemany("INSERT INTO Student_courses VALUES(?, ?)", students_courses)
    sqlite_connection.commit()
    print("Таблицы заполнены")
    cursor.close()

except _sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")