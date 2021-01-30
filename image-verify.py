'''
TO DO:
Taking in input (which will be classes x y h w)
Check if there are same number of objects
Check that class is in predefined_classes.txt
***Sort by class number
Check that bounding box pixel values are less than 3 pixels apart


Written by: Eric, Rosy, Francine
'''
DIFFERENCE = 3

#getting the input
box_file1 = open("box1.txt", "r")
box_file2 = open("box2.txt", "r")
box1 = [x.strip('\n') for x in box_file1.readlines()]
box2 = [x.strip('\n') for x in box_file2.readlines()]
# print(len(box1))
# print(len(box2))


def difference(coordinates1, coordinates2, difference):
  for i in range(2): # just compare x y of coordinates
    point1 = coordinates1[i]
    point2 = coordinates2[i]
    x_difference = abs(point1[0] - point2[0])
    y_difference = abs(point1[1] - point2[1])
    if x_difference >= difference or y_difference >= difference:
        return False
  return True

# get two files
box_file1 = open("box1.txt", "r")
box_file2 = open("box2.txt", "r")

# make each line in the file an element in the array
box1 = [x.strip('\n') for x in box_file1.readlines()]
box2 = [x.strip('\n') for x in box_file2.readlines()]

#print check
print(box1)
print(len(box1))
print(box1[0][0])
# print(box2)
# print(len(box2)) 

# check the lengths are equal, effectively making sure they have the same number of boxes
if(len(box1) == len(box2)):
    # for each box in the array box1
    for i in range(len(box1)): # we need to sort first
        # split strings into lists
        i1list = box1[i].split(" ")
        i2list = box2[i].split(" ")
        if i1list[0] == i2list[0]: #check if the classes are the same first
            # 
            x1 = float(i1list[1])
            y1 = float(i1list[2])
            w1 = float(i1list[3])
            h1 = float(i1list[4])
            topleft1 = (x1 - w1/2, y1 + h1/2)
            # topright1 = (x1 + w1/2, y1 + h1/2)
            # botleft1 = (x1 - w1/2, y1 - h1/2)
            botright1 = (x1 + w1/2, y1 - h1/2)
            coordinates1 = list(topleft1, botright1)

            x2 = i2list[1]
            y2 = i2list[2]
            w2 = i2list[3]
            h2 = i2list[4]
            topleft2 = (x2-w2/2, y2+h2/2)
            # topright2 = (x2+w2/2, y2+h2/2)
            # botleft2 = (x2-w2/2, y2-h2/2)
            botright2 = (x2+w2/2, y2-h2/2)
            coordinates2 = list(topleft2, botright2)
            result = difference(coordinates1, coordinates2, DIFFERENCE)
            if result == True:
                print("All good")
            else:
                print("hmm we need a third opinion")
        else:
            print("we need a third opinion. Class difference in classification ", i)
            print(box1[0], box2[0])
else:
    print('we need a third opinion. There are different number of objects')


































































































































