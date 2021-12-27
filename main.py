from image import create_views
from match import create_matches
from sfm import SFM
import time
from logger import Logger

import argparse

images_dir = "./images"
views = []


def set_args(parser):
    parser.add_argument('--imgs_dir', type=str, default="./images")


def main(args):
    logger = Logger()
    views = create_views(args.imgs_dir)
    matches = create_matches(views)
    sfm = SFM(views,matches)
    sfm.performReconstruction()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    set_args(parser)
    args = parser.parse_args()
    main(args)
