'''
TO DO:
Taking in input (which will be classes x y h w)
Check if there are same number of objects
Check that class is in predefined_classes.txt
***Sort by class number
Check that bounding box pixel values are less than 3 pixels apart


Written by: Eric, Rosy, Francine
'''

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