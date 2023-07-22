import os
import shutil

#source
from_dir="C:/Users/kaush/Downloads/Class 112/testA"
#Destination
to_dir="C:/Users/kaush/Downloads/Class 112/testB"

list_of_file=os.listdir(from_dir)

for file_name in list_of_file:
    name,extension=os.path.splitext(file_name)

    if extension == "":
        continue 
    if extension in ['.gif','.png','.jpg','.jpeg',',jfif']:

        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+"Image_files"
        path3=to_dir+'/'+"Image_files"+"/"+file_name

        if os.path.exists(path2):
            print("Moving"+file_name+"...")
            shutil.move(path1,path2)
        else:
            os.makedirs(path2)
            print("Moving"+file_name+"...")
            shutil.move(path1,path3)

    

