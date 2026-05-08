import os
import re

dir_path = "/media/azaz/D/AntigravityData/DSA_Exam/Jenny'sLecturesYT_Notes/"

# Get all markdown files
files = [f for f in os.listdir(dir_path) if f.endswith(".md")]

# Regex to find prefix like "1.1_", "2.10_", "6.13_"
pattern = re.compile(r'^(\d+\.\d+_)(.*)')

groups = {}
for f in files:
    match = pattern.match(f)
    if match:
        prefix = match.group(1)
        if prefix not in groups:
            groups[prefix] = []
        groups[prefix].append(f)

for prefix, file_list in groups.items():
    if len(file_list) > 1:
        # Sort files by modification time (newest first)
        file_list_paths = [os.path.join(dir_path, f) for f in file_list]
        file_list_paths.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        
        newest = file_list_paths[0]
        # All others are considered old
        for old_file in file_list_paths[1:]:
            # We want to replace the old file with the newest one's content, 
            # so the old filename is kept, OR we delete the old file.
            # The user complained about creating new files instead of replacing the old. 
            # This implies they wanted the OLD filenames to be reused.
            print(f"Old file to replace: {os.path.basename(old_file)}")
            print(f"Newest file: {os.path.basename(newest)}")
            
            # Read newest content
            with open(newest, "r") as nf:
                content = nf.read()
            
            # Write to old file
            with open(old_file, "w") as of:
                of.write(content)
                
            # Delete newest file since it's a new name we shouldn't have created
            os.remove(newest)
            print(f"Deleted {os.path.basename(newest)} and updated {os.path.basename(old_file)}\n")

