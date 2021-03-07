# This is experiemental file for debug purposes.
import utils


generator = utils.data_generator(100)

print(generator.data)

generator.export()