# Quinn Kwiatkowski
# UWYO COSC 1010
# Submission Date: 10/15/2024
# HW 01
# Lab Section: 14
# Sources, people worked with, help given to: None
# Homework Question: None

# You are given a list of dictionaries where each dictionary represents a student
# and their scores in different subjects.
# Student Data:

students = [
{"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
{"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
{"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
{"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}]
#print(students)

# Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.

# Your task is to calculate the average scores for each student and print the names of students whose average score is greater than 80.

# Solution:

# Empty list for the average grades
average_grade = {}
# Pull the grades, calculate the average and store them in the 'average_grade = []'
for student in students:
    name = student['name']
    scores = student['scores']
    average_scores = sum(scores.values())/len(scores) # Part 1 of the HW
    average_grade[name] = average_scores # Part 2 of the HW

print(average_grade)
#prints (1 and 2 combined):
#{'Alice': 84.33333333333333, 'Bob': 80.0, 'Charlie': 87.33333333333333, 'David': 71.66666666666667}

# Use an if statement to pull out names of students whose average grades are larger than 80 
for name, average_grade in average_grade.items(): 
    if average_grade > 80:
        print(name)
#prints (3):
#Alice
#Charlie
#NOTE: does not print bob because the average score is exactly 80, and the function only pulls the name if it is greater than 80.