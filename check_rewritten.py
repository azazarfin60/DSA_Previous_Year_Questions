import os
import re

dir_path = "/media/azaz/D/AntigravityData/DSA_Exam/Jenny'sLecturesYT_Notes/"

files = [f for f in os.listdir(dir_path) if f.endswith(".md")]

unprocessed = []

for f in files:
    if f in ['00_index.md', 'README.md']:
        continue
    
    filepath = os.path.join(dir_path, f)
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        
    # Check if the file has typical markdown headings
    if "## " not in content:
        unprocessed.append(f)

print(f"Found {len(unprocessed)} files that might not be rewritten (no '## ' heading):")
for f in unprocessed:
    print(f" - {f}")

