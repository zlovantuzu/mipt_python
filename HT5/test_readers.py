import sys
import argparse

from utils.image_toner import equalization, gamma_correction
from utils.reader import image_reader as imread
from utils.reader import csv_reader, bin_reader, txt_reader, json_reader
from utils.processor import histogram
from utils.writer import image_writer

from utils.image_toner import stat_correction


def print_args_1():
    print(type(sys.argv))
    if (len(sys.argv) > 1):
        for param in sys.argv[1:]:
            print(param, type(param))
    return sys.argv[1:]

def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-img', '--img_path', default='', help='Path to image')

    parser.add_argument('-p', '--path', default='', help='Input file path ')
    # parser.add_argument('-t','--type', default='txt', help='Input file format ')
    parser.add_argument('-m', '--mode', default='hist', help='Input program mode: hist (histogram), equal (equalization), gc (gamma correction), st (stat correction)')

    parser.add_argument('-o', '--output', help='Save file path')
    parser.add_argument('-g', '--gamma', default='2.2', help='Input gamma value for gamma correction')

    return parser

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = init_parser()
    args = parser.parse_args(sys.argv[1:])

    if args.img_path == '':
        print('arg: \"img_path\" missing')
        exit(0)
    if args.output == '':
        print('arg: \"output\" missing')
        exit(0)

    image = None
    hist = None

    image = imread.read_data(args.img_path)

    if args.mode == "hist":
        image_writer.write_data(args.output, histogram.image_processing(image))
    elif args.mode == "equal":
        image_writer.wite_data(args.output, equalization.processing(image))
    elif args.mode == "gc":
        if args.gamma == '':
            print('arg: \"mg_path\" missing')
            exit(0)
        image_writer.write_data(args.output, gamma_correction.processing(image, float(args.gamma)))
    elif args.mode == "st":
        if args.path == '':
            print('arg: \"path\" missing')
            exit(0)
        fileType = open(args.path).name.split(".")[-1]
        hist_template = None
        match fileType:
            case 'img':
                hist_template = histogram.image_processing(imread.read_data(args.path))
            case 'csv':
                hist_template = csv_reader.read_data(args.path)
            case 'bin':
                hist_template = bin_reader.read_data(args.path)
            case 'txt':
                hist_template = txt_reader.read_data(args.path)
            case 'json':
                hist_template = json_reader.read_data(args.path)
            case _:
                print('\"fileType\" invalid')
                pass

        res_image = stat_correction.processing(hist_template, image)
        image_writer.write_data(args.output, res_image)
    else:
        print('arg: \"mode\" invalid')
        exit(0)

