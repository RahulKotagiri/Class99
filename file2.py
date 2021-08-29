import os
import shutil

path = "/Users/Rahul/"

print("before copying file: ")
print( os.listdir(path))

source = "/Users/Rahul/Test.txt"
destination = "/Users/Rahul/Final.txt"
dest = shutil.copy(source, destination)
print("after copying file")
print(os.listdir(path))