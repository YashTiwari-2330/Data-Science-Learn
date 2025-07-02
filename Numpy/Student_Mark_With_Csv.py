import numpy as np
import csv


def load_and_clean_grades(file_path):
    names = []
    raw_grades = []

    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)  # skip header
        for row in reader:
            names.append(row[0])
            grades = []
            for val in row[1:]:
                try:
                    score = float(val)
                    # Handle outliers
                    if score < 0 or score > 100:
                        grades.append(np.nan)
                    else:
                        grades.append(score)
                except:
                    grades.append(np.nan)  # handle '', 'N/A', etc.
            raw_grades.append(grades)

    grades_array = np.array(raw_grades, dtype=np.float64)

    # Fill missing values with column-wise mean
    col_means = np.nanmean(grades_array, axis=0)
    inds = np.where(np.isnan(grades_array))
    grades_array[inds] = np.take(col_means, inds[1])

    return names, headers[1:], grades_array


# Load and clean
names, subjects, grades = load_and_clean_grades("grades_dirty.csv")

# Stats
student_avg = np.mean(grades, axis=1)
subject_avg = np.mean(grades, axis=0)
overall_avg = np.mean(grades)

# Reporting
print("Subjects:", subjects)
print("\nPer-subject average:")
for subj, avg in zip(subjects, subject_avg):
    print(f"{subj}: {avg:.2f}")

print("\nPer-student average:")
for name, avg in zip(names, student_avg):
    print(f"{name}: {avg:.2f}")

print("\nStudents below overall average:")
for name, avg in zip(names, student_avg):
    if avg < overall_avg:
        print(f"{name} ({avg:.2f})")

# Optional: Normalization
normalized = (grades - np.min(grades, axis=0)) / (np.max(grades, axis=0) - np.min(grades, axis=0))
