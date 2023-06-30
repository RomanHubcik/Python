student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99, 
    "Draco" : 74,
    "Neville" : 62,
}

student_grades = {}


#Conversion
for item in student_scores:
    if student_scores[item] > 90:
        student_grades[item] = "Outstanding"
    elif student_scores[item] > 80:
        student_grades[item] = "Exceeds Expectations"
    elif student_scores[item] > 70: 
        student_grades[item] = "Acceptable"
    else:
        student_grades[item] = "Fail"


print(student_scores)
print(student_grades)