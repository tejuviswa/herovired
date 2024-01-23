import os
import shutil
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description="Backup files from a source directory to a destination directory.")
    parser.add_argument("source_dir", type=str, help="The source directory to back up.")
    parser.add_argument("destination_dir", type=str, help="The destination directory for the backup.")
    args = parser.parse_args()

    source_dir = args.source_dir
    destination_dir = args.destination_dir

    try:
        if not os.path.exists(source_dir):
            raise ValueError(f"Source directory not found: {source_dir}")
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)  # Create destination directory if it doesn't exist

        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)

            if os.path.exists(destination_file):
                timestamp = time.strftime("%Y%m%d-%H%M%S")  # Generate timestamp
                destination_file = f"{os.path.splitext(destination_file)[0]}_{timestamp}{os.path.splitext(destination_file)[1]}"

            shutil.copy2(source_file, destination_file)  # Copy file, preserving metadata
            print(f"Copied {filename} to {destination_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
