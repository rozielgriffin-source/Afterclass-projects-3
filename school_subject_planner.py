student_profile = ("Roziel", "Grade 10", "Section Z", 8)
 
print("Student Profile:", student_profile)

student_name = student_profile[0]
grade = student_profile[1]
section = student_profile[2]
total_subjects = student_profile[3]

print("\nStudent Name:", student_name)
print("Grade:", grade)
print("Section:", section)
print("Total Subjects:", total_subjects)
 
print("Middle two details:", student_profile[1:3])

monday_subjects = {"Biology", "Culinary", "English", "Computer", "P.E"}
tuesday_subjects = {"Avid", "History", "Math", "Sports", "Music"}
 
print("\nMondays classes:", monday_subjects)
print("Tuesday classes:", tuesday_subjects)

monday_subjects.add("Spanish")
print("\nAfter adding spanish to Monday:", monday_subjects)
 
monday_subjects.discard("P.E")
print("After removing P.E from Monday:", monday_subjects)
 
tuesday_subjects.add("Culinary")
print("After adding Culinary to Tuesday:", tuesday_subjects)
 
tuesday_subjects.discard("History")
print("After removing History from Tuesday:", tuesday_subjects)

all_subjects = monday_subjects.union(tuesday_subjects)
common_subjects = monday_subjects.intersection(tuesday_subjects)
only_monday = monday_subjects.difference(tuesday_subjects)
only_tuesday = tuesday_subjects.difference(monday_subjects)
different_subjects = monday_subjects.symmetric_difference(tuesday_subjects)
 
print("\nAll subjects:", all_subjects)
print("Common subjects:", common_subjects)
print("Monday only subjects:", only_monday)
print("Tuesday only subjects:", only_tuesday)
print("Different subjects:", different_subjects)

print("--------------------------------")
print("\nSCHOOL SUBJECT PLANNER SUMMARY")
print("--------------------------------")

print("\nStudent:", student_name)
print("Grade:", grade)
print("Monday subjects:", monday_subjects)
print("Tuesday subjects:", tuesday_subjects)
print("Subjects on both days:", common_subjects)
print("All unique subjects:", all_subjects)