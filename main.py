from tws import main
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', help='The example input file', required=True)
    args = parser.parse_args()

    i = open(args.input_file).read()

    main(i)
