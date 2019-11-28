import os
import shutil
import hashlib

hash_dict = {}

user_input = raw_input("Enter path to images: ")
assert os.path.exists(user_input), "Couldn't find directory "+str(user_input)
os.chdir(user_input)

copy_dir = raw_input("Enter path to copy images to: ")
if not os.path.exists(copy_dir):
    os.mkdir(copy_dir)

for dirName, subdirList, fileList in os.walk(user_input):
    for fname in fileList:
        imagefile = open(fname)
        image_contents = imagefile.read()
        fileHash = hashlib.md5(image_contents).hexdigest()
        imagefile.close()
        if fileHash not in hash_dict.keys():
            hash_dict[fileHash] = fname
            print(fileHash + " : " + fname)
            shutil.copy(fname, copy_dir)
