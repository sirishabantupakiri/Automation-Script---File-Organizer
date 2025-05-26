import os
import shutil
import logging
from datetime import datetime

# --- CONFIGURATION ---

# Define file type categories
FILE_CATEGORIES = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv'],
    'Others': []
}

# Setup logging
LOG_FILE = "file_organizer.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- CORE FUNCTIONS ---

def get_category(extension: str) -> str:
    """Returns the file category based on its extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def organize_files(directory: str) -> None:
    """Organizes files in the given directory into categorized subfolders."""
    if not os.path.isdir(directory):
        print(f"❌ Error: '{directory}' is not a valid directory.")
        logging.error(f"Invalid directory: {directory}")
        return

    print(f"\n📁 Organizing files in: {directory}\n")
    logging.info(f"Started organizing: {directory}")

    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    try:
                        file_name = entry.name
                        file_path = entry.path
                        _, extension = os.path.splitext(file_name)
                        category = get_category(extension)
                        category_folder = os.path.join(directory, category)

                        # Create category folder if it doesn't exist
                        os.makedirs(category_folder, exist_ok=True)

                        target_path = os.path.join(category_folder, file_name)

                        # Avoid moving if already in correct folder
                        if os.path.abspath(file_path) != os.path.abspath(target_path):
                            shutil.move(file_path, target_path)
                            print(f"✅ Moved: {file_name} → {category}/")
                            logging.info(f"Moved '{file_name}' to '{category}'")
                        else:
                            logging.info(f"Skipped '{file_name}' (already in correct folder)")
                    except Exception as e:
                        print(f"⚠️ Error moving file '{entry.name}': {e}")
                        logging.error(f"Error moving file '{entry.name}': {e}")
    except Exception as e:
        print(f"❌ Critical error: {e}")
        logging.critical(f"Critical error in organizing files: {e}")

    print("\n🎉 Organization complete.")
    logging.info("File organization finished.\n")

# --- SCRIPT ENTRY POINT ---

if __name__ == "__main__":
    print("🔄 File Organizer Script")
    print("------------------------")
    folder_path = input("Enter the full path of the folder to organize: ").strip()
    organize_files(folder_path)



