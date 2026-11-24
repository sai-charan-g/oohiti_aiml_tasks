
name = input("Enter student name: ")

num_subjects = int(input("Enter number of subjects: "))

subject_names = []
marks_list = []

for i in range(num_subjects):
    sub = input("\nEnter subject name: ")
    
    marks = float(input("Enter marks (0-100): "))
    
    while marks < 0 or marks > 100:
        print("Invalid marks! Please enter between 0 and 100.")
        marks = float(input("Enter marks again: "))
        
    subject_names.append(sub)
    marks_list.append(marks)

total = 0
for m in marks_list:
    total = total + m

average = total / num_subjects

grade = ""
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

if average >= 40:
    result = "Pass"
else:
    result = "Fail"

print("         STUDENT REPORT        ")
print("Student Name:", name)
print("No of Subjects:", num_subjects)

for i in range(num_subjects):
    print(subject_names[i], ":", marks_list[i])

print("Total Marks:", total, "/", num_subjects * 100)
print("Average Percentage:", round(average, 2), "%")
print("Grade:", grade)
print("Final Result:", result)
