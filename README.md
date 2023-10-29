# merge_markdown_files_by_subdirectory_name_python

## Markdown File Merging Program

### Created: 
29/10/2023

### Language:
Python

### Purpose: 
To merge the content from multiple markdown files into one markdown file

### Reason for Creation:
After using Obsidian for some time, I had generated a number of markdown files that were a bit disjointed.
To consolidate these files, I got the idea to create a program to merge the many markdown files into a more streamlined, reduced set of files

### Menu Options:
1. Create a directory in current working directory and to store merged files
2. Create a directory in custom directory and store merged files
3. Quit

### Program Flow (Each Loop):
1. User selects an option from the menu
2. Create a new folder where merged content will be stored
    i. One function allows for creating a new directory in the directory where the program file is run
    ii. Another function allows for creating a directory in a custom location on the local machine
3. Get the folder containing the content to be merged
4. Create a list of all the sub-directories contained in the directory
5. Create a list of all the sub-directory names (Used to create the new files)
6. Generate index via for loop (used for accessing elements in the sub-directory list and new file names list)
7. Generate a list of all the paths of files in the sub-directory
8. Create the new file where all the merged content will be writen too
9. Read each of the files in the sub-directory and write the content to the new file
10. Return to menu

### Limitations:
- Only created to handle markdown files.
- Not tested with any other file formats
