# Student Grading System Project - Complete Guide

## Project Overview

Build a comprehensive student grading system that handles multiple students, calculates grades using configurable grading scales, computes statistics, and provides detailed reports. This project demonstrates data structures, algorithms, file I/O, and object-oriented programming principles.

**Skills Demonstrated:**
- Data structures (lists, dictionaries, classes)
- Input validation and error handling
- Statistical calculations
- File I/O (CSV import/export)
- Configuration management
- Report generation
- Object-oriented design

**Project Difficulty:** Intermediate  
**Estimated Time:** 4-6 hours  
**Prerequisites:** Python basics, functions, data structures, file handling

---

## Version 1: Basic Single-Student Grader

### Features
- Fixed subject list
- Simple grading scale (A-F)
- Calculate total, average, percentage
- Assign letter grade

### Complete Code

```python
"""
Student Grading System - Version 1 (Basic)
Single student, fixed subjects
"""

# Configuration
SUBJECTS = ["Math", "Physics", "Chemistry", "English", "Biology"]

GRADE_SCALE = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F"),
]

def get_letter_grade(percentage):
    """
    Return letter grade based on percentage.
    
    Args:
        percentage: Score percentage (0-100)
    
    Returns:
        str: Letter grade
    """
    for cutoff, letter in GRADE_SCALE:
        if percentage >= cutoff:
            return letter
    return "F"

def get_subject_score(subject_name):
    """
    Get valid score for a subject.
    
    Args:
        subject_name: Name of the subject
    
    Returns:
        float: Valid score (0-100)
    """
    while True:
        try:
            score = float(input(f"Enter {subject_name} score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("  ❌ Score must be between 0 and 100. Try again.")
        except ValueError:
            print("  ❌ Invalid number. Try again.")

def main():
    """Main grading system."""
    print("\n" + "=" * 60)
    print("         STUDENT GRADING SYSTEM")
    print("=" * 60)
    
    # Get student name
    student_name = input("\nEnter student name: ").strip()
    if not student_name:
        student_name = "Anonymous"
    
    # Collect scores
    print(f"\nEnter scores for {student_name}:")
    scores = {}
    for subject in SUBJECTS:
        scores[subject] = get_subject_score(subject)
    
    # Calculate results
    total = sum(scores.values())
    max_possible = len(SUBJECTS) * 100
    percentage = (total / max_possible) * 100
    letter_grade = get_letter_grade(percentage)
    
    # Display report card
    print("\n" + "=" * 60)
    print(f"        REPORT CARD - {student_name.upper()}")
    print("=" * 60)
    
    for subject, score in scores.items():
        grade = get_letter_grade(score)
        print(f"{subject:<15}: {score:6.2f}  ({grade})")
    
    print("-" * 60)
    print(f"{'Total':<15}: {total:6.2f} / {max_possible}")
    print(f"{'Percentage':<15}: {percentage:6.2f}%")
    print(f"{'Final Grade':<15}: {letter_grade}")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

### Sample Output

```
============================================================
         STUDENT GRADING SYSTEM
============================================================

Enter student name: Alice Johnson

Enter scores for Alice Johnson:
Enter Math score (0-100): 92
Enter Physics score (0-100): 85
Enter Chemistry score (0-100): 78
Enter English score (0-100): 88
Enter Biology score (0-100): 90

============================================================
        REPORT CARD - ALICE JOHNSON
============================================================
Math           :  92.00  (A+)
Physics        :  85.00  (A)
Chemistry      :  78.00  (B)
English        :  88.00  (A)
Biology        :  90.00  (A+)
------------------------------------------------------------
Total          : 433.00 / 500
Percentage     :  86.60%
Final Grade    : A
============================================================
```

---

## Version 2: Multiple Students with Statistics

### New Features
- Handle multiple students
- Class statistics (average, topper, etc.)
- Ranking system
- Detailed comparison

### Complete Code

```python
"""
Student Grading System - Version 2
Multiple students with statistics
"""

from statistics import mean, median, stdev

