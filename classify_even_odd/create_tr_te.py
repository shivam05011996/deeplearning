import sys
import json
from random import randint

MIN = int(sys.argv[3])
MAX = int(sys.argv[4])

tr_file = open(sys.argv[1], 'w+')
next_line = '\n'

def create_training_samples():
    for i in range(int(sys.argv[2])):
        num = randint(MIN, MAX)
        if num % 2 == 0:
            tr_file.write(json.dumps((num, 0, 0)) + next_line)
        else:
            tr_file.write(json.dumps((num, 1, 1)) + next_line)

if __name__ == '__main__':
    create_training_samples()

