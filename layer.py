from neuron import Neuron

class Layer:
    def __init__(self, inputs, outputs):
        self.neurons = [Neuron(inputs) for _ in range(outputs)]

    def forward(self, x):
        return [neuron.forward(x) for neuron in self.neurons]


