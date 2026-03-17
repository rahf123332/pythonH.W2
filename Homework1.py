students = []
students.append(["Ali", 75])
students.append(["Sara", 88])
students.append(["Omar", 45])
students.insert(2, ["Lina", 90])
students[2][0] = "Mona"
passed_students = []
for s in students:
    if s[1] >= 50:
        passed_students.append(s)
print("Students List:", students)
print("Passed Students:", passed_students)
