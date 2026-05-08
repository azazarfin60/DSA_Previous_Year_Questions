import os

dir_path = "/media/azaz/D/AntigravityData/DSA_Exam/Jenny'sLecturesYT_Notes/"
files = [f for f in os.listdir(dir_path) if f.endswith(".md")]

unprocessed = []

for f in files:
    filepath = os.path.join(dir_path, f)
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()
        
    # Check if any line is longer than 1500 characters
    has_long_line = any(len(line) > 1500 for line in lines)
    if has_long_line:
        unprocessed.append(f)

if unprocessed:
    print(f"Found {len(unprocessed)} files with very long lines (possibly raw transcripts):")
    for f in unprocessed:
        print(f" - {f}")
else:
    print("No files with excessively long lines found.")

