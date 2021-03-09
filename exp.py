# This is experiemental file for debug purposes.
import utils

generator = utils.data_generator(100)

for i in range(500):
    print(generator.generate_one()['rating'])