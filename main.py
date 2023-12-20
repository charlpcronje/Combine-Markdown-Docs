import os
import json
import sys

def load_exclusions(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def should_exclude(path, exclusions):
    for exclusion in exclusions:
        if path.startswith(exclusion):
            return True
    return False

def get_relative_path(root, file_path):
    return os.path.relpath(file_path, root)

def combine_markdown_files(root_dir, output_file, exclusions):
    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(root_dir):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d), exclusions['folders'])]
            
            for file in files:
                if file.endswith('.md') and not should_exclude(os.path.join(root, file), exclusions['files']):
                    file_path = os.path.join(root, file)
                    relative_path = get_relative_path(root_dir, file_path)
                    outfile.write(f"\n\n**File:** [{relative_path}]({relative_path})\n\n")
                    with open(file_path, 'r') as infile:
                        outfile.write(infile.read() + '\n\n')

def main():
    # Use the provided directory path or default to the current directory
    root_directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    output_md_file = os.path.join(root_directory, 'PROJECT DOCS.md')

    # Load exclusions from the JSON file
    exclusions_file = os.path.join(root_directory, 'projectDocs.json')
    exclusions = load_exclusions(exclusions_file)

    # Combine the markdown files
    combine_markdown_files(root_directory, output_md_file, exclusions)

if __name__ == "__main__":
    main()
