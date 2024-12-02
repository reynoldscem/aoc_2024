from argparse import ArgumentParser
from pathlib import Path
import numpy as np


def build_parser():
    parser = ArgumentParser()

    parser.add_argument('input_filename', type=Path)

    return parser


def monotonic(array):
    diffs = np.diff(array)
    signs = np.sign(diffs)[np.nonzero(diffs)]

    if signs.size == 0:
        return True

    return np.all(signs == signs[0])


def abs_change_in_accepted_values(array, accepted_values=range(1, 4)):
    absolute_differences = np.abs(np.diff(array))

    return np.setdiff1d(absolute_differences, np.array(accepted_values)).size == 0


def main():
    args = build_parser().parse_args()

    lines = args.input_filename.read_text().splitlines()
    lines = [list(map(int, line.split())) for line in lines]

    def safe(whole_array):
        arrays_with_deletion = (
            whole_array[:i] + whole_array[i + 1:]
            for i in range(len(whole_array))
        )
        return any(
            monotonic(array) and abs_change_in_accepted_values(array)
            for array in arrays_with_deletion
        )

    line_safety = [safe(line) for line in lines]
    print(sum(line_safety))


if __name__ == '__main__':
    main()
