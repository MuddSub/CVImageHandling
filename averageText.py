def get_values(file):
    values = open(file, 'r')
    values = sorted([x.strip('\n') for x in values.readlines()])
    values = [x.split() for x in values]
    values = list(map(lambda bbox: [float(x) for x in bbox], values))
    return values

'''takes two lists repesenting one bounding box in yolo format and average the coordinates but ignores the class'''
def average(L1, L2):
    averaged_list = [L1[0]]
    for i in [1,2,3,4]:
        averaged_list.append((L1[i] + L2[i]) / 2)
    return averaged_list


def average_files(file1, file2, output_folder):
    values1 = get_values(file1)
    values2 = get_values(file2)
    average_values = []

    for i in range(len(values1)):
        average_values += average(values1[i], values2[i])

    file_name = find_file_name(file1)
    average_txt = open(output_folder + file_name, "w")
    s1 = ''
    for i in range(len(average_values)):
        if((i+1)%5 == 1):
            s1 = s1 + str(int(average_values[i])) #the class number is always an int
        else:
            s1 = s1 + str(average_values[i])
        if((i+1)%5 == 0 and i != len(average_values)-1):
            s1 = s1[:-1] + '\n\n' #idk why but its super buggy, it will only skip a line with two new lines
        else:
            s1 = s1 + '  '
        s1 = s1[:-1] #to get rid of extra space at the end
    average_txt.write(s1[:-1])
    average_txt.close()
    return average_values

def find_file_name(file1):
    return file1.split("/")[-1]