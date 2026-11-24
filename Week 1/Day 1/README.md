# Day 1: Student Performance Analyzer

A simple interactive command-line Python program to calculate a student's total marks, average percentage, grade, and pass/fail result based on user input.

## Concepts Used
- Basic variables and user input (`input()`)
- Data types: `int`, `float`, `str`, `list`
- Loops: `for` loop to collect marks and calculate total, `while` loop for validation
- Conditionals: `if`, `elif`, `else` to assign grades and pass/fail status

## Grading Scheme
- `>= 90%` : Grade A
- `>= 75%` : Grade B
- `>= 60%` : Grade C
- `>= 40%` : Grade D
- `< 40%` : Grade F (Fail)

## How to Run

1. Open terminal in the Day 1 folder:
   ```bash
   cd "Week 1/Day 1"
   ```
2. Run the script:
   ```bash
   python main.py
   ```

## Sample Run

```text
----- Student Performance Analyzer -----
Enter student name: John Doe
Enter number of subjects: 3

Enter subject name: Maths
Enter marks (0-100): 85

Enter subject name: Physics
Enter marks (0-100): 72

Enter subject name: Chemistry
Enter marks (0-100): 38

===============================
         STUDENT REPORT        
===============================
Student Name: John Doe
No of Subjects: 3
-------------------------------
Maths : 85.0
Physics : 72.0
Chemistry : 38.0
-------------------------------
Total Marks: 195.0 / 300
Average Percentage: 65.0 %
Grade: C
Final Result: Pass
===============================
```
