# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))#Faiqua Fatima added int() and fixed paranthesis
exam_three = int(input("Input exam grade three: "))#str->int by faiqua

grades = [exam_one,exam_two,exam_three]# Faiqua Fatima added comas to seperate the items in list
sum = 0
for grade in grades: #changed from "grade in grade" to "grade in grades" by Faiqua Fatima
  sum = sum + grade

avg = sum / len(grades) #Faiqua Fatima changed "grdes" to "grades"

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:#Faiqua Fatima added ":"
    letter_grade = "B"
elif avg >=70 and avg < 80:#Faiqua Fatima changed ">69" to ">=70"
    letter_grade = "C" #"C' changed to "C" by Faiqua
elif avg >= 60 and avg <70:#Faiqua Fatima changed "<= 69" to ">= 60" and ">= 65" to "<70"
    letter_grade = "D"
else: #elif changed to else by Faiqua Fatima
    letter_grade = "F"

for grade in grades: #"for grade in grade" changed to "for grade in grades" by Faiqua
    print("Exam: " + str(grades))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade =="F":#"letter-grade" changed to "letter_grade" by Faiqua, is replaced by ==
    print ("Student is failing.")#Faiqua added paranthesis after print statement
else:
    print ("Student is passing.")#Faiqua added paranthesis after print statement
