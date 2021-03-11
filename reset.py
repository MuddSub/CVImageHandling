import os

def remove(path, number_of_files, number_of_files_removed):
    if  os.path.exists(path):
        number_of_files += 1
        val = input("Do you wish to remove " + path + "? Y for yes n for no.")
        if(val == "Y"):
            os.remove(path)
            number_of_files_removed +=1
            print(path + " has been removed.")
    return number_of_files, number_of_files_removed

if __name__ == "__main__":
    number_of_files = 0
    number_of_files_removed = 0
    number_of_files, number_of_files_removed = remove("./output/images/", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove("./output/labels/", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove("./compData/failed_labeler1/", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove("./compData/failed_labeler2/", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove("failed_verification.txt", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove("passed_verification.txt", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove("admin_failed_verification.txt", number_of_files, number_of_files_removed)
    number_of_files, number_of_files_removed = remove("admin_passed_verification.txt", number_of_files, number_of_files_removed)
    print("number of files found: ", number_of_files)
    print("number of files removed: ", number_of_files_removed)