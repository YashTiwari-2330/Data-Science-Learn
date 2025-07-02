import numpy as np

# 1️⃣ Generate synthetic student scores
np.random.seed(42)
num_students = 100

math_scores = np.random.randint(50, 100, size=num_students)
science_scores = np.random.randint(40, 95, size=num_students)
english_scores = np.random.randint(45, 90, size=num_students)

# Combine scores: shape (100, 3)
scores = np.vstack((math_scores, science_scores, english_scores)).T
subjects = ['Math', 'Science', 'English']

# 2️⃣ Basic Stats: Mean, Std, Total, Rank
mean_scores = np.mean(scores, axis=0)
std_scores = np.std(scores, axis=0)
total_scores = np.sum(scores, axis=1)
ranks = total_scores.argsort()[::-1] + 1  # Higher score = higher rank

print("✅ Mean scores:", dict(zip(subjects, mean_scores)))
print("✅ Std deviation:", dict(zip(subjects, std_scores)))
print("✅ Top 5 Total Scores:", total_scores[:5])
print("✅ Top 5 Ranks:", ranks[:5])

# 3️⃣ Normalize the data
scores_norm = (scores - mean_scores) / std_scores
print("\n✅ Normalized scores (first 3 rows):\n", scores_norm[:3])

# 4️⃣ Add Missing Values (simulate)
scores_missing = scores.copy()
scores_missing[::10, 1] = np.nan  # Every 10th student missing Science score

# 6️⃣ Predict Total Score using Science + English (Linear Regression)

# Features (X): Science & English
X = scores_missing[:, 1:3]
# Add bias column
X_b = np.hstack((np.ones((num_students, 1)), X))

# Target (y): Total score
y = total_scores

# Normal Equation: θ = (XᵀX)^(-1)Xᵀy
theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y

# Predict
y_pred = X_b @ theta

# Compare predictions
print("\n✅ Predicted total scores (first 5):\n", y_pred[:5])
print("✅ Actual total scores (first 5):\n", total_scores[:5])
