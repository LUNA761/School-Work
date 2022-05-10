students = []

def calc_grade(score) -> str:
    if score <= 50 and score > 41:
        return "A"

    elif score > 31 and score < 50:
        return "B"

    elif score > 21 and score < 50:
        return "C"

    elif score > 11 and score < 50:
        return "D"

    elif score > 10 and score < 0:
        return "U"

    else:
        return ""

def calc_score(grade: str) -> int:
    if grade == "A":
        return 50
    elif grade == "B":
        return 40
    elif grade == "C":
        return 30
    elif grade == "D":
        return 20
    elif grade == "U":
        return 10

def is_score_higher_than_target(student) -> bool:
    return student["score"] > calc_score(student["target_grade"])

def is_target_higher_than_score(student) -> bool:
    return student["score"] < calc_score(student["target_grade"])

def score_same_as_target(student) -> bool:
    return calc_grade(student["score"]) == student["target_grade"]

def input_students():
    global students

    while 1:
        new_student = {}
        
        new_student["name"] = input("Please enter the student name ~ ").lower()
        new_student["score"] = int(input("Please enter the student's score ~ "))
        new_student["target_grade"] = input("Please enter the student's target grade ~").upper()

        students.append(new_student)

        again = input("Would you like to add another student? [y/n] ~").lower()
        if again == "n":
            break
        elif again == "y":
            continue
        else:
            print("That was not a valid option!")
            break

def print_student_data():
    global students

    for student in students:
        if score_same_as_target(student):
            print(f'{student["name"].title()} met their target grade!')
        
        elif is_score_higher_than_target(student):
            print(f'{student["name"].title()} passed their target grade. Well done!')

        elif is_target_higher_than_score(student):
            print(f'{student["name"].title()} didn`t reach target grade!')

input_students()
print_student_data()
            
        
