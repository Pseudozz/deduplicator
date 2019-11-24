import os
import shutil
import hashlib

hash_list = {}
user_input = raw_input("Enter path to images: ")
copy_dir = raw_input("Enter path to copy images to: ")
assert os.path.exists(user_input), "Couldn't find directory "+str(user_input)

os.chdir(user_input)
if not os.path.exists(copy_dir):
    os.mkdir(copy_dir)

for dirName, subdirList, fileList in os.walk(user_input):
    for fname in fileList:
        imagefile = open(fname)
        image_contents = imagefile.read()
        jpg_hash = hashlib.md5(image_contents).hexdigest()
        imagefile.close()
        if jpg_hash not in hash_list.keys():
            hash_list[jpg_hash] = fname
            print(jpg_hash + " : " + fname)
            shutil.copy(fname, copy_dir)
