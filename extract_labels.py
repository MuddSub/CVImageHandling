import os
#assumes starting directory is ~/imageLabeling

def extract_from(path):
    """
        Outputs a list with the names of all files (text files and another formats) in a specific directory.
        Does not find the names of files in the subdirectories.
    """
    #getting user input for the right path
    val = input("Do you wish to record text files from " + path + "? Y for yes n for no.")
    if(val == "Y"):
        return os.listdir(path)
    else:
        custom_path = input("Which directory do you want to record text files from?")
        return os.listdir(custom_path)

def extract_to_txt(records_path, output_labels):
    """
        prints each element of output_labels on seperated lines to a text_file called records_path
    """
    #getting user input for the right records_path
    val = input("Do you wish to record text files to " + records_path + "? Y for yes n for no.")
    if(val == "Y"):
        verified_text_files = open("./verified_text_files_m.txt", "w")
    else:
        custom_path = input("Which file do you want to record text files to?")
        verified_text_files = open(custom_path, "w")
    #printing to records_path
    for label in output_labels:
        print(label, file = verified_text_files)
    verified_text_files.close()

if __name__ == "__main__":
    print("When inputing paths or names, DO NOT put quotes (' ') !")
    output_labels = extract_from("./output/labels")
    extract_to_txt("./verified_text_files_m.txt", output_labels)