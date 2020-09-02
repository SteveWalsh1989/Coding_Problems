"""
From Hacker R
HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  0 - 100 .
Any  less than 40  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the  grade  and the next multiple of 5  is less than 3, round  grade up to the next multiple of .
If the value of  is less than 38 , no rounding occurs as the result will still be a failing grade.

Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

Function Description

Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.

gradingStudents has the following parameter(s):

grades: an array of integers representing grades before rounding
The first line contains a single integer, , the number of students.
Each line  of the  subsequent lines contains a single integer, , denoting student 's grade.

"""


def grading(grades):
    """rounds up grades """
    # declare return value
    results = []

    # iterate through grades
    for grade in grades:
        # check passing grade and difference for rounding
        if grade >= 38 and grade % 5 >= 3:
            # round up grade
            grade = (grade + 5) - (grade % 5)

        # add to results
        results.append(grade)

    return results


def main():
    """ Main function """

    grades = [4, 77, 38, 91, 67]

    results = grading(grades)

    print(f"Grades: {grades}")
    print(f"results: {results}")


''' Run Program '''
main()