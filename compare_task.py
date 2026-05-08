import os
import re

task_file = "/home/azaz/.gemini/antigravity/brain/2068779f-8a4b-4fc2-9e33-f3e71eb8484b/task.md"
dir_path = "/media/azaz/D/AntigravityData/DSA_Exam/Jenny'sLecturesYT_Notes/"

with open(task_file, "r") as f:
    task_content = f.read()

# Extract numbers like 1.1, 5.10 from task.md
task_numbers = set(re.findall(r'- \[[x ]\] (\d+\.\d+)', task_content))

files = [f for f in os.listdir(dir_path) if f.endswith(".md")]
file_numbers = set()
for f in files:
    match = re.match(r'^(\d+\.\d+)_', f)
    if match:
        file_numbers.add(match.group(1))

missing_in_task = file_numbers - task_numbers
print(f"Total numbered files in directory: {len(file_numbers)}")
print(f"Total numbered tasks in task.md: {len(task_numbers)}")
print(f"Missing from task.md: {sorted(list(missing_in_task))}")

# Are there any files without numbers?
un_numbered = [f for f in files if not re.match(r'^(\d+\.\d+)_', f) and f not in ['00_index.md', 'README.md']]
print(f"Un-numbered files: {un_numbered}")

