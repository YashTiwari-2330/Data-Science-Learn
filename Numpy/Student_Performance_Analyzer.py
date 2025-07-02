import numpy as np

#STEP 1 LOAD DATA

data = np.genfromtxt("grades_dirty.csv" , delimiter="," , dtype=str , skip_header=1)


names = data[:,0]
score_raw = data[:,1]

#STEP 2 CONVERT SCORES TO FLOAT , USING NAN , NA
def clean_score(arr):
    cleaned = []
    max_len = 0

    # First pass: clean and convert each row
    for row in arr:
        new_row = []
        for val in row:
            try:
                num = float(val)
                if num < 0:  # invalid score
                    new_row.append(np.nan)
                else:
                    new_row.append(num)
            except:
                new_row.append(np.nan)
        cleaned.append(new_row)
        max_len = max(max_len, len(new_row))

    # Second pass: pad rows with np.nan to make them same length
    for i in range(len(cleaned)):
        while len(cleaned[i]) < max_len:
            cleaned[i].append(np.nan)

    for i, row in enumerate(cleaned):
        print(f"Row {i} length = {len(row)}")

    return np.array(cleaned)


scores = clean_score(score_raw)

# STEP 3 PRINT CLEANED SCORES
print("📊 Cleaned Score : \n" , scores)

# STEP 4 CALCULATE AVERAGE PER STUDENT , IGNORES NUN
student_avg = np.nanmean(scores , axis=1)
print("\n🎓 Average Score per Student:")
for name , avg in zip(names , student_avg):
    print(f"{name:8} → {avg:.2f}")

# Step 5: Calculate average per subject
subject_avg = np.nanmean(scores , axis=0)
subjects = ["Math", "English", "Science", "Gujrati", "Hindi"]
print("\n📚 Average Score per Subject:")
for sub , avg in zip(subjects , subject_avg):
    print(f"{sub:8}  →  {avg:.2f}")

# STEP 6: FIND TOP STUDENT
top_idx = np.nanargmax(student_avg)
print(f"\n🏆 Top Student: {names[top_idx]} with average {student_avg[top_idx]:.2f}")

# STEP 7 STUDENT WHO FAILED ANY EXAMS
fail_marks = scores < 40
fails_any = np.any(fail_marks , axis=1)
print("\n❌ Students who failed at least one subject:")
print(names[fails_any])

# STEP 8 BEST SUBJECT FOR EACH STUDENT
best_subject = np.nanargmax(scores , axis=1)
print("\n🥇 Best subject for each student:")
for i , sub_idx in enumerate(best_subject):
    print(f"{names[i]:8}  →  {subjects[sub_idx]}")

# STEP 9 Z-SCORE NORMALIZATION
mean = np.nanmean(scores)
std = np.nanstd(scores)
normalized_scores = (scores - mean) / std
print("\n⚖️ Z-score Normalized Scores:\n", normalized_scores.round(2))

# STEP 10 SAVE CLEANED SCORES TO A NEW CSV
np.savetxt("cleaned_scores.csv" , scores , delimiter=',' , fmt = "%.2f")
print("\n💾 Cleaned scores saved to 'cleaned_scores.csv'")
