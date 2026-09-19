import random
from relu import ReLU

class Neuron:
    def __init__(self, inputs):
        self.inputs = inputs
        self.weights = [random.uniform(-1, 1) for _ in range(inputs)]
        self.bias = random.uniform(-1, 1)

    def forward(self, x):
        prediction = []


        for weight, input in zip(self.weights, x):
            prediction.append(weight * input)

        prediction = sum(prediction) + self.bias
        return prediction



