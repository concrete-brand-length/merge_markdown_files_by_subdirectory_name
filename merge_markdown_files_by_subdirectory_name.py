'''
Markdown File Merging Program

Created: 
29/10/2023

Language: 
Python

Purpose: 
To merge the content from multiple markdown files into one markdown file

Reason for Creation:
After using Obsidian for some time, I had generated a number of markdown files that were a bit disjointed.
To consolidate these files, I got the idea to create a program to merge the many markdown files into a more streamlined, reduced set of files


Menu Options:
1. Create a directory in current working directory and to store merged files
2. Create a directory in custom directory and store merged files
3. Quit

Program Flow (Each Loop):
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

Limitations:
- Only created to handle markdown files.
- Not tested with any other file formats
'''


import os
from itertools import chain


''' 
For creating a directory at the path wherethe python file is being run

@return - The file path of the new directory
'''
def create_directory_in_current_directory():
    while True:
        user_choice = input("Create a new diretory (y or n)> ")
        if user_choice in ["y", "Y"]:
            user_input = input("New Directory Name> ")
            directory_path = f"{os.getcwd()}\\{user_input}"
            if os.path.exists(directory_path) == False:
                os.mkdir(directory_path)
            return directory_path
        elif user_choice in ["n", "N"]:
            return os.getcwd()
        else:
            print("Input invalid. Try again!")


''' 
For creating a directory at a location specified by the user 

@return - The file path of the new directory
'''
def create_directory_in_custom_directory(path):
    while True:
        user_choice = input("Create a new diretory (y or n)> ")
        if user_choice in ["y", "Y"]:
            user_input = input("New Directory Name> ")
            directory_path = f"{path}\\{user_input}"
            if os.path.exists(directory_path) == False:
                os.mkdir(directory_path)
            return directory_path
        elif user_choice in ["n", "N"]:
            return path
        else:
            print("Input invalid. Try again!")


''' 
Creates a new file

@return - The file path of the new file
''' 
def create_new_file(path, new_file_name):
    file_path = f"{path}\\{new_file_name}.md"
    with open(file_path, 'w') as file:
        pass
    return file_path


''' 
Generates a list of all the subdirectories in the directory path passed

@return - A list containing sub-diretory paths
'''
def generate_subdirectory_path_list(path):
    folder_paths = [x[0] for x in os.walk(path)]
    return folder_paths[1:]
    

'''
Generates a list of file names contained in the directory passed

@return - A list containing file names in all sub-directories
'''
def generate_new_file_names_(path):
    file_names = [x[1] for x in os.walk(path)]
    return list(chain.from_iterable(file_names))


'''
Generates a list of file paths contained in a directory
'''
def generate_subdirectory_file_path_list(directory_path):
    return [f"{directory_path}\\{file}" for file in os.listdir(directory_path) if os.path.isfile(f"{directory_path}\\{file}")]
    

''' 
Merges the content of files in list parameter containing file paths, into a single file that is passed as a parameter
'''
def merge_files(new_file_path, file_path_list):
    write_file = open(new_file_path, "a")
   
    if len(file_path_list) > 0:
        for file_path in file_path_list:
            if file_path not in [".DS_Store"]: # Files to omit
                with open(file_path, 'r') as read_file:
                    write_file.write(read_file.read())
    write_file.close()


'''
Checks if the path parameter passed exists

@return - True if exists
@return - False if does not exist
'''
def is_valid_path(path):
    return os.path.exists(path)


'''
Gets input from the user for a path

Iterates until user enters a valid path or they enter q to quit

@return - a validated path
'''
def get_valid_path(message):
    while True:
        user_input = input(message)
        if is_valid_path(user_input):
            return user_input
        if (user_input == "q"):
            quit()
        print("That path does not exist. Try entering another path!")


'''
Contains all the function calls when the user wants to create a folder from where the Python file is run from
'''
def menu_option1():
    new_directory_path = create_directory_in_current_directory()
    path_of_files_to_merge = get_valid_path("Directory Full Path - Files to Merge> ")
    sub_directory_paths = generate_subdirectory_path_list(path_of_files_to_merge)
    new_file_names_list = generate_new_file_names_(path_of_files_to_merge)
    for index in range(len(sub_directory_paths)):
        sub_directory_file_path_list = generate_subdirectory_file_path_list(sub_directory_paths[index])
        new_file_path = create_new_file(new_directory_path, new_file_names_list[index])
        merge_files(new_file_path, sub_directory_file_path_list)
    print("Merge Complete")


'''
Contains all the function calls when the user wants to create a folder at a custom path
'''
def menu_option2():
    custom_path = get_valid_path("Directory Full Path - Local Directory to Use> ")
    new_directory_path = create_directory_in_custom_directory(custom_path)
    path_of_files_to_merge = get_valid_path("Enter the path to the directory containing the files to be merged")
    sub_dictory_paths = generate_subdirectory_path_list(path_of_files_to_merge)
    new_file_names_list = generate_new_file_names_(path_of_files_to_merge)
    for index in range(len(sub_dictory_paths)):
        sub_directory_file_path_list = generate_subdirectory_file_path_list(sub_dictory_paths[index])
        new_file_path = create_new_file(new_directory_path, new_file_names_list[index])
        merge_files(new_file_path, sub_directory_file_path_list)
    print("Merge Complete")



'''
For printing the program's menu to the user
'''
def print_menu():
    menu_options = [f"1. Create a directory in '{os.getcwd()}' and merge files", 
                    "2. Create a directory in custom directory and merge files", 
                    "3. Quit"]
    print("\nMenu Options: ")
    for option in menu_options:
        print(f"\t- {option}")


'''
Runs the program

Progam loops until user enters 3 to quit
'''
def program_loop():
    print("\nFile Merging Program")
    while True:
        print_menu()
        menu_choice = input("Option Choice (1 ,2, 3)> ")
        if menu_choice == "1":
            print()
            menu_option1()
        elif menu_choice == "2":
            print()
            menu_option2()
        elif menu_choice == "3":
            quit()
        else:
            print("That was an incorrect choice. Please try again!\n")

       
if __name__ == "__main__":
    program_loop()
