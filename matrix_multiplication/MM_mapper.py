#!/usr/bin/env python3

import sys

NUMBER_OF_ROWS_IN_A = 2
NUMBER_OF_COLUMNS_IN_B = 2


def main():
    for line in sys.stdin:

        line = line.strip()
        row_number, column_number, matrix_name, value = line.split(" ")

        if matrix_name == "A":
            for i in range(1, NUMBER_OF_COLUMNS_IN_B+ 1):
                print('{},{}\t{},{},{}'.format(row_number,
                                               i,
                                               matrix_name,
                                               column_number,
                                               value)
                      )
        if matrix_name == "B":
            for i in range(1, NUMBER_OF_ROWS_IN_A + 1):
                print('{},{}\t{},{},{}'.format(i,
                                               column_number,
                                               matrix_name,
                                               row_number,
                                               value)
                      )


if __name__ == '__main__':
    main()
