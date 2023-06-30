student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99, 
    "Draco" : 74,
    "Neville" : {"score" : 62, "long" : 32}
}

for key in student_scores:
    print(key, student_scores[key])

print(student_scores["Neville"]["score"])