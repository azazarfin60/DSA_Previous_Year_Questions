import re

task_file = "/home/azaz/.gemini/antigravity/brain/2068779f-8a4b-4fc2-9e33-f3e71eb8484b/task.md"
with open(task_file, "r") as f:
    lines = f.readlines()

video_count = 0
for line in lines:
    line = line.strip()
    # Check if the line is a task item and starts with a section number like 1.1, 5.10, etc.
    if line.startswith("- [x]") or line.startswith("- [ ]") or line.startswith("- [/]"):
        # Extract the text after the checkbox
        text = line[5:].strip()
        # Look for a number pattern like 1.1, 2.10, etc.
        if re.match(r'^\d+\.\d+', text):
            video_count += 1

print(f"Total video items found in task.md: {video_count}")
