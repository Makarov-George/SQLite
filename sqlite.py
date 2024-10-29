import _sqlite3

try:
    sqlite_connection = _sqlite3.connect('sqlite.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    def students_older_30(cursor):
        print('Студенты старше 30 лет:')
        cursor.execute('''SELECT name, surname from Students where age > 30''')
        rows = cursor.fetchall()
        for row in rows:
            print(row[0] + ' ' + row[1])

    def students_python(cursor):
        print('Студенты обущающиеся на курсе по питону:')
        cursor.execute('''SELECT id from Courses where name = "python"''')
        id_course = cursor.fetchall()
        for i in id_course:
            id_course = i
        
        cursor.execute('''SELECT student_id from Student_courses where course_id = ?''', id_course)
        id_student = cursor.fetchall()
        for i in id_student:
            id_student = i
            cursor.execute('''SELECT name, surname from Students where id = ?''', id_student)
            student = cursor.fetchall()
            for i in student:
                print(i[0] + ' ' + i[1])

    def students_python_Spb(cursor):
        print('Студенты обущающиеся на курсе по питону и живущие в Спб:')
        cursor.execute('''SELECT id from Courses where name = "python"''')
        id_course = cursor.fetchall()
        for i in id_course:
            id_course = i
        
        cursor.execute('''SELECT student_id from Student_courses where course_id = ?''', id_course)
        id_student = cursor.fetchall()
        for i in id_student:
            id_student = i
            cursor.execute('''SELECT name, surname from Students where id = ? and city = "Spb"''', id_student)
            student = cursor.fetchall()
            if len(student) != 0:
                for i in student:
                    print(i[0] + ' ' + i[1])
            else:
                break
    
    students_older_30(cursor)
    students_python(cursor)
    students_python_Spb(cursor)
    sqlite_connection.commit()
    print("Выполнено")
    cursor.close()

except _sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")