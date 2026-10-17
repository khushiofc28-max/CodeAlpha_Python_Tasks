import os
import shutil

def organize_images():
    # Folder paths define karein
    source_folder = "source_folder"
    destination_folder = "images_folder"

    # Folders automatically create karein agar exist nahi karte
    if not os.path.exists(source_folder):
        os.makedirs(source_folder)
        # Testing ke liye sample dummy files bana lete hain
        with open(os.path.join(source_folder, "photo1.jpg"), "w") as f:
            f.write("sample image data")
        with open(os.path.join(source_folder, "photo2.jpg"), "w") as f:
            f.write("sample image data")
        with open(os.path.join(source_folder, "notes.txt"), "w") as f:
            f.write("sample text notes")
        print(f"[SETUP] Created '{source_folder}' with test files.")

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"[SETUP] Created '{destination_folder}'.")

    # Files scan aur move karne ka logic
    files = os.listdir(source_folder)
    moved_count = 0

    print("\n--- Moving .jpg Files ---")
    for file_name in files:
        # Check karein agar file .jpg extension wali hai
        if file_name.lower().endswith(".jpg"):
            src_path = os.path.join(source_folder, file_name)
            dest_path = os.path.join(destination_folder, file_name)

            shutil.move(src_path, dest_path)
            print(f"Moved: {file_name} -> {destination_folder}/")
            moved_count += 1

    print("-------------------------")
    print(f"Automation Complete! Total {moved_count} image(s) moved successfully.")

if __name__ == "__main__":
    organize_images()