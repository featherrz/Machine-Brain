from Tensor.dimensions import calculate, shape
from Tensor.utils import Is, encode_sentence, decode_sentence

class Tensor:
    def __init__(self, data):
        self.data = []
        for d in data:
            question = d[0]
            answer = d[1]
            self.data.append((encode_sentence(question), encode_sentence(answer)))

        self.unrefined_data = data

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data).replace("[", "").replace("]", "")

    def __eq__(self, other):
        if not isinstance(other, Tensor):
            return False

        return self.data == other.data

    def value(self):
        return self.data

    def __ne__(self, other):
        return not self == other

    def shape(self):
        return shape(self)


