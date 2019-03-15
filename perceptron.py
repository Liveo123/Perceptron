import random

WEIGHTS_SIZE = 2

class Perceptron:

    # Constructor
    def __init__(self):
        self.weights = []

        # Initialise weights
        for x in range(WEIGHTS_SIZE):
            self.weights = random.uniform(-1, 1)

    def guess(self, inputs):
        asset(len(self.weights)) == len(inputs)), 
                                        "Ensure inputs is the same length as weights." 
        sum = 0
        for i in range(0, weights):
            sum += input[i]*weights[i]
