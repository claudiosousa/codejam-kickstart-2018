input_file = open('data/input.sample', "r")

import solver
solver.input = input_file.readline
solver.run()
