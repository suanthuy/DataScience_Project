#read file
with  open("clean_data.csv", encoding="utf8") as file:
    data = file.read().split("\n")

header = data[0]
students = data[1:]

#remove last student (empty student)
students.pop()

#split header
header = header.split(",")
subject = header[5:]

total_student = len(students)

#split each student in list
for i in range(len(students)):
    students[i] = students[i].split(",")

students.pop()

num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,0,0]

for s in students:
   for i in range(11):
       pass

