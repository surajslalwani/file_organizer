import os
import shutil
import argparse



def get_folder_name(ext_list, ext):
    for key, value in ext_list.items():
        if ext in value:
            return key
    return None



def if_file_exists(name, ext, folder_path):
    count = 1
    final_path = os.path.join(folder_path, f"{name}{ext}")
    while os.path.exists(final_path):
        new_name = f"{name}({count}){ext}"
        final_path = os.path.join(folder_path, new_name)
        count += 1
    return final_path

def organize_files(directory, dry_run):
    #Gives a set of all extensions written in the 'extensions' dictionary, Used to move files with unknown extensions to 'Others' Folder
    all_ext = set()
    for v in extensions.values():
        for e in v: 
            all_ext.add(e)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            name, ext = os.path.splitext(filename)
            ext = ext.lower()

            if ext in all_ext:
                folder_name = get_folder_name(extensions, ext)
                folder_path = os.path.join(directory, folder_name)
                final_path = if_file_exists(name, ext, folder_path)
                if dry_run:
                    print("[DRY RUN] Moved", filename, "to", folder_name)
                else:
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, final_path)
                    print("Moved", filename, "to", folder_name)
            else:
                folder_name = "Others"
                folder_path = os.path.join(directory, folder_name)
                final_path = if_file_exists(name, ext, folder_path)
                if dry_run:
                    print("[DRY RUN] Moved", filename, "to", folder_name)
                else:
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, final_path)
                    print("Moved", filename, "to", folder_name)
        else:
            if dry_run:
                print("[DRY RUN] Skipped", filename, "is a directory")
            else:
                print("Skipped", filename, "is a directory")



# Moves all the files in Others Folder into the directory for reorganizing
def clean_others(directory, dry_run):
    for folder in os.listdir(directory):
        path = os.path.join(directory, folder)
        if not os.path.isfile(path):
            if(folder == "Others"):
                for file in os.listdir(path):
                    file_path = os.path.join(path, file)
                    dir_path = os.path.join(directory, file)
                    if dry_run:
                        print("[DRY RUN] Moved", file, "from Other Folder to Directory")
                    else:
                        shutil.move(file_path, dir_path)
                        print("Moved", file, "from Other Folder to Directory")



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



parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command', help='Available Commands', required=True)

parser_org = subparser.add_parser('organize', help='Enter Path of the directory')

parser_org.add_argument('directory', type=str, help="Path of The directory")
parser_org.add_argument('-dr', '--dry-run', help="Dry run, just a preview", action='store_true')


args = parser.parse_args()






if args.command == 'organize':
    clean_others(args.directory, args.dry_run)
    organize_files(args.directory, args.dry_run)

print("Files Organized...!")
input("Press Enter to Exit")