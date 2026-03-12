# create nested directories
import os
os.makedirs("parent/child/grandchild", exist_ok=True)

# list files and folders
path = "."
items = os.listdir(path)
for item in items:
    print(item)

# find files by extension
search_path = "."
extension = ".txt"
for root, dirs, files in os.walk(search_path):
    for file in files:
        if file.endswith(extension):
            print(os.path.join(root, file))