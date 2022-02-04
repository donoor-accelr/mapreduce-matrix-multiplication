#!/usr/bin/env python3

import argparse


NUMBER_OF_ROWS_IN_A = 2
NUMBER_OF_COLUMNS_IN_B = 2


def argument_parser():
    """
        Parse the desired input from the user.

    Expected arguments:
    --a_matrix_path:    (str) Path to A matrix text file
    --b_matrix_path:    (str) Path to B matrix text file

    Returns
    -------
    input_parser.parse_args
    """
    input_parser = argparse.ArgumentParser(prog='Matrix Multiplication Mapper')
    input_parser.add_argument('--a_matrix_path',
                              type=str,
                              default='./a_matrix.txt',
                              help='Path to A matrix text file')
    input_parser.add_argument('--b_matrix_path',
                              type=str,
                              default='./b_matrix.txt',
                              help='Path to B matrix text file')
    return input_parser.parse_args()


def read_matrix(file_path: str, matrix_name: str, num_of_times: int):
    with open(file_path) as f:
        matrix_rows = f.readlines()
    for row_number, row in enumerate(matrix_rows):
        row_values = row.split(" ")
        row_values = map(int, row_values)
        for column_number, value in enumerate(row_values):
            for i in range(num_of_times):
                if matrix_name == "A":
                    print('{},{}\t{},{},{}'.format(row_number,
                                                   i,
                                                   matrix_name,
                                                   column_number,
                                                   value)
                          )
                else:
                    print('{},{}\t{},{},{}'.format(i,
                                                   column_number,
                                                   matrix_name,
                                                   row_number,
                                                   value)
                          )


def main():
    parsed_arguments = argument_parser()
    read_matrix(parsed_arguments.a_matrix_path, "A", NUMBER_OF_COLUMNS_IN_B)
    read_matrix(parsed_arguments.b_matrix_path, "B", NUMBER_OF_ROWS_IN_A)


if __name__ == '__main__':
    print("Mappppppppppppppppper startttttt99999999999")
    main()
