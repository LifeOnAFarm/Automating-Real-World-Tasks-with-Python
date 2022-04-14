"""
Automating Real-World Tasks with Python
Week 1
Seamus de Cleir

Use the Python Imaging Library to do the following to a batch of images:
Open an image
Rotate an image
Resize an image
Save an image in a specific format in a separate directory 
You'll have 90 minutes to complete this lab.
"""

# Import modules
import os
from PIL import Image

# Assign directory
directory = "images/"

# Iterate over files in image directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    try:
        im = Image.open(f)
        # Rotate and resize
        new_image = im.resize((128, 128)).rotate(90).convert('RGB')
        # Save a jpg
        new_image.save("/opt/icons/" + filename + ".jpg")
    except:
        print("This is not an image file: " + f)
