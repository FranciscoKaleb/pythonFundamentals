


# student_id, first_name, last_name, age, course 
students = [
    [1, "John", "Doe", 20, "Computer Science"],
    [2, "Jane", "Smith", 22, "Mathematics"],
    [3, "Emily", "Johnson", 19, "Physics"],
    [4, "Michael", "Brown", 21, "Chemistry"]
]
def add_student(id, fn, ln, a, c):
    global students
    students.append([id,fn,ln,a,c])
    print('successfully added')
    print_student()

def print_student():
    global students
    for student in students:
        print(f' id: {student[0]}\n First name: {student[1]}\n Last name: {student[2]}\n Age: {student[3]}\n Course: {student[4]}\n\n')
keep_running = True
def run():
    global keep_running, students
    while keep_running == True:
        print('Choose a number:')
        print('[1] add a student')
        print('[2] print students')
        print('[3] print students sorted by age')
        print('[4] print students sorted by last name')
        print('[5] exit')
        x = input()
        if x == "1":
            print('Enter student id:')
            id = int(input())
            print('Enter student first name')
            fn = input()
            print('Enter student last name')
            ln = input()
            print('Enter student age:')
            a = int(input())
            print('Enter course:')
            c = input()
            add_student(id, fn, ln, a, c)
            run()
        elif x == "2":
            print_student()
            run()
        else:
            keep_running = False
            print('program end')
            
run()




