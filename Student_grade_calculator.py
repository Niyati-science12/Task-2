def student_grade_calculator(marks):
    if marks>=90 and marks<=100:
        return ("A")
    elif marks>=80 and marks<90:
        return ("B")
    elif marks>=70 and marks<80:
        return ("C")
    elif marks>=60 and marks<70:
        return ("D")
    else:
        return ("F")
name= input("Enter student name:")
marks=int(input("Enter marks(0-100):"))
Grade= student_grade_calculator(marks)
print("RESULT FOR", name,":")
print("Marks:", marks,"/100")
print("Grade:", Grade)
if Grade in ["A", "B"]:
    print("Message: Very Good! Keep it up!")
elif Grade in ["C", "D"]:
    print("Message: You can do better.")
else:
    print("Message: Needs improvement.")
        
