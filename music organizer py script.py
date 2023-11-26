import os
import shutil

def organize_music_files(folder_path):
    # Create folders if they don't exist
    wav_folder = os.path.join(folder_path, "wav files")
    mp3_folder = os.path.join(folder_path, "mp3 files")
    aiff_folder = os.path.join(folder_path, "aiff files")
    m4a_folder = os.path.join(folder_path, "m4a files")
    flac_folder = os.path.join(folder_path, "flac files")

    for folder in [wav_folder, mp3_folder, aiff_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Dictionary to track processed file names
    processed_files = set()

    # Iterate through all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            #checks if file name has been processed.
            if file in processed_files:
                continue

            # Check file extension and move to the corresponding folder
            if file.lower().endswith(".wav"):
                shutil.move(file_path, os.path.join(wav_folder, file))
                print(f"Moved {file} to 'wav files' folder.")
            elif file.lower().endswith(".mp3"):
                shutil.move(file_path, os.path.join(mp3_folder, file))
                print(f"Moved {file} to 'mp3 files' folder.")
            elif file.lower().endswith(".aiff"):
                shutil.move(file_path, os.path.join(aiff_folder, file))
                print(f"Moved {file} to 'aiff files' folder.")
            elif file.lower().endswith(".m4a"):
                shutil.move(file_path, os.path.join(m4a_folder, file))
                print(f"Moved {file} to 'm4a files' folder.")
            elif file.lower().endswith(".flac"):
                shutil.move(file_path, os.path.join(flac_folder, file))
                print(f"Moved {file} to 'flac files' folder.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")

    if os.path.exists(folder_path):
        organize_music_files(folder_path)
        print("Music files organized successfully.")
    else:
        print("Invalid folder path. Please check and try again.")
