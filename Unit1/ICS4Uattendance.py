totalClasses = int(input("Enter total # of classes: "))
classesAttended = int(input("Enter total # of class attended: "))

attendance = (classesAttended/totalClasses)*100
print("Your attendance is",attendance,"%")

if attendance < 75:
    print("You are not allowed to sit in the exam")
else:
    print("You are allowed to sit in the exam")
exit(0)