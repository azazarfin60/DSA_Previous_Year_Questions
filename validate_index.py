import os
import re

index_file = "/media/azaz/D/AntigravityData/DSA_Exam/Jenny'sLecturesYT_Notes/00_index.md"
dir_path = "/media/azaz/D/AntigravityData/DSA_Exam/Jenny'sLecturesYT_Notes/"

with open(index_file, "r") as f:
    content = f.read()

# Extract links: [text](filename.md)
pattern = re.compile(r'\[.*?\]\((.*?\.md)\)')
links = pattern.findall(content)

missing = []
for link in links:
    if not os.path.exists(os.path.join(dir_path, link)):
        missing.append(link)

if missing:
    print(f"Found {len(missing)} broken links:")
    for m in missing:
        print(f" - {m}")
else:
    print("All links in 00_index.md are valid and point to existing files!")
