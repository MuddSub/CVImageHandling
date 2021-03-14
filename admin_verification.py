from image_labels import *
def admin_verify(verified_text_files):
    total_images = count("./compData/admin/", "jpg")
    print("Admin verification started. Total images is ", total_images)
    admin_labelers = [name for name in os.listdir("./compData/admin/") if os.path.isdir(os.path.join("./compData/admin/", name))]
    if('unused_images' in admin_labelers):
        admin_labelers.remove('unused_images')
    while(len(verified_text_files) < total_images + 1):
        time.sleep(10)
        for labeler in admin_labelers:
            print("currently checking files verified by: ", labeler)
            for admin_file in os.listdir(os.path.join("./compData/admin/" + labeler +'/' + labeler + '/')):
                if admin_file in verified_text_files:
                    continue
                print("currently checking: ", admin_file)
                name_pair = admin_file.split("'")[1] #awef-awef_123.txt in folders ./compData/failed_labeler1 and ./compData/failed_labeler2
                if name_pair in verified_text_files:
                    continue
                #img_name = admin_file[:-4] + ".jpg"
                #img_name = img_name.split("/")[-1]
                img_name = './compData/admin/' + labeler + '/' + admin_file[:-4] + ".jpg"
                admin_file_path = './compData/admin/' + labeler + '/' + labeler + '/' + admin_file
                box1 = image_labels('./compData/failed_labeler1/' + name_pair)
                box2 = image_labels('./compData/failed_labeler2/' + name_pair)
                box3 = image_labels(admin_file_path)
                results = [box3.verify_labels(box1), box3.verify_labels(box2)]
                if results[0] and results[1]:
                    print("True, True, the admin labels has been moved to output/labels")
                    shutil.copy(admin_file_path, "./output/labels/" + admin_file)
                    admin_passed = open("admin_passed_verification.txt", "a")
                    print("passed ", admin_file, file = admin_passed)
                    admin_passed.close()
                    #os.rename(admin_file_path, "./output/labels/" + admin_file)
                elif results[0] and not results[1]:
                    print("failed_labeler1 and admin labels has been averaged and moved to output/labels")
                    average_files('./compData/failed_labeler1/' + name_pair, admin_file_path, "./output/labels/")
                    admin_passed = open("admin_passed_verification.txt", "a")
                    print("passed ", admin_file, file = admin_passed)
                    admin_passed.close()
                elif results[1] and not results[0]:
                    print("failed_labeler2 and admin labels has been averaged and moved to output/labels")
                    average_files('./compData/failed_labeler2/' + name_pair, admin_file_path, "./output/labels/")
                    admin_passed = open("admin_passed_verification.txt", "a")
                    print("passed ", admin_file, file = admin_passed)
                    admin_passed.close()
                else:
                    if not os.path.exists("./compData/admin/unused_images/"):
                        os.makedirs("./compData/admin/unused_images/")
                    print("False, False, no label will be outputed")
                    os.rename(img_name, "./compData/admin/unused_images/" + admin_file[:-4] + ".jpg") #./compData/admin/hi.jpg
                    admin_failed = open("admin_failed_verification.txt", "a")
                    print("failed ", admin_file, file = admin_failed)
                    admin_failed.close()
                verified_text_files.append(admin_file)
                admin_verification_records = open('./admin_verified_text_files.txt', 'a')
                print(admin_file, file = admin_verification_records)
                admin_verification_records.close()

if __name__ == "__main__":
    verified_text_files = []
    if (os.path.exists("./admin_verified_text_files.txt")):
        verification_records = open('./admin_verified_text_files.txt', 'r')
        verified_text_files = verification_records.readlines()
        verified_text_files = [x.strip("\n") for x in verified_text_files]
        verified_text_files.apend('bookmark.txt')
    else:
        verified_text_files = ['bookmark.txt']
    print("length of verified_text_files ", len(verified_text_files))
    print(verified_text_files)
    admin_verify(verified_text_files)