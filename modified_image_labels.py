'''
Written by: Eric, Rosy, Francine
'''
import os
import time
import shutil
from averageText import *
from count import *
from sortList import *
class image_labels_m:
    def __init__(self, file_name):
        self.file_name = file_name
        self.box_file = open(file_name, "r")
        self.box_list = sorted([x.strip('\n') for x in self.box_file.readlines()])
        self.box_list = sortList(self.box_list)
        print(self.box_list)
        self.length = len(self.box_list)
        self.DIFFERENCE = 6
        self.IMGWIDTH = 640
        self.IMGHEIGHT = 480
    
    def difference(self, coordinates1, coordinates2):
        """
        | Checks if the difference between two bounding boxes are greater than a set difference limit.
        |
        | Inputs:   self
        |           coordinates1: a list of lists in the format [[left_x, top_y], [right_x, bottom_y]]
        |           coordinates2: a list of lists in the format [[left_x, top_y], [right_x, bottom_y]]
        | Output:   a boolean indicating if any of the coordinate pairs are >= DIFFERENCE apart
        """
        for i in range(2): # just compare x y of coordinates
            point1 = coordinates1[i]
            point2 = coordinates2[i]
            x_difference = abs(point1[0] - point2[0])
            y_difference = abs(point1[1] - point2[1])
            if x_difference >= self.DIFFERENCE or y_difference >= self.DIFFERENCE:
                return False
        return True

    def coordinates(self, coordslist):
        x = float(coordslist[1])
        y = float(coordslist[2])
        w = float(coordslist[3])
        h = float(coordslist[4])
                    
        topleft = ((x - w/2) * self.IMGWIDTH, (y + h/2) * self.IMGHEIGHT)
        botright = ((x + w/2) * self.IMGWIDTH, (y - h/2) * self.IMGHEIGHT) 
        coordinates = [topleft, botright]
        return coordinates

    def verify_labels(self, image2):
        """
        | Check if the number of boxes in the images equal, if so continue to verify if the difference 
        | between the coordinates are smaller than 6.
        | Does not care if classes match. only cares about location of the bounding boxes.
        |
        | Input:   self
        |          image2: another instance of the image_labels_m class
        | Output:  If the number of boxes are the same and the coordinate differences is smaller than 6, return True; 
        |          If not, return False
        """
        # check the lengths are equal, effectively making sure they have the same number of boxes
        if self.length == image2.length:

            # for each box in the list box_list


            for i in range(self.length): # iterating thru the boxes in the files
                
                # split strings into lists
                i1list = self.box_list[i].split(" ")
                i2list = image2.box_list[i].split(" ")
                
                #doesn't check if the classes are the same first
                if(i1list == '' and i2list == ''):
                    return True
                elif(i1list == '' and i2list != '') or (i2list == '' and i1list != ''):
                    return False
                coordinates1 = self.coordinates(i1list)
                coordinates2 = self.coordinates(i2list)
                print(i1list[0] , "coordinates1: ", coordinates1)
                print(i2list[0], "coordinates2: ", coordinates2)
                
                result = self.difference(coordinates1, coordinates2)

                if result == False:
                    print("result false")
                    return False
            return True
        else:
            print("other false")
            return False

