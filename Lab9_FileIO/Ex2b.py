import os
import stat

file_path = '/Users/lanceabut/Downloads/survey_1000.csv'

if os.path.exists(file_path):
    if os.access(file_path, os.R_OK):
        file_stats = os.stat(file_path)

        print(f"File: {file_path}")
        print(f"Size: {file_stats.st_size} bytes")
        print(f"Permissions: {stat.filemode(file_stats.st_mode)}")
        print(f"Last modified: {file_stats.st_mtime}")
    else:
        print(f"The file '{file_path}' exists but is not readable.")
else:
    print(f"The file '{file_path}' does not exist.")