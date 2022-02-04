#!/usr/bin/env python3

import sys


NUMBER_OF_COLUMNS_IN_A = 3


def main():

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
                for i in range(1, NUMBER_OF_COLUMNS_IN_A + 1):
                    if (i in value_dict) and (len(value_dict[i]) == 2):
                        total_sum = total_sum + value_dict[i][0] * value_dict[i][1]
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
        for j in range(1, NUMBER_OF_COLUMNS_IN_A + 1):
            if (j in value_dict) and (len(value_dict[j]) == 2):
                total_sum = total_sum + value_dict[j][0] * value_dict[j][1]
        print('({},{}),{}'.format(current_key[0],
                                  current_key[1],
                                  total_sum,
                                  )
              )


if __name__ == '__main__':
    main()
