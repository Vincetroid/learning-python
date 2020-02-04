#example 1
student_attendance = {"Rolf": 45, "Bob": 34, "Anne": 24}

for student in student_attendance:
    print(f"Student {student}: {student_attendance[student]}") 

#example 2
attendance_values = student_attendance.values()
average = sum(attendance_values) / len(attendance_values)
print(average)