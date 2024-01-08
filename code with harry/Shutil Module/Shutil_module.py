import shutil

# To copy file in selected folder
shutil.copy("test.py","test1.py")

# To copy folder in selected folder
shutil.copytree("folders","copied_folder")

# To move file from given adress of folder 
shutil.move("folders/folder_test.py","moved_file.py")

# To delete a folder from selected folder
shutil.rmtree("copied_folder2")

# To delete a dile from given adressed folder
# --> use os modeule
import os
os.remove("test2.py")
