# Lab 11
import math
import os
import matplotlib.pyplot as plt


def main():
    # printing menu
    print("1.Student grade")
    print("2.Assignment statistics")
    print("3.Assignment graph")
    print()

    option = input("Enter your selection: ")

    if option == "1":
        # ask the user for a student name
        name = input("What is the student's name: ")

        # Their grade should then be printed out as a percentage, rounded to the nearest whole percentage

        # Check list of students
        student_found = False

        # Open the file safely using with statement
        with open("data/students.txt") as file:
            for line in file:
                the_id = line[0:3]
                line = line[3:]
                # Remove leading/trailing whitespace like newlines
                if line.strip() == name:
                    student_found = True
                    break

        # If the student was not found after the loop, print "Student not found"
        if not student_found:
            print("Student not found")
        else:
            grade = 0

            # list of assignments
            new_file = open("data/assignments.txt")
            new_lines = new_file.readlines()
            new_file.close()
            new_lines = [line.strip() for line in new_lines]

            # calculate that student’s grade for the entire course
            for filename in os.listdir("data/submissions"):
                file_path = os.path.join("data/submissions", filename)
                # print(f"Processing file: {file_path}")
                # Now you can open and process the file
                with open(file_path, 'r') as file:
                    content = file.read()
                    temp_stud_id = content[0:3]
                    if the_id == temp_stud_id:
                        temp_assign_id = content[4:-3]
                        for i in range(len(new_lines)):
                            if new_lines[i] == temp_assign_id:
                                points = new_lines[i + 1]
                                grade += (int(content[-2:])) * (int(points) / 1000)

            print(round(grade), "%", sep="")

        '''
        file = open("data/students.txt")
        for line in file:
            the_id = line[0:3]
            line = line[3:]
            print(line)
            if line == name:
                print("FOUND")
                print(name)
                print(the_id)
                
                # calculate that student’s grade for the entire course
                for filename in os.listdir("data/submissions"):
                    file_path = os.path.join("data/submissions", filename)
                    print(f"Processing file: {file_path}")
                    # Now you can open and process the file
                    with open(file_path, 'r') as file:
                        content = file.read()
                        # Do something with the content
                        print(content)
                
                break

            else:
                # or print “Student not found” if the student does not exist
                print("Student not found")
                break
            '''

    elif option == "2":
        # prompt the user for an assignment name
        assignment = input("What is the assignment name: ")
        # find the maximum, average, and minimum percent scores for all submissions for that assignment
        # If the assignment doesn’t exist, print “Assignment not found”.
        # list of assignments
        new_file = open("data/assignments.txt")
        new_lines = new_file.readlines()
        new_file.close()
        new_lines = [line.strip() for line in new_lines]

        assign_not_found = True
        for line in new_lines:
            if line == assignment:
                assign_not_found = False
        if assign_not_found:
            print("Assignment not found")
        else:
            grades = []

            for i in range(len(new_lines)):
                if new_lines[i] == assignment:
                    temp_target_assign_id = new_lines[i + 1]

            # calculate that student’s grade for the entire course
            for filename in os.listdir("data/submissions"):
                file_path = os.path.join("data/submissions", filename)
                with open(file_path, 'r') as file:
                    content = file.read()
                    temp_assign_id = content[4:-3]
                    if temp_assign_id == temp_target_assign_id:
                        grades.append(int(content[-2:]))

            # Find Min
            min_grade = grades[0]
            for grade in grades:
                if grade < min_grade:
                    min_grade = grade
            print(f"Min: {min_grade}%")

            # Find Avg
            total = 0
            for grade in grades:
                total += grade
            avg_grade = total / len(grades)
            print(f"Avg: {math.floor(avg_grade)}%")

            # Find Max
            max_grade = grades[0]
            for grade in grades:
                if grade > max_grade:
                    max_grade = grade
            print(f"Max: {max_grade}%")


    else:
        # prompt the user for an assignment name
        # If the assignment does not exist, print “Assignment not found”
        assignment = input("What is the assignment name: ")

        # list of assignments
        new_file = open("data/assignments.txt")
        new_lines = new_file.readlines()
        new_file.close()
        new_lines = [line.strip() for line in new_lines]

        assign_not_found = True
        for line in new_lines:
            if line == assignment:
                assign_not_found = False
        if assign_not_found:
            print("Assignment not found")
        else:
            # If the assignment does exist, the program should display a histogram of the assignment scores
            scores = []
            temp_target_assign_id_two = None

            for i in range(len(new_lines)):
                if new_lines[i] == assignment:
                    temp_target_assign_id_two = new_lines[i + 1]

            # calculate that student’s grade for the entire course
            for filename in os.listdir("data/submissions"):
                file_path = os.path.join("data/submissions", filename)
                with open(file_path, 'r') as file:
                    content = file.read()
                    temp_assign_id = content[4:-3]
                    if temp_assign_id == temp_target_assign_id_two:
                        scores.append(int(content[-2:]))

            plt.hist(scores, bins=[50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
            plt.show()


if __name__ == "__main__":
    main()
