'''
count counts the number of files of a given type inside of a directory and all of its subdirectory
    
'''
import os
def count(directory, file_type):
    all_files = os.listdir(directory)
    if all_files == []:
        return 0
    else:
        return sum(list(map(lambda x: diverse_counting(directory, x, file_type), all_files)))

'''
diverse_count is a helper function for count and 
    it counts the number of files of a given type 
    inside a directory and all of its subdirectories.
input: directory is a string reprenting the starting directory
        file is a string that represents the file or subdirectory name
            Ex: fish.txt
                folder
                image.jpg
        file_type is a string that represents the file ending without the dot
            Ex: txt
                jpg
output: if the file is a subdirectory, then it returns the number of files in that directory
        if the file is of the right type, then it returns 1
        if the file is not of the right type, then it returns 0
'''
def diverse_counting(directory, file, file_type):
    if os.path.isdir(os.path.join(directory, file)):
        return count(os.path.join(directory, file), file_type)
    elif file.split(".")[-1] == file_type:
        return 1
    else:
        return 0