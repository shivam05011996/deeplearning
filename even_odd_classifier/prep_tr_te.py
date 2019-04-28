import random
import numpy as np


def prep_train_set(num_sample=10000, min_val=1, max_val=50000):
    train_sample_list = []
    train_labels_list = []

    for i in range(num_sample):
        sample = random.randint(min_val, max_val)
        if [sample] in train_sample_list:
            continue

        train_sample_list.append([sample])


        if sample % 2 == 0:
            train_labels_list.append([0])
        else:
            train_labels_list.append([1])


    return np.array(train_sample_list, dtype=np.int64), np.array(train_labels_list, dtype=np.int64)

def prep_test_set(num_sample=10000, min_val=50000, max_val=1000000):
    test_sample_list = []
    test_labels_list = []

    for i in range(num_sample):
        sample = random.randint(min_val, max_val)
        if [sample] in test_sample_list:
            continue

        test_sample_list.append([sample])

        if sample % 2 == 0:
            test_labels_list.append([0])
        else:
            test_labels_list.append([1])

    return np.array(test_sample_list, dtype=np.int64), np.array(test_labels_list, dtype=np.int64)



