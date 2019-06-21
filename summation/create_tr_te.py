import sys
import json
from random import randint

MIN = int(sys.argv[2])
MAX = int(sys.argv[3])

tr_file = open(sys.argv[4], 'w+')

def create_training_samples():
    for i in range(int(sys.argv[1])):
        n1 = randint(MIN, MAX)
        n2 = randint(MIN, MAX)

        s = n1 + n2
        tr_file.write(json.dumps((n1, n2, s)) + '\n')

if __name__ == '__main__':
    create_training_samples()
