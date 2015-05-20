#!/bin/env python2.7

# This script creates thumbnail images for all png images in a directory.
# The original size images are renamed to [name]_large.png while the thumbnail
# images are saved as [name].png (the original filename).

from PIL import Image
import os
import sys
import shutil

MAX_SIZE = 600, 400

def thumbnail_resize(path, full_file_name, file_name, full_file_path):
    try:
        image = Image.open(full_file_path)

        if image.size[0] < MAX_SIZE[0] and image.size[1] < MAX_SIZE[1]:
            print "File '%s' is already thumbnail size." % full_file_name
        else:
            copy_file_name = file_name + "_large.png"
            copy_file_path = os.path.join(path, copy_file_name)

            if os.path.isfile(copy_file_path):
                print "File '%s' exists, skipping copy." % copy_file_name
            else:
                print "Copying '%s' to '%s'" % (full_file_name, copy_file_name)
                shutil.copyfile(full_file_path, copy_file_path)

                print "Creating thumbnail for '%s'." % full_file_name
                image.thumbnail(MAX_SIZE, Image.ANTIALIAS)
                image.save(full_file_path, "png")
    except IOError:
        print "Could not create thumbnail for '%s'." % full_file_name

if __name__ == '__main__':
    path = sys.argv[1] if (len(sys.argv) > 1) else "."

    for full_file_name in os.listdir(path):
        file_name, file_ext = os.path.splitext(full_file_name)
        full_file_path = os.path.join(path, full_file_name)

        if file_ext != ".png" or file_name.endswith("_large"): continue

        thumbnail_resize(path, full_file_name, file_name, full_file_path)
