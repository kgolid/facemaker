import os
import random
from svgpathtools import svg2paths, wsvg, disvg


def scale_and_align(shape, feature_type):
    """ TODO """
    return shape


def get_paths_from_directory(dirpath, feature_type):
    svgs = filter(lambda fi: fi.endswith(".svg"), os.listdir(dirpath))
    chosen_svg = random.choice(svgs)
    paths, _ = svg2paths(dirpath + chosen_svg)
    return scale_and_align(paths, feature_type)


def main():
    eyepaths = get_paths_from_directory('./faces/eyes/', 'EYES')
    nosepaths = get_paths_from_directory('./faces/noses/', 'NOSE')
    mouthpaths = get_paths_from_directory('./faces/mouths/', 'MOUTH')

    facepaths = eyepaths + nosepaths + mouthpaths
    wsvg(facepaths)


if __name__ == '__main__':
    main()
