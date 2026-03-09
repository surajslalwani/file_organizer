import os
import shutil
import argparse




def get_folder_name(ext_list, ext):
    for key, value in ext_list.items():
        if ext in value:
            return key
    return None



directory = "C:/Users/dell/Documents/GitHub/File Organizer/test_folder"

extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".tif", ".webp", ".svg", ".heic", ".heif", ".ico", ".raw", ".psd", ".ai", ".eps"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".3gp", ".3g2", ".m4v", ".ts", ".vob"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".pages"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".numbers"],
    "Presentations": [".ppt", ".pptx", ".odp", ".key"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a", ".wma", ".aiff", ".alac", ".amr", ".mid", ".midi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".cab"],
    "Executables": [".exe", ".msi", ".bat", ".cmd", ".sh", ".bin", ".app", ".apk"],
    "Code": [".py", ".cpp", ".c", ".h", ".hpp", ".java", ".js", ".ts", ".html", ".css", ".php", ".go", ".rs", ".swift", ".kt", ".m", ".mm", ".scala", ".lua", ".dart", ".r", ".pl"],
    "Data": [".json", ".xml", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".db", ".sqlite", ".sql"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "3D": [".obj", ".fbx", ".stl", ".blend", ".3ds", ".dae"],
    "Disk_Images": [".iso", ".img", ".dmg"],
    "Torrents": [".torrent"]
}


for folder in os.listdir(directory):
    path = os.path.join(directory, folder)
    if not os.path.isfile(path):
        if(folder == "Others"):
            for file in os.listdir(path):
                file_path = os.path.join(path, file)
                dir_path = os.path.join(directory, file)
                shutil.move(file_path, dir_path)


all_ext = set()
for v in extensions.values():
    for e in v: 
        all_ext.add(e)


for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()

        if ext in all_ext:
            folder_name = get_folder_name(extensions, ext)
            folder_path = os.path.join(directory, folder_name)

            os.makedirs(folder_path, exist_ok=True)
            final_path = os.path.join(folder_path, filename)

            shutil.move(file_path, final_path)
            print("Moved", filename, "to", folder_name)
        else:
            folder_name = "Others"
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            final_path = os.path.join(folder_path, filename)
            shutil.move(file_path, final_path)
            print("Moved", filename, "to", folder_name)
    else:
        print("Skipped", filename, "is a directory")

print("Files Organized...!")