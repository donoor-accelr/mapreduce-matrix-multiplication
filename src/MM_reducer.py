#!/usr/bin/env python3

import sys
import argparse


NUMBER_OF_COLUMNS_IN_A = 3


def argument_parser():
    """
        Parse the desired input from the user.

    Expected arguments:
    --mapper_output:    (str) Path to Mapper output file path
    Returns
    -------
    input_parser.parse_args
    """
    input_parser = argparse.ArgumentParser(prog='Matrix Multiplication Mapper')
    input_parser.add_argument('--mapper_output',
                              type=str,
                              default='../data/mapper_output.txt',
                              help='Path to Mapper output file path')
    return input_parser.parse_args()


def main():
    parsed_arguments = argument_parser()

    # with open(parsed_arguments.mapper_output) as f:
    #     key_value_pairs = f.readlines()

    current_key = None
    total_sum = 0.0
    value_dict = dict()

    # for key_value_pair in key_value_pairs:
    for key_value_pair in sys.stdin:
        key_value_pair = key_value_pair.strip()

        key, value = key_value_pair.split('\t', 1)

        try:
            row_number, column_number = map(int, key.split(','))
            key = (row_number, column_number)

            value = value.split(',')
            replicate_key, element_value = int(value[1]), float(value[2])
        except:
            continue

        if key == current_key:
            if replicate_key not in value_dict:
                value_dict[replicate_key] = [element_value]
            else:
                value_dict[replicate_key].append(element_value)
        else:
            if current_key:
                for i in range(NUMBER_OF_COLUMNS_IN_A):
                    if (i in value_dict) and (len(value_dict[i]) == 2):
                        total_sum += value_dict[i][0] * value_dict[i][1]
                print('({},{}),{}'.format(current_key[0],
                                          current_key[1],
                                          total_sum,
                                          )
                      )

            current_key = key
            value_dict = dict()
            value_dict[replicate_key] = [element_value]
            total_sum = 0.0

    if current_key:
        for j in range(NUMBER_OF_COLUMNS_IN_A):
            if (j in value_dict) and (len(value_dict[j]) == 2):
                total_sum += value_dict[j][0] * value_dict[j][1]
        print('({},{}),{}'.format(current_key[0],
                                  current_key[1],
                                  total_sum,
                                  )
              )


if __name__ == '__main__':
    main()
