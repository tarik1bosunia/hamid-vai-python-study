## 🎓 Day 11: Mini Project — Student Grading System

Build a small console app that:

* Accepts **scores** for multiple subjects (0–100)
* Calculates **total, average, percentage**
* Assigns **letter grade** from a configurable scale
* (Optional) Computes **GPA** and **class position stats**

---

### 📏 Grading Scale (Editable)

You can tweak these thresholds easily in code.

| Letter | Min % |
| :----: | :---: |
|   A+   |   90  |
|    A   |   80  |
|    B   |   70  |
|    C   |   60  |
|    D   |   50  |
|    F   |  < 50 |

> 💡 Tip: Store the scale in a list of tuples so you can change it without editing logic.

---

## 1) Simple Version (Single Student, Fixed Subjects)

```python
# --- Config ---
SUBJECTS = ["Math", "Physics", "Chemistry", "English", "Biology"]
GRADE_SCALE = [
    (90, "A+"),
    (80, "A"),
    (70, "B"),
    (60, "C"),
    (50, "D"),
    (0,  "F"),
]

# --- Helpers ---
def get_letter_grade(percent: float) -> str:
    for cutoff, letter in GRADE_SCALE:
        if percent >= cutoff:
            return letter
    return "F"

# --- Main ---
print("\n=== Student Grading System (Simple) ===")
scores = {}
for subject in SUBJECTS:
    while True:
        try:
            val = float(input(f"Enter {subject} score (0-100): "))
            if 0 <= val <= 100:
                scores[subject] = val
                break
            else:
                print("Score must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid number. Try again.")

total = sum(scores.values())
percentage = total / (len(SUBJECTS) * 100) * 100
letter = get_letter_grade(percentage)

print("\n--- Report Card ---")
for subj, val in scores.items():
    print(f"{subj:<12}: {val:6.2f}")
print(f"Total       : {total:6.2f} / {len(SUBJECTS)*100}")
print(f"Percentage  : {percentage:6.2f}%")
print(f"Grade       : {letter}")
```

**Sample Run**

```
=== Student Grading System (Simple) ===
Enter Math score (0-100): 92
Enter Physics score (0-100): 85
Enter Chemistry score (0-100): 78
Enter English score (0-100): 88
Enter Biology score (0-100): 90

--- Report Card ---
Math        :  92.00
Physics     :  85.00
Chemistry   :  78.00
English     :  88.00
Biology     :  90.00
Total       : 433.00 / 500
Percentage  :  86.60%
Grade       : A
```

---

## 2) Advanced Version (Weighted Subjects, GPA, Multiple Students)

Features:

* **Weights** per subject (e.g., core vs elective)
* **Multiple students** input
* **Per-subject validation**
* **GPA mapping** from letter grade

```python
from statistics import mean

# --- Config ---
SUBJECTS = {
    "Math": 0.25,
    "Physics": 0.20,
    "Chemistry": 0.20,
    "English": 0.20,
    "Biology": 0.15,
}
assert abs(sum(SUBJECTS.values()) - 1.0) < 1e-9, "Weights must sum to 1.0"

GRADE_SCALE = [
    (90, "A+", 4.0),
    (80, "A",  3.7),
    (70, "B",  3.0),
    (60, "C",  2.0),
    (50, "D",  1.0),
    (0,  "F",  0.0),
]

# --- Helpers ---
def letter_and_gpa(percent: float):
    for cutoff, letter, gpa in GRADE_SCALE:
        if percent >= cutoff:
            return letter, gpa
    return "F", 0.0

# --- Input ---
print("\n=== Student Grading System (Advanced) ===")
while True:
    try:
        n = int(input("How many students? "))
        if n > 0:
            break
        print("Enter a positive integer.")
    except ValueError:
        print("Invalid number. Try again.")

students = []
for i in range(1, n + 1):
    print(f"\n-- Student {i} --")
    name = input("Name: ").strip() or f"Student_{i}"
    marks = {}
    for subj in SUBJECTS:
        while True:
            try:
                val = float(input(f"  {subj} (0-100): "))
                if 0 <= val <= 100:
                    marks[subj] = val
                    break
                else:
                    print("  Score must be 0-100.")
            except ValueError:
                print("  Invalid number.")

    # Weighted percentage
    weighted_pct = sum(marks[s] * SUBJECTS[s] for s in SUBJECTS)
    letter, gpa = letter_and_gpa(weighted_pct)

    students.append({
        "name": name,
        "marks": marks,
        "weighted_pct": weighted_pct,
        "letter": letter,
        "gpa": gpa,
    })

# --- Output ---
print("\n========= Results =========")
for s in students:
    print(f"\n{name:=^28}")
    print(f"{s['name']}")
    print("Subject-wise:")
    for subj, val in s["marks"].items():
        print(f"  {subj:<10}: {val:6.2f}")
    print(f"Weighted % : {s['weighted_pct']:.2f}%")
    print(f"Letter     : {s['letter']}")
    print(f"GPA        : {s['gpa']:.2f}")

# Class stats
class_avg = mean(s["weighted_pct"] for s in students)
best = max(students, key=lambda x: x["weighted_pct"])
worst = min(students, key=lambda x: x["weighted_pct"])

print("\n===== Class Statistics =====")
print(f"Class Average % : {class_avg:.2f}%")
print(f"Topper         : {best['name']} ({best['weighted_pct']:.2f}%)")
print(f"Needs Support  : {worst['name']} ({worst['weighted_pct']:.2f}%)")
```

> 🧪 Try changing weights (e.g., give Math more weight) and see how the final grades shift.

---

## 3) Extras & Extensions

* **Pass/Fail rule:** require at least 40% in **each subject** in addition to overall percentage.
* **CSV I/O:** read students and marks from a CSV, write results to another CSV.
* **Grading policy profiles:** store multiple scales (e.g., Strict, Lenient) and choose at runtime.
* **Letter per subject:** also compute letter grades for each subject individually.

---

## 4) Utility: Percent ↔ GPA Converter

```python
GRADE_SCALE = [
    (90, "A+", 4.0),
    (80, "A",  3.7),
    (70, "B",  3.0),
    (60, "C",  2.0),
    (50, "D",  1.0),
    (0,  "F",  0.0),
]

def percent_to_gpa(p):
    for cutoff, letter, gpa in GRADE_SCALE:
        if p >= cutoff:
            return letter, gpa
    return "F", 0.0

# Demo
for p in [95, 83, 71, 64, 52, 41]:
    letter, gpa = percent_to_gpa(p)
    print(f"{p}% -> {letter} ({gpa})")
```

---

### ✅ Concepts Covered

* Input validation and error handling
* Data structures: lists, dicts, tuples
* Aggregations: sum, mean, min/max
* Reusable configuration (scales, weights)

> 🎯 **Takeaway:** With small abstractions (scale, weights), this tiny app becomes flexible enough for many grading policies. Ready for a GUI next (e.g., `tkinter`)?
