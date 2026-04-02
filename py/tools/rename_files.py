import os
import sys

def rename_files(directory, old_str, new_str):
    if not os.path.isdir(directory):
        print(f'Error: "{directory}" does not exist!')
        return

    for filename in os.listdir(directory):
        if old_str in filename:
            new_name = filename.replace(old_str, new_str)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f'renamed: {filename} -> {new_name}')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python rename_files.py directory old_str new_str')
    else:
        rename_files(sys.argv[1], sys.argv[2], sys.argv[3])