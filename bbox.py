'''
TO DO:
Taking in input (which will be classes x y h w)
Check if there are same number of objects
Check that class is in predefined_classes.txt
***Sort by class number
Check that bounding box pixel values are less than 3 pixels apart


Written by: Eric, Rosy, Francine
'''
import os
import time
from averageText import *
from count import *
class image_labels:
    def __init__(self, file_name):
        self.file_name = file_name
        self.box_file = open(file_name, "r")
        self.box_list = sorted([x.strip('\n') for x in self.box_file.readlines()])
        self.length = len(self.box_list)
        self.DIFFERENCE = 3
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
        | between the coordinates are smaller than 3.
        |
        | Input:   self
        |          image2: another instance of the image_labels class
        | Output:  If the number of boxes are the same and the coordinate differences is smaller than 3, return True; 
        |          If not, return False
        """
        # check the lengths are equal, effectively making sure they have the same number of boxes
        if self.length == image2.length:

            # for each box in the list box_list


            for i in range(self.length): # iterating thru the boxes in the files
                
                # split strings into lists
                i1list = self.box_list[i].split(" ")
                i2list = image2.box_list[i].split(" ")
                
                if i1list[0] == i2list[0]: #check if the classes are the same first
                    if(i1list == '' and i2list == ''):
                        return True
                    elif(i1list == '' and i2list != '') or (i2list == '' and i1list != ''):
                        return False
                    coordinates1 = self.coordinates(i1list)
                    coordinates2 = self.coordinates(i2list)
                    print("coordinates1: ", coordinates1)
                    print("coordinates2: ", coordinates2)
                    
                    result = self.difference(coordinates1, coordinates2)

                    if result == False:
                        return False
                else:
                    return False
            return True
        else:
            return False

def verify(labeled_files1, labeled_files2, verified_text_files, basepath, labelers):
    for bbox_file2 in labeled_files2:
        if bbox_file2 in verified_text_files:
            continue
        for bbox_file1 in labeled_files1:
            if bbox_file2 == bbox_file1:
                file2 = basepath + labelers[1] + "/" + bbox_file2
                file1 = basepath + labelers[0] + "/" + bbox_file1
                print("file being checked rn is: ", file2)
                box2 = image_labels(file2)
                box1 = image_labels(file1)
                if box1.verify_labels(box2) == True:
                    print("passed verification")
                    passed = open("passed_verification.txt", "a")
                    print("passed ", file1, " ", file2, file = passed)
                    passed.close()
                    average_files(file1, file2, "./output/labels/")
                    os.replace(basepath + bbox_file1[:-4] + '.jpg', "./output/images/" +bbox_file1[:-4]+'.jpg')
                else:
                    print("failed verification")
                    failed = open("failed_verification.txt", "a")
                    print("failed ", file1, " ", file2, file = failed)
                    failed.close()
                    os.replace(basepath + bbox_file1[:-4] + '.jpg', "./compData/admin/" +bbox_file1[:-4]+'.jpg')
                verified_text_files.append(bbox_file1)

def start_verifying(basepath, verified_text_files=[]):
    print('Verification started')
    print('Basepath is ', basepath)
    group_names = [name for name in os.listdir(basepath) if os.path.isdir(os.path.join(basepath, name))]
    if('admin' in group_names):
        group_names.remove('admin')
    else:
        os.makedirs(basepath + "admin/")
    while(True):
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