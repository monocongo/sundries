import argparse
import os
from xml.etree import ElementTree

if __name__ == "__main__":

    # parse the command line arguments
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--labels_dir",
                             required=True,
                             help="path to directory containing label files")
    args_parser.add_argument("--images_dir",
                             required=True,
                             help="path to directory containing image files")
    args = vars(args_parser.parse_args())

    # rewrite each label (annotation) file's image path value
    for label_file in os.listdir(args["labels_dir"]):
        if label_file.endswith(".xml"):

            # prepend the directory to the file to get the full path
            label_file = os.sep.join((args["labels_dir"], label_file))

            # parse the XML into an ElementTree
            tree = ElementTree.parse(label_file)

            # get the original path value, pull out the file name
            original_path = tree.find('.//path')
            _, file = os.path.split(os.path.abspath(original_path.text))

            # add the images directory where the file should actually be located
            image_file_path = os.sep.join((args["images_dir"], file))

            # replace the image file path value
            tree.find('.//path').text = image_file_path

            # write the tree back into the file
            tree.write(label_file)
