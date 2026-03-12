# copy and back up files using shutil
import shutil

shutil.copy("example.txt", "example_backup.txt")


# delete files safely
import os

backup_file = "example_backup.txt"
if os.path.exists(backup_file):
    os.remove(backup_file)
    print(f"{backup_file} deleted successfully.")
else:
    print(f"{backup_file} does not exist.")