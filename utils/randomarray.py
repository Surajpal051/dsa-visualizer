## Function to generate the random array

import random
def random_array(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0,100))
    return arr