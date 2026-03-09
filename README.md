# Smart File Organizer

A simple Python tool that automatically organizes files in a directory based on their file extensions.

The script scans a folder, detects file types, and moves them into categorized folders such as **Images, Videos, Documents, Audio, Code, Archives**, and more. This helps keep directories like **Downloads, project folders, or working directories clean and structured**.

---

## Features

* Scans a directory and detects files
* Categorizes files based on their extensions
* Automatically creates folders for each category
* Moves files into the appropriate folder
* Places unknown file types into an **Others** folder
* Skips directories while scanning
* Cleans previously organized `Others` folder when the script is run again

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

1. Open `main.py`.

2. Set the directory you want to organize:

```python
directory = "path/to/your/folder"
```

3. Run the script:

```
python main.py
```

The script will automatically scan the folder and organize all files.

---