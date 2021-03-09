from image_labels import *

def admin_verify():
    admin_labelers = [name for name in os.listdir("./compData/admin/") if os.path.isdir(os.path.join("./compData/admin/", name))]
    if('unused_images' in admin_labelers):
        admin_labelers.remove('unused_images')
    for labeler in admin_labelers:
        for admin_file in os.listdir(os.path.join("./compData/admin/" + labeler +'/' + labeler + '/')):
            name_pair = admin_file.split("'")[1] #awef-awef_123.txt in folders ./compData/failed_labeler1 and ./compData/failed_labeler2
            #img_name = admin_file[:-4] + ".jpg"
            #img_name = img_name.split("/")[-1]
            img_name = './compData/admin' + labeler + '/' + admin_file[:-4] + ".jpg"
            admin_file_path = './compData/admin/' + labeler + '/' + labeler + '/' + admin_file
            box1 = image_labels('./compData/failed_labeler1/' + name_pair)
            box2 = image_labels('./compData/failed_labeler2/' + name_pair)
            box3 = image_labels(admin_file_path)
            results = [box3.verify_labels(box1), box3.verify_labels(box2)]
            if results[0] and results[1]:
                os.rename(admin_file_path, "./output/labels/" + admin_file)
            elif results[0] and not results[1]:
                average_files('./compData/failed_labeler1/' + name_pair, admin_file_path, "./output/labels/")
            elif results[1] and not results[0]:
                average_files('./compData/failed_labeler2/' + name_pair, admin_file_path, "./output/labels/")
            else:
                if not os.path.exists("./compData/admin/unused_images/"):
                    os.makedirs("./compData/admin/unused_images/")
                os.rename(img_name, "./compData/admin/unused_images/" + admin_file[:-4] + ".jpg") #./compData/admin/hi.jpg