# Configuration
SUBJECTS = ["Math", "Physics", "Chemistry", "English", "Biology"]

GRADE_SCALE = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0, "F"),
]

def get_letter_grade(percentage):
    """Return letter grade for given percentage."""
    for cutoff, letter in GRADE_SCALE:
        if percentage >= cutoff:
            return letter
    return "F"

def get_subject_score(subject_name):
    """Get validated subject score."""
    while True:
        try:
            score = float(input(f"  {subject_name:12s} (0-100): "))
            if 0 <= score <= 100:
                return score
            print("    ❌ Score must be 0-100.")
        except ValueError:
            print("    ❌ Invalid input.")

def calculate_student_results(scores):
    """
    Calculate results for a student.
    
    Args:
        scores: Dictionary of {subject: score}
    
    Returns:
        dict: Results including total, percentage, grade
    """
    total = sum(scores.values())
    max_possible = len(scores) * 100
    percentage = (total / max_possible) * 100
    letter = get_letter_grade(percentage)
    
    return {
        'total': total,
        'max': max_possible,
        'percentage': percentage,
        'letter': letter
    }

def print_report_card(name, scores, results):
    """Print detailed report card for a student."""
    print("\n" + "=" * 70)
    print(f"  REPORT CARD - {name.upper()}")
    print("=" * 70)
    print(f"{'Subject':<15} {'Score':>10} {'Grade':>10}")
    print("-" * 70)
    
    for subject, score in scores.items():
        grade = get_letter_grade(score)
        print(f"{subject:<15} {score:10.2f} {grade:>10}")
    
    print("-" * 70)
    print(f"{'Total':<15} {results['total']:10.2f} / {results['max']}")
    print(f"{'Percentage':<15} {results['percentage']:10.2f}%")
    print(f"{'Final Grade':<15} {results['letter']:>10}")
    print("=" * 70)

def print_class_statistics(students):
    """Print comprehensive class statistics."""
    percentages = [s['results']['percentage'] for s in students]
    
    # Sort by percentage
    ranked = sorted(students, key=lambda x: x['results']['percentage'], reverse=True)
    
    print("\n" + "=" * 70)
    print("  CLASS STATISTICS")
    print("=" * 70)
    
    # Overall stats
    print(f"\nOverall Performance:")
    print(f"  Total Students    : {len(students)}")
    print(f"  Class Average     : {mean(percentages):.2f}%")
    print(f"  Median Score      : {median(percentages):.2f}%")
    
    if len(percentages) > 1:
        print(f"  Standard Deviation: {stdev(percentages):.2f}")
    
    print(f"  Highest Score     : {max(percentages):.2f}%")
    print(f"  Lowest Score      : {min(percentages):.2f}%")
    
    # Top 3 performers
    print(f"\n🏆 Top 3 Performers:")
    for i, student in enumerate(ranked[:3], 1):
        print(f"  {i}. {student['name']:<20} - {student['results']['percentage']:.2f}% ({student['results']['letter']})")
    
    # Grade distribution
    print(f"\n📊 Grade Distribution:")
    grade_counts = {}
    for student in students:
        grade = student['results']['letter']
        grade_counts[grade] = grade_counts.get(grade, 0) + 1
    
    for grade in ['A+', 'A', 'B', 'C', 'D', 'F']:
        count = grade_counts.get(grade, 0)
        if count > 0:
            bar = "█" * count
            print(f"  {grade:3s} : {bar} ({count})")
    
    # Subject-wise analysis
    print(f"\n📚 Subject-Wise Average:")
    for subject in SUBJECTS:
        subject_scores = [s['scores'][subject] for s in students]
        avg = mean(subject_scores)
        print(f"  {subject:<15}: {avg:6.2f}")
    
    print("=" * 70)

