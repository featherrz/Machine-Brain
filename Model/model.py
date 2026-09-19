from layer import Layer
import time

class TrainError(Exception):
    pass

class Model:
    def __init__(self, inputs, outputs, hidden_size=3, layers=3, learning_rate=0.01):
        self.layers = []
        self.learning_rate = learning_rate
        self.trained = False

        self.layers.append(Layer(inputs, hidden_size)) # First

        for _ in range(layers - 2):
            self.layers.append(Layer(hidden_size, hidden_size)) # Middle

        self.layers.append(Layer(hidden_size, outputs)) # Output/Last

    def forward(self, x):
        answer = x
        history = [x]

        for layer in self.layers:
            answer = layer.forward(answer)
            history.append(answer)

        return answer, history

    def train(self, dataset, epochs=1000, record_time=False, retrain=False):
        if self.trained and not retrain:
           raise TrainError("Model is already trained")

        if record_time:
           start = time.perf_counter()

        for _ in range(epochs):
            for example in dataset:
                question = example[0]
                correct = example[1]
                prediction, history = self.forward(question)
                errors = [y - p for y, p in zip(correct, prediction)]

                for layer_index in range(len(self.layers)-1, -1, -1):
                    layer = self.layers[layer_index]
                    layer_input = history[layer_index]
                    previous_error = [0] * len(layer_input)

                    for neuron, error in zip(layer.neurons, errors):
                        old_weights = neuron.weights[:]
                        for i in range(len(neuron.weights)):
                            correction = error * layer_input[i] * self.learning_rate
                            neuron.weights[i] += correction
                            previous_error[i] += error * old_weights[i]

                        neuron.bias += error * self.learning_rate
                    errors = previous_error

        if record_time:
           print(f"Training taken: {time.perf_counter() - start:.3f}s")

        self.trained = True

    def predict(self, x):
        answer, _ = self.forward(x)
        if len(answer) == 1:
            return answer[0]
        return answer



# DATASET
dataset = [
    ([1], [1]),
    ([2], [4]),
    ([3], [9]),
    ([4], [16]),
    ([5], [25]),
    ([6], [36]),
    ([7], [49]),
    ([8], [64]),
    ([9], [81]),
    ([10], [100]),
]

dataset = [
    (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    ),
    (
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    )
]

m = Model(inputs=10, outputs=10, hidden_size=10, learning_rate=0.000001)
m.train(dataset, record_time=True, epochs=100000)
print(m.predict([41, 42, 43, 44, 45, 46, 47, 48, 49, 50]))
