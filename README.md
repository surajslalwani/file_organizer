# Smart File Organizer

A Python CLI tool that automatically organizes files in a directory based on their file extensions.

It scans a folder, detects file types, and moves them into categorized folders such as **Images, Videos, Documents, Audio, Code, Archives**, and more — keeping directories like **Downloads or project folders clean and structured.**

---

## Features

* Scans a directory and detects files
* Categorizes files based on their extensions
* Automatically creates folders for each category
* Moves files into the appropriate folder
* Places unknown file types into an **Others** folder
* Skips directories while scanning
* Cleans previously organized `Others` folder when the script is run again 
* Handles duplicate filenames safely (no overwrites)
* Command-line interface (CLI)
* Dry Run mode to preview changes without modifying files


---

## Project Structure

```
file_organizer/
│
├── main.py
├── README.md
│
└── example_folder/
```

`example_folder` is included only to demonstrate how the organizer works.

---

## Example

### Before

```
example_folder/
    photo.png
    music.mp3
    report.pdf
    script.py
    archive.zip
```

### After running the script

```
example_folder/
    Images/
        photo.png
    Audio/
        music.mp3
    Documents/
        report.pdf
    Code/
        script.py
    Archives/
        archive.zip
```

Files with unknown extensions will be moved to:

```
Others/
```

---

## Usage

1. Open Termianl.

2. Basic Command:

```Terminal
python main.py organize <directory_path>
```

3. Dry Run Mode (Preview Only):

```
python main.py organize ./example_folder --dry-run
```

Output example:

```
[DRY RUN] photo.png → Images/
[DRY RUN] music.mp3 → Audio/
```

---

## Notes
Existing files with the same name will not be overwritten
→ They will be renamed automatically like:

```
file(1).jpg, file(2).jpg, ...
```

Dry run mode does not create folders or move files


The script will automatically scan the folder and organize all files.

---