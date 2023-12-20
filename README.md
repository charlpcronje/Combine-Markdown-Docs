
# Combine Project Markdown Docs 

## Overview
This Python application recursively scans a specified directory and its sub-directories for Markdown (`.md`) files and combines them into a single file named `PROJECT DOCS.md`. It also allows users to exclude specific files or folders from the combination process through a configuration file named `projectDocs.json`.

## Features
- **Recursive File Scanning**: Scans all sub-directories for `.md` files.
- **Exclusion Configuration**: Exclude specific files and folders using `projectDocs.json`.
- **Custom Headers**: Adds a header with the relative path to each Markdown file in `PROJECT DOCS.md`.

## Installation
1. Ensure Python is installed on your system.
2. Clone or download this repository to your local machine.
3. Navigate to the directory containing the script.

## Usage
1. Modify the `root_directory` variable in the script to point to your target directory containing the Markdown files.
2. Ensure `projectDocs.json` is in the same directory as the script or update its path in the script.
3. Run the script with Python:

```bash
python combine_markdown.py
```

4. The combined Markdown content will be available in `PROJECT DOCS.md` in the same directory.

## Configuration (`projectDocs.json`)
Create a `projectDocs.json` file in the same directory as the script with the following structure:

```json
{
    "files": ["path/to/excluded/file.md", "another/path/to/exclude.md"],
    "folders": ["path/to/excluded/folder", "another/excluded/folder"]
}
```

- `files`: Array of file paths to exclude from the combining process.
- `folders`: Array of folder paths to exclude from the combining process.

Paths should be relative to the `root_directory`.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](link-to-your-issues-page) if you want to contribute.

## License
[MIT](link-to-your-license-file)

## Contact
Charl Cronje
Email: charl.cronje@mail.com
Project Link: [https://github.com/charlpcronje/Combine-Markdown-Docs.git](https://github.com/charlpcronje/Combine-Markdown-Docs.git)
