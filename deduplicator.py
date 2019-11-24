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
        fileHash = hashlib.md5(image_contents).hexdigest()
        imagefile.close()
        if fileHash not in hash_list.keys():
            hash_list[fileHash] = fname
            print(fileHash + " : " + fname)
            shutil.copy(fname, copy_dir)
