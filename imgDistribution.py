# inputs: folder with all the images, list of names that will label the images 
# has one folder of images that it splits so everyone has a folder of images
# nest folders so they're still in the larger folder

# importing os module 
import os, os.path, shutil


def get_names(file):
    """ 
    Input: text file with names
    Generates a list of names, gathered from a text file
    Output: list of names
    """
    name_file = open(file, "r")
    list_of_names = []
    for line in name_file:
        stripped_line = str(line.strip())
        line_string = stripped_line.split()
        list_of_names +=line_string
    name_file.close()
    return list_of_names


def pair_people(names):
    """ 
    Input: a list of unpaired names
    Output: a list, where each element is a pair of names of the form "name1-name2"
    If the number of names is odd, pair_people will append 'Other' to the final name
    """
    pair_names = []
    if (len(names) % 2) == 1:
        names += ['Other']

    if len(names) > 2:
        pair_names += [names[0] + '-' + names[1]] + pair_people(names[2:])
      
    else:
        if (len(names) % 2) == 0:
            pair_names += [names[0] + '-' + names[1]]
   
    return pair_names

    

def rename_images(pair_names, parent_dir):
    """
    Inputs: a list of pairsand a directory with images
    Outputs: the same directory, but with renamed images
    rename_images cycles through the images stored in the directory and 
    assigns them evenly among the provided pairs, using the naming convention
    "name1-name2_#.jpg"
    """
    images = os.listdir(parent_dir)
    if '.DS_Store' in images:
        images.remove('.DS_Store')
    numPairs = len(pair_names)
    for x in range(len(images)):
        whichPair = x % numPairs
        os.rename(parent_dir +'/'+ images[x], parent_dir + '/' + pair_names[whichPair] + '_' + str(x) + '.jpg')
    return images
    

def move_images(parent_dir):
    """ creates new folders in the parent_dir and moves images into the folders
        image names need to be name_number
        folder names are name
    """
    images = [f for f in os.listdir(parent_dir) if os.path.isfile(os.path.join(parent_dir, f))]

    for image in images:
        folder_name = image.split('_')[0]

        new_path = os.path.join(parent_dir, folder_name)
        if not os.path.exists(new_path):
            os.makedirs(new_path)

        old_image_path = os.path.join(parent_dir, image)
        new_image_path = os.path.join(new_path, image)
        shutil.move(old_image_path, new_image_path)

    folders = [folder for folder in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, folder))]

    for folder in folders:
        name1 = folder.split('-')[0]
        name2 = folder.split('-')[1]
        folder_path = os.path.join(parent_dir, folder)
        name1_path = os.path.join(folder_path, name1)
        os.makedirs(name1_path)
        name2_path = os.path.join(folder_path, name2)
        os.makedirs(name2_path)


def main(names_file = 'names.txt', parent_dir = '/home/cvteam1/imageLabeling/compData/'):
    """ Inputs: txt file with peoples' names, directory of images to be sorted (parent_dir should contain only images)
        Gets names from file
        Creates pairs (format: name1-name2) 
        Renames images (format: name1-name2_0.jpg)
        Moves images to folders named name1-name2
        Output: none
    """
    names = get_names(names_file)
    pairs = pair_people(names)
    rename_images(pairs, parent_dir)
    move_images(parent_dir)

def admin_rename_images(names, parent_dir):
    """
    Inputs: a list of names and a directory with images
    Outputs: the same directory, but with renamed images
    rename_images cycles through the images stored in the directory and 
    assigns them evenly among the provided names, using the naming convention
    "admin_name'name1-name2_#.jpg"
    """
    images = os.listdir(parent_dir)
    if '.DS_Store' in images:
        images.remove('.DS_Store')
    numNames = len(names)
    for x in range(len(images)):
        whichName = x % numNames
        os.rename(parent_dir +'/'+ images[x], parent_dir + '/' + names[whichName] + "'" + images[x])
    return images

def admin_move_images(parent_dir):
    """ creates new folders in the parent_dir and moves images into the folders
    """
    images = [f for f in os.listdir(parent_dir) if os.path.isfile(os.path.join(parent_dir, f))]

    for image in images:
        folder_name = image.split("'")[0]

        new_path = os.path.join(parent_dir, folder_name)
        if not os.path.exists(new_path):
            os.makedirs(new_path)

        old_image_path = os.path.join(parent_dir, image)
        new_image_path = os.path.join(new_path, image)
        shutil.move(old_image_path, new_image_path)

    folders = [folder for folder in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, folder))]

    for folder in folders:
        folder_path = os.path.join(parent_dir, folder)
        text_path = os.path.join(folder_path, folder)
        os.makedirs(text_path) 
    
def admin_distribution(admin_file = 'admin_names.txt', parent_dir = '/home/cvteam1/imageLabeling/compData/admin/'):
    """
    distributes images within the admin folder
    """
    admin_names = get_names(admin_file)
    admin_rename_images(admin_names, parent_dir)
    admin_move_images(parent_dir)