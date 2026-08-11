import re

with open("README.md", "r") as f:
    content = f.read()

applied = len(re.findall(r"🟡", content))
assessment = len(re.findall(r"🔵", content))
interview = len(re.findall(r"🟣", content))

print("=== Internship Application Stats ===")
print(f"Applied: {applied}")
print(f"Online Assessments: {assessment}")
print(f"Interviews: {interview}")