def main():
    """Main program with multiple students."""
    print("\n" + "=" * 70)
    print("         STUDENT GRADING SYSTEM - Multiple Students")
    print("=" * 70)
    
    # Get number of students
    while True:
        try:
            num_students = int(input("\nHow many students? "))
            if num_students > 0:
                break
            print("❌ Please enter a positive number.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
    
    # Collect data for all students
    students = []
    
    for i in range(1, num_students + 1):
        print(f"\n{'─' * 70}")
        print(f"  Student {i} of {num_students}")
        print('─' * 70)
        
        name = input("Name: ").strip()
        if not name:
            name = f"Student_{i}"
        
        print("Enter scores:")
        scores = {}
        for subject in SUBJECTS:
            scores[subject] = get_subject_score(subject)
        
        results = calculate_student_results(scores)
        
        students.append({
            'name': name,
            'scores': scores,
            'results': results
        })
    
    # Print individual report cards
    print("\n\n" + "█" * 70)
    print("  INDIVIDUAL REPORT CARDS")
    print("█" * 70)
    
    for student in students:
        print_report_card(student['name'], student['scores'], student['results'])
    
    # Print class statistics
    print_class_statistics(students)

if __name__ == "__main__":
    main()
```

---

## Version 3: Advanced with Weighted Subjects and GPA

### New Features
- Weighted subjects (core vs elective)
- GPA calculation (4.0 scale)
- Pass/fail validation (minimum per subject)
- Configurable grading profiles

### Complete Code

```python
"""
Student Grading System - Version 3
Weighted subjects, GPA, advanced features
"""

from statistics import mean
import json

# Configuration
SUBJECTS = {
    "Mathematics": {"weight": 0.25, "core": True},
    "Physics": {"weight": 0.20, "core": True},
    "Chemistry": {"weight": 0.20, "core": True},
    "English": {"weight": 0.20, "core": True},
    "Biology": {"weight": 0.15, "core": False},
}

# Validate weights sum to 1.0
total_weight = sum(s["weight"] for s in SUBJECTS.values())
assert abs(total_weight - 1.0) < 0.01, f"Weights must sum to 1.0 (currently {total_weight})"

GRADE_SCALE = [
    (90, "A+", 4.0),
    (85, "A", 3.7),
    (80, "A-", 3.3),
    (75, "B+", 3.0),
    (70, "B", 2.7),
    (65, "B-", 2.3),
    (60, "C+", 2.0),
    (55, "C", 1.7),
    (50, "C-", 1.3),
    (45, "D", 1.0),
    (0, "F", 0.0),
]

MINIMUM_PASSING_SCORE = 40  # Per subject minimum
MINIMUM_OVERALL = 50  # Overall percentage minimum

def get_grade_info(percentage):
    """
    Get letter grade and GPA for percentage.
    
    Returns:
        tuple: (letter, gpa)
    """
    for cutoff, letter, gpa in GRADE_SCALE:
        if percentage >= cutoff:
            return letter, gpa
    return "F", 0.0

def calculate_weighted_percentage(scores):
    """
    Calculate weighted percentage based on subject weights.
    
    Args:
        scores: Dictionary of {subject: score}
    
    Returns:
        float: Weighted percentage
    """
    weighted_sum = 0
    for subject, score in scores.items():
        weight = SUBJECTS[subject]["weight"]
        weighted_sum += score * weight
    return weighted_sum

def check_passing_status(scores, weighted_pct):
    """
    Check if student passes based on criteria.
    
    Args:
        scores: Dictionary of {subject: score}
        weighted_pct: Overall weighted percentage
    
    Returns:
        tuple: (passed: bool, failures: list)
    """
    failures = []
    
    # Check per-subject minimum
    for subject, score in scores.items():
        if score < MINIMUM_PASSING_SCORE:
            failures.append((subject, score))
    
    # Check overall minimum
    if weighted_pct < MINIMUM_OVERALL:
        failures.append(("Overall", weighted_pct))
    
    passed = len(failures) == 0
    return passed, failures

def calculate_cgpa(students):
    """
    Calculate Cumulative GPA for a student across multiple semesters.
    
    Args:
        students: List of student data (could represent semesters)
    
    Returns:
        float: CGPA
    """
    total_gpa = sum(s['results']['gpa'] for s in students)
    return total_gpa / len(students) if students else 0.0

def get_subject_score(subject_name):
    """Get validated subject score."""
    while True:
        try:
            score = float(input(f"  {subject_name:15s} (0-100): "))
            if 0 <= score <= 100:
                return score
            print("    ❌ Score must be 0-100.")
        except ValueError:
            print("    ❌ Invalid input.")

def print_detailed_report(student):
    """Print comprehensive report for a student."""
    name = student['name']
    scores = student['scores']
    results = student['results']
    
    print("\n" + "=" * 80)
    print(f"  DETAILED REPORT CARD - {name.upper()}")
    print("=" * 80)
    
    # Subject-wise details
    print(f"\n{'Subject':<15} {'Weight':>8} {'Score':>8} {'Grade':>8} {'GPA':>6} {'Type':>8}")
    print("-" * 80)
    
    for subject, score in scores.items():
        weight = SUBJECTS[subject]["weight"]
        grade, gpa = get_grade_info(score)
        subj_type = "Core" if SUBJECTS[subject]["core"] else "Elective"
        
        status = ""
        if score < MINIMUM_PASSING_SCORE:
            status = "  ❌ FAIL"
        
        print(f"{subject:<15} {weight*100:7.1f}% {score:8.2f} {grade:>8} {gpa:6.2f} {subj_type:>8} {status}")
    
    # Overall results
    print("-" * 80)
    print(f"{'Weighted Percentage':<15} : {results['weighted_pct']:6.2f}%")
    print(f"{'Final Grade':<15} : {results['letter']}")
    print(f"{'GPA (4.0 scale)':<15} : {results['gpa']:.2f}")
    
    # Pass/Fail status
    if results['passed']:
        print(f"{'Status':<15} : ✅ PASSED")
    else:
        print(f"{'Status':<15} : ❌ FAILED")
        print(f"\nFailed in:")
        for subject, score in results['failures']:
            print(f"  • {subject}: {score:.2f}")
    
    print("=" * 80)

def save_to_file(students, filename="grades_report.txt"):
    """Save results to text file."""
    with open(filename, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("  STUDENT GRADING SYSTEM - FINAL REPORT\n")
        f.write("=" * 80 + "\n\n")
        
        for student in students:
            f.write(f"\nStudent: {student['name']}\n")
            f.write(f"Weighted %: {student['results']['weighted_pct']:.2f}%\n")
            f.write(f"Grade: {student['results']['letter']}\n")
            f.write(f"GPA: {student['results']['gpa']:.2f}\n")
            f.write(f"Status: {'PASSED' if student['results']['passed'] else 'FAILED'}\n")
            f.write("-" * 80 + "\n")
    
    print(f"\n✅ Report saved to {filename}")

def main():
    """Advanced grading system main program."""
    print("\n" + "=" * 80)
    print("      ADVANCED STUDENT GRADING SYSTEM")
    print("      Weighted Subjects • GPA • Pass/Fail Criteria")
    print("=" * 80)
    
    print(f"\nGrading Configuration:")
    print(f"  • Minimum per subject: {MINIMUM_PASSING_SCORE}%")
    print(f"  • Minimum overall: {MINIMUM_OVERALL}%")
    print(f"  • GPA Scale: 4.0")
    
    # Get number of students
    while True:
        try:
            num_students = int(input("\nHow many students? "))
            if num_students > 0:
                break
            print("❌ Enter a positive number.")
        except ValueError:
            print("❌ Invalid input.")
    
    # Collect student data
    students = []
    
    for i in range(1, num_students + 1):
        print(f"\n{'─' * 80}")
        print(f"  Student {i} of {num_students}")
        print('─' * 80)
        
        name = input("Name: ").strip() or f"Student_{i}"
        
        print("Enter scores:")
        scores = {}
        for subject in SUBJECTS.keys():
            scores[subject] = get_subject_score(subject)
        
        # Calculate results
        weighted_pct = calculate_weighted_percentage(scores)
        letter, gpa = get_grade_info(weighted_pct)
        passed, failures = check_passing_status(scores, weighted_pct)
        
        students.append({
            'name': name,
            'scores': scores,
            'results': {
                'weighted_pct': weighted_pct,
                'letter': letter,
                'gpa': gpa,
                'passed': passed,
                'failures': failures
            }
        })
    
    # Display reports
    print("\n\n" + "█" * 80)
    print("  INDIVIDUAL REPORTS")
    print("█" * 80)
    
    for student in students:
        print_detailed_report(student)
    
    # Class statistics
    print("\n" + "=" * 80)
    print("  CLASS SUMMARY")
    print("=" * 80)
    
    passed_students = [s for s in students if s['results']['passed']]
    failed_students = [s for s in students if not s['results']['passed']]
    
    print(f"\nTotal Students: {len(students)}")
    print(f"Passed: {len(passed_students)} ({len(passed_students)/len(students)*100:.1f}%)")
    print(f"Failed: {len(failed_students)} ({len(failed_students)/len(students)*100:.1f}%)")
    
    if students:
        avg_gpa = mean(s['results']['gpa'] for s in students)
        avg_pct = mean(s['results']['weighted_pct'] for s in students)
        
        print(f"\nClass Average GPA: {avg_gpa:.2f}")
        print(f"Class Average %: {avg_pct:.2f}%")
        
        # Top performer
        topper = max(students, key=lambda x: x['results']['weighted_pct'])
        print(f"\n🏆 Top Performer: {topper['name']}")
        print(f"   Score: {topper['results']['weighted_pct']:.2f}%")
        print(f"   Grade: {topper['results']['letter']} (GPA: {topper['results']['gpa']:.2f})")
    
    # Save option
    save_choice = input("\n\nSave report to file? (y/n): ").strip().lower()
    if save_choice == 'y':
        save_to_file(students)
    
    print("\n✅ Grading complete!")

if __name__ == "__main__":
    main()
```

---

## Practice Exercises

### Basic Level

1. **Add More Subjects**: Extend the subject list with more courses.

2. **Custom Grading Scale**: Allow user to input custom grade boundaries.

3. **Subject Remarks**: Add comments like "Excellent", "Good", "Needs Improvement".

4. **Pass Percentage**: Calculate what percentage of students passed.

5. **Attendance Factor**: Include attendance in final calculation.

### Intermediate Level

6. **CSV Import**: Read student names and scores from CSV file.

7. **CSV Export**: Export results to CSV for Excel analysis.

8. **Subject-wise Topper**: Find top student in each subject.

9. **Progress Tracking**: Compare current grades with previous semester.

10. **Grade Improvement**: Calculate percentage improvement from last term.

### Advanced Level

11. **GUI Interface**: Create tkinter GUI with input forms and result display.

12. **Database Integration**: Store student data in SQLite database.

13. **Transcript Generation**: Generate PDF transcripts using reportlab.

14. **Predictive Analysis**: Predict final grades based on mid-term performance.

15. **Class Comparison**: Compare performance across multiple classes/sections.

---

## Key Takeaways

1. **Configuration Management**: Use dictionaries and constants for flexible grading policies.

2. **Input Validation**: Always validate user input to prevent errors.

3. **Data Structures**: Dictionaries and lists effectively organize student data.

4. **Statistical Analysis**: Use statistics module for mean, median, standard deviation.

5. **Weighted Averages**: Core subjects can carry more weight than electives.

6. **Pass/Fail Criteria**: Multiple criteria (per-subject and overall) ensure comprehensive evaluation.

7. **Reporting**: Clear, formatted output makes results easy to understand.

8. **File I/O**: Save results for record-keeping and further analysis.

---

## References

- **Python statistics module**: https://docs.python.org/3/library/statistics.html
- **CSV handling**: https://docs.python.org/3/library/csv.html
- **File I/O**: https://docs.python.org/3/tutorial/inputoutput.html
- **JSON configuration**: https://docs.python.org/3/library/json.html

---

**Next Steps**: Implement CSV import/export, create a GUI version, or integrate with a database for persistent storage!
