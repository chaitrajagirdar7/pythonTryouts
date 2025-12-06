# Creates a dictionary where student names are keys and their marks are values.
#   Asks the user to input a student's name.
#   Retrieves and displays the corresponding marks.
#   If the student’s name is not found, display an appropriate message.
Markssheet = {"anand": 50,
              "chaitra": 90,
              "govind": 67,
              "sriz": 77
              }
try:
    studentsname = input("key instudent name to know their marks: ")
    studentnamelist = Markssheet.keys()
    # print(studentnamelist)

    for key in studentnamelist:
        if key == studentsname:
            print(f"{studentsname}\'s marks is {Markssheet[key]}")
            break
    if key not in studentsname:
        print("Student name u entered is incorrect")

except Exception as e:
    print(f"An unexpected error occurred: {e}")