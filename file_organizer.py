import os
import shutil

# Folder path you want to organize
FOLDER_PATH = os.getcwd()

# File type mapping
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".js", ".sh"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Presentations": [".pptx", ".ppt"],
}

# Create folders if they don't exist
for folder in file_types:
    folder_path = os.path.join(FOLDER_PATH, folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files into folders
for filename in os.listdir(FOLDER_PATH):

    file_path = os.path.join(FOLDER_PATH, filename)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, file_extension = os.path.splitext(filename)

    for folder, extensions in file_types.items():

        if file_extension.lower() in extensions:

            destination_folder = os.path.join(FOLDER_PATH, folder)

            shutil.move(file_path, destination_folder)
            break

print(f"Files organized successfully in: {FOLDER_PATH}")
