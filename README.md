# Automation-Script---File-Organizer

The File Sorter Utility is a Python-based tool designed to streamline file management by automatically sorting files in a chosen directory into categorized subfolders based on their extensions. It organizes files into groups like Documents, Images, Videos, and Others, with detailed logging for transparency.

## Key Features

- Scans a user-specified directory for files.
- Groups files by their extensions into predefined categories.
- Creates subfolders automatically as needed (e.g., Documents, Images, Videos, Others).
- Relocates files to their respective category folders.
- Maintains a tidy directory structure.
- Logs all actions to a file for tracking and debugging.

## Technologies Used

- **Python 3.13.3**
- Standard Built-in modules:
  - `os` : For file and directory operations.
  - `shutil` : For moving files.
  - `logging`: For recording script activities

## Supported Files Types & Extensions

| Category  | File Extensions                          |
|-----------|------------------------------------------|
| Documents | `.pdf`, `.docx`, `.txt`, `.pptx`, `.xls` |
| Images    | `.jpg`, `.jpeg`, `.png`, `.gif`          |
| Videos    | `.mp4`, `.avi`, `.mov`, `.mkv`           |
| Others    | Any other file types not listed above    |

##  How to Use

**Setup and Usage**
**Prerequisites**
    - Python 3.6+ installed (download from python.org).
    - Basic familiarity with running scripts in a terminal or command prompt.
    - Read and write permissions for the target directory.

**Installation**
    - Download the Script:

**Clone the repository or download the script directly:**
     - git clone https://github.com/yourusername/file-sorter-utility.git
     - cd file-sorter-utility
     - Alternatively, save file_organizer.py to a local directory (e.g., C:\Scripts).

**Verify Python Installation:**
       - Run python --version in a terminal to confirm Python is installed and accessible.

**Running the Script**
       - Open a terminal (e.g., Command Prompt, PowerShell, or VS Code integrated terminal).
       - Navigate to the script’s directory:
       - cd path/to/your/script
            - Example: cd C:\Scripts
       - Execute the script:
            - python file_organizer.py
            - When prompted, enter the full path of the directory to organize (e.g., C:\Users\YourName\Downloads or /home/user/downloads).
       - The script will:
            - Scan the directory.
            - Create category folders if they don’t exist.
            - Move files to their respective folders.
            - Log all actions to file_organizer.log.


   
