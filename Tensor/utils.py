MAX_SEQUENCE_POSTIONS = 2
PAD = 0

# -----------------------------------------------------
# Get the length safely
# -----------------------------------------------------
def get_length(value):
    if isinstance(value, (int, float)):
        return 0

    if isinstance(value, (list, tuple)):
        return len(value)

    if hasattr(value, "data"):
        return len(value.data)

    raise TypeError(f"Unsupported type: {type(value).__name__}")


# -----------------------------------------------------
# Check types
# -----------------------------------------------------
class Is:
    def __init__(self, value):
        self.value = value

    def str(self):
        return isinstance(self.value, str)

    def list(self):
        return isinstance(self.value, list)

    def tuple(self):
        return isinstance(self.value, tuple)

    def int(self):
        return isinstance(self.value, int)

    def float(self):
        return isinstance(self.value, float)

    def bool(self):
        return isinstance(self.value, bool)

    def number(self):
        return isinstance(self.value, (int, float))

def encode(word):
    encoded = []
    for letter in word:
        encoded.append(ord(letter) / 122.0)

    return encoded

def decode(word):
    decoded = chr(round(word * 122.0))

    return decoded

def encode_sentence(sentence):
    encoded = []
    for letter in sentence:
        encoded.extend(encode(letter))
    encoded.extend([PAD] * (MAX_SEQUENCE_POSTIONS - len(encoded)))
    return encoded

def decode_sentence(sentence):
    if PAD in sentence:
        index = sentence.index(PAD)
        del sentence[index:]
    decoded = ""
    for word in sentence:
        decoded += decode(word)
    return decoded


print(encode_sentence("Hi"))
