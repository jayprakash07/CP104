"""
-------------------------------------------------------
Lab 2, Task 13
-------------------------------------------------------
Author:  Jayprakash Pathak
ID:      169018920
Email:   path8920@mylaurier.ca
__updated__ = "2022-09-21"
-------------------------------------------------------
"""
MIDTERM_WEIGHT = 0.35
EXAM_WEIGHT = 0.65

midterm_mark = float(input("Mid-term Mark (%): "))
exam_mark = float(input("Exam Mark (%): "))

final_midterm_mark = (midterm_mark * MIDTERM_WEIGHT)
final_exam_mark = (exam_mark * EXAM_WEIGHT)
final_grade = final_midterm_mark + final_exam_mark

print(f"\nFinal Grade (%): {final_grade}")
