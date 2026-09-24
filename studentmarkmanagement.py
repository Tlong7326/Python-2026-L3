def add_students(students):
	number = int(input("Number of students: "))
	for _ in range(number):
		student_id = input("Student ID: ")
		name = input("Student name: ")
		dob = input("Date of birth: ")
		students[student_id] = [name, dob]


def add_courses(courses):
	number = int(input("Number of courses: "))
	for _ in range(number):
		course_id = input("Course ID: ")
		courses[course_id] = input("Course name: ")


def add_marks(students, courses, marks):
	course_id = input("Course ID: ")
	if course_id not in courses:
		print("Course not found.")
		return

	marks[course_id] = {}
	for student_id in students:
		mark = float(input(f"Mark for {students[student_id][0]}: "))
		marks[course_id][student_id] = mark


def show_students(students):
	for student_id, student in students.items():
		print(student_id, student[0], student[1])


def show_courses(courses):
	for course_id, course_name in courses.items():
		print(course_id, course_name)


def show_marks(students, courses, marks):
	course_id = input("Course ID: ")
	if course_id not in courses:
		print("Course not found.")
		return

	print("Marks for", courses[course_id])
	for student_id, student in students.items():
		mark = marks.get(course_id, {}).get(student_id, "Not entered")
		print(student[0], mark)


def main():
	students = {}
	courses = {}
	marks = {}

	while True:
		print("\nStudent Mark Management")
		print("1. Input students")
		print("2. Input courses")
		print("3. Input marks for a course")
		print("4. List students")
		print("5. List courses")
		print("6. Show student marks for a course")
		print("0. Exit")

		choice = input("Choose an option: ").strip()
		if choice == "1":
			add_students(students)
		elif choice == "2":
			add_courses(courses)
		elif choice == "3":
			add_marks(students, courses, marks)
		elif choice == "4":
			show_students(students)
		elif choice == "5":
			show_courses(courses)
		elif choice == "6":
			show_marks(students, courses, marks)
		elif choice == "0":
			print("Goodbye!")
			break
		else:
			print("Invalid option.")


if __name__ == "__main__":
	main()