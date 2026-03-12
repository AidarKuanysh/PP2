# move/copy files between directories
import shutil
source_file = "source/example.txt"
destination_directory = "destination/"

# copy file
shutil.copy(source_file, destination_directory)

# move file
shutil.move(source_file, destination_directory)