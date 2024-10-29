import _sqlite3

try:
    sqlite_connection = _sqlite3.connect('sqlite.db')
    print("База данных создана и успешно подключена к SQLite\n")
    class Data_base():
        def __init__(self, cursor):
            self.C = cursor
        
        def set(self, cursor):
            self.C = cursor
        
        def get(self):
            return self.C
        
        def CreateTable(self):
            self.C.execute('''CREATE TABLE if not exists Students (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                surname TEXT NOT NULL,
                                age INTEGER NOT NULL,
                                city TEXT NOT NULL);''')
            self.C.execute('''CREATE TABLE if not exists Courses (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                time_start TEXT NOT NULL,
                                time_end TEXT NOT NULL);''')
            self.C.execute('''CREATE TABLE if not exists Student_courses (
                                student_id INTEGER,
                                course_id INTEGER,
                                FOREIGN KEY(student_id) REFERENCES Students(id),
                                FOREIGN KEY(course_id) REFERENCES Courses(id));''')
            sqlite_connection.commit()
            print("Таблицы были созданы или проверены, что они уже есть\n")
        
        def Check(self):
            self.C.execute('''SELECT * from Students''')
            check = self.C.fetchall()
            if len(check) != 0:
                print('Таблица Students уже заполнена')
            else:
                print('Таблица Students была пуста, но мы ее заполнили)')
                students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
                self.C.executemany('''INSERT INTO Students VALUES(?, ?, ?, ?, ?)''', students)
                sqlite_connection.commit()
            
            self.C.execute('''SELECT * from Courses''')
            check = self.C.fetchall()
            if len(check) != 0:
                print('Таблица Courses уже заполнена')
            else:
                print('Таблица Courses была пуста, но мы ее заполнили)')
                courses = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]
                self.C.executemany('''INSERT INTO Courses VALUES(?, ?, ?, ?, ?)''', courses)
                sqlite_connection.commit()
            
            self.C.execute('''SELECT * from Student_courses''')
            check = self.C.fetchall()
            if len(check) != 0:
                print('Таблица Student_courses уже заполнена\n')
            else:
                print('Таблица Student_courses была пуста, но мы ее заполнили)\n')
                students_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]
                self.C.executemany('''INSERT INTO Student_courses VALUES(?, ?, ?, ?, ?)''', students_courses)
                sqlite_connection.commit()

        def students_older_30(self):
            print('Студенты старше 30 лет:')
            self.C.execute('''SELECT name, surname from Students where age > 30''')
            rows = self.C.fetchall()
            for row in rows:
                print(row[0] + ' ' + row[1])
            print()
        
        def students_python(self):
            print('Студенты обущающиеся на курсе по питону:')
            self.C.execute('''SELECT id from Courses where name = "python"''')
            id_course = self.C.fetchall()
            for i in id_course:
                id_course = i
            
            self.C.execute('''SELECT student_id from Student_courses where course_id = ?''', id_course)
            id_student = self.C.fetchall()
            for i in id_student:
                id_student = i
                self.C.execute('''SELECT name, surname from Students where id = ?''', id_student)
                student = self.C.fetchall()
                for i in student:
                    print(i[0] + ' ' + i[1])
            print()

        def students_python_Spb(self):
            print('Студенты обущающиеся на курсе по питону и живущие в Спб:')
            self.C.execute('''SELECT id from Courses where name = "python"''')
            id_course = self.C.fetchall()
            for i in id_course:
                id_course = i
            
            self.C.execute('''SELECT student_id from Student_courses where course_id = ?''', id_course)
            id_student = self.C.fetchall()
            for i in id_student:
                id_student = i
                self.C.execute('''SELECT name, surname from Students where id = ? and city = "Spb"''', id_student)
                student = self.C.fetchall()
                if len(student) != 0:
                    for i in student:
                        print(i[0] + ' ' + i[1])
                else:
                    break
            print()

        def Base_info(self):
            self.CreateTable()
            self.Check()
            self.students_older_30()
            self.students_python()
            self.students_python_Spb()

        sqlite_connection.commit()
    SQLite = Data_base(sqlite_connection.cursor())
    SQLite.Base_info()
except _sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")