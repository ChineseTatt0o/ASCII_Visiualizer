#block1 - import process
from PIL import Image
path = input("enter pic/gif path : ")
#!pics & gifs
pic1gif = Image.open(path)
#!invalid inputs
try:
    img = path
except FileNotFoundError:
    print("ERROR : file not found. check path")
except Exception as e:
    print("error :", e)
#!test
# print(pic1gif.format, pic1gif.size)