def verify(labeled_files1, labeled_files2, verified_text_files, basepath, labelers):
    """
        compares matching text files from two directories, each represented by one labeled_files
        this is the more lenient version that does not care about class names, just location

        if two matching text files pass verification, the average of their text files will go to ./output_m/labels/
                                                    the image they are associated will be copied to ./output_m/images/
        if two matching text files fail verification, one text file will be copied to ./compData/failed_labeler1 and the other will be copied to ./compData/failed_labeler2
                                                    the image they are associated with will be copied to ./compData/admin
                                                    the image they are associated with will go to ./output_m/images/
                                                    a record of the two file names will be added to failed_verification_m.txt

        inputs:
            labeled_files1: a list containing the all the text file names of one labeler, like the contents of ./compData/erchen-halu/erchen/
            labeled_files2: a list containing the all the text file names of other labeler, like the contents of ./compData/erchen-halu/halu/
            verified_text_files: a list of all previously verified text file names so we don't repeat
            basepath: the directory that contains all labeler pairs, generally speaking will be ./compData
            labelers: a list containing the names of the two labelers, like [erchen, halu]
    """
    for bbox_file2 in labeled_files2:
        if bbox_file2 in verified_text_files:
            continue
        for bbox_file1 in labeled_files1:
            if bbox_file2 == bbox_file1:
                file2 = basepath + labelers[1] + "/" + bbox_file2
                file1 = basepath + labelers[0] + "/" + bbox_file1
                print("file being checked rn is: ", file2)
                box2 = image_labels_m(file2)
                box1 = image_labels_m(file1)
                if box1.verify_labels(box2) == True:
                    print("passed verification")
                    passed = open("passed_verification_m.txt", "a")
                    print("passed ", file1, " ", file2, file = passed)
                    passed.close()
                    average_files(file1, file2, "./output_m/labels/")
                    shutil.copy(basepath + bbox_file1[:-4] + '.jpg', "./output_m/images/" +bbox_file1[:-4]+'.jpg')
                else:
                    print("failed verification")
                    failed = open("failed_verification_m.txt", "a")
                    print("failed ", file1, " ", file2, file = failed)
                    failed.close()
                    shutil.copy(basepath + bbox_file1[:-4] + '.jpg', "./compData/admin/" +bbox_file1[:-4]+'.jpg')
                    shutil.copy(basepath + labelers[1] + "/" + bbox_file2, "./compData/failed_labeler2/" + bbox_file2)
                    shutil.copy(basepath + labelers[0] + "/" + bbox_file1, "./compData/failed_labeler1/" + bbox_file1)
                verified_text_files.append(bbox_file1)
                verification_records = open('./verified_text_files_m.txt', 'a')
                print(bbox_file1, file = verification_records)
                verification_records.close()

def start_verifying(basepath, verified_text_files=[]):
    """
        ASSUMES THAT THERE ARE NO IMAGES IN ADMIN AT THE START.

        loops through all the subdirectories until all text files are checked (i.e. number of text files pairs checked 
        equals the number of images intital images.)
        checks in 10 second intervals

        input: 
            basepath: the directory that contains all labeler pairs, generally speaking will be ./compData
            verified_text_files: a list of all previously verified text file names so we don't repeat
                                    this list is obtained from verified_text_files_m.txt
    """
    print('Verification started')
    print('Basepath is ', basepath)
    group_names = [name for name in os.listdir(basepath) if os.path.isdir(os.path.join(basepath, name))]
    if('admin' in group_names):
        group_names.remove('admin')
    else:
        os.makedirs(basepath + "admin/")
    if('failed_labeler1' in group_names):
        group_names.remove('failed_labeler1')
    if('failed_labeler2' in group_names):
        group_names.remove('failed_labeler2')
    total_images = count("./compData/", "jpg") #this will double count same images if there are already images in the admin folder when you run this file
    while(len(verified_text_files)< total_images + 1):
        time.sleep(10)
        for group in group_names:
            print("curently checking", group)
            new_basepath = basepath +group+"/"
            labelers = [ name for name in os.listdir(new_basepath) if os.path.isdir(os.path.join(new_basepath, name))]
            if(len(labelers) == 2):
                labeled_files1 = os.listdir(new_basepath + labelers[0]+"/")
                labeled_files2 = os.listdir(new_basepath + labelers[1]+"/")
                if(len(labeled_files1)>0 and len(labeled_files2)>0):
                    if(len(labeled_files1)<=len(labeled_files2)):
                        verify(labeled_files1, labeled_files2, verified_text_files, new_basepath, labelers)
                    else:
                        verify(labeled_files2, labeled_files1, verified_text_files, new_basepath, labelers)

if __name__ == "__main__":
    if (os.path.exists("./verified_text_files_m.txt")):
        verification_records = open('./verified_text_files_m.txt', 'r')
        verified_text_files = verification_records.readlines()
        verified_text_files = [x.strip("\n") for x in verified_text_files]
        verified_text_files.apend('bookmark.txt')
    else:
        verified_text_files = ['bookmark.txt']
    basepath = "./compData/"
    if not os.path.exists("./output_m/"):
        os.makedirs("./output_m/")
    if not os.path.exists("./output_m/images/"):
        os.makedirs("./output_m/images")
    if not os.path.exists("./output_m/labels/"):
        os.makedirs("./output_m/labels/")
    if not os.path.exists("./compData/failed_labeler1/"):
        os.makedirs("./compData/failed_labeler1/")
    if not os.path.exists("./compData/failed_labeler2/"):
        os.makedirs("./compData/failed_labeler2/")
    start_verifying(basepath, verified_text_files)