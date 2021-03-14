import os
import shutil
def remove_file(path, number_of_files, number_of_files_removed):
    if  os.path.exists(path):
        number_of_files += 1
        val = input("Do you wish to remove " + path + "? Y for yes n for no.")
        if(val == "Y"):
            os.remove(path)
            number_of_files_removed +=1
            print(path + " has been removed.")
    return number_of_files, number_of_files_removed
def remove_folder(path, number_of_files, number_of_files_removed):
    if os.path.exists(path):
        number_of_files += 1
        val = input("Do you wish to remove " + path + "? Y for yes n for no.")
        if(val == "Y"):
            shutil.rmtree(path)
            number_of_files_removed +=1
            print(path + " has been removed.")
    return number_of_files, number_of_files_removed
if __name__ == "__main__":
    number_of_files = 0
    number_of_files_removed = 0
    number_of_files, number_of_files_removed = remove_folder("./output/images/", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove_folder("./output/labels/", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove_folder("./compData/failed_labeler1/", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove_folder("./compData/failed_labeler2/", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove_file("failed_verification.txt", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove_file("passed_verification.txt", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove_file("admin_failed_verification.txt", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove_file("admin_passed_verification.txt", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove_file("admin_verified_text_files.txt", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove_file("verified_text_files.txt", number_of_files, number_of_files_removed)
    print("number of files found: ", number_of_files)
    print("number of files removed: ", number_of_files_removed)