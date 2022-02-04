#!/bin/bash
cat data/matrix_data.txt | python src/MM_mapper.py | sort -n | python src/MM_reducer.py