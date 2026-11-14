#block1 - import process
from PIL import Image
path = input("enter pic/gif path : ")

try:
    #!pics & gifs
    pic1gif = Image.open(path)
    print("Asset successfully imported!")
#!invalid inputs
except FileNotFoundError:
    print(" ERROR : file not found. check path :) ")
except Exception as e:
    print("error :", e)
#!test
# print(pic1gif.format, pic1gif.size)

#block2 - convertion process
#!Conversion function
from PIL import ImageSequence, ImageOps
#&ASCII characters (dark to bright)
ASCII_CHARS = "@%#*+=-:. "
#& Conversion function
def convert_to_ascii(image, width=100):
    #& Convert image to grayscale
    image = ImageOps.grayscale(image)
    #& Resize while preserving proportions
    ratio = image.height / image.width
    height = int(width * ratio * 0.5)
    image = image.resize((width, height))
    #& Extract pixel values
    pixels = list(image.get_flattened_data())
    ascii_str = ""
    #& Convert each pixel into an ASCII character
    for pixel in pixels:
        index = pixel * (len(ASCII_CHARS) - 1) // 255
        ascii_str += ASCII_CHARS[index]
    #& Split ASCII characters into lines
    ascii_img = "\n".join(
        ascii_str[i:i + width]
        for i in range(0, len(ascii_str), width)
    )

    return ascii_img


#! Detect image or GIF
ascii_frames = []
frame_durations = []

if getattr(pic1gif, "is_animated", False):

    #& Process every GIF frame
    for frame in ImageSequence.Iterator(pic1gif):
        ascii_frames.append(convert_to_ascii(frame.copy()))
        frame_durations.append(
            frame.info.get("duration", 100)
        )

else:

    #& Process a single image
    ascii_frames.append(convert_to_ascii(pic1gif))
    frame_durations.append(0)

print("ASCII conversion completed!")

#block3 - output process
import os
import time

#! Clear terminal
os.system("cls" if os.name == "nt" else "clear")

#! Detect image or GIF
if len(ascii_frames) > 1:

    #& Display GIF frames
    while True:
        for i, frame in enumerate(ascii_frames):

            os.system("cls" if os.name == "nt" else "clear")

            print(frame)

            #& Wait according to original GIF frame duration
            time.sleep(frame_durations[i] / 1000)

else:

    #& Display a single ASCII image
    print(ascii_frames[0])





