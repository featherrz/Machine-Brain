print("[test]: ok (start)")

from Tensor.utils import Is
from Tensor.exceptions import ArraySizeError


# -----------------------------------------------------
# Calculate two arrays
# -----------------------------------------------------
def calculate(operator: str, self, other) -> list:

    self_data = self.data if hasattr(self, "data") else self
    other_data = other.data if hasattr(other, "data") else other

    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    if operator not in operations:
        raise ValueError(f"Unsupported operator: {operator}")

    operation = operations[operator]

    def recursive_calculate(a, b):
        a_type = Is(a)
        b_type = Is(b)

        if a_type.list() and b_type.list():
            if len(a) != len(b):
                raise ArraySizeError(
                    "Cannot calculate arrays with different sizes"
                )

            return [
                recursive_calculate(x, y)
                for x, y in zip(a, b)
            ]

        if a_type.number() and b_type.number():
            return operation(a, b)

        raise TypeError(
            f"Cannot calculate {type(a).__name__} with {type(b).__name__}"
        )

    return recursive_calculate(self_data, other_data)


print("[test]: ok (end)")


# -----------------------------------------------------
# Get the Array's shape
# -----------------------------------------------------
def shape(self):

    data = self.unrefined_data
    dimensions = []

    def find_shape(current):
        if not isinstance(current, list):
            return

        dimensions.append(len(current))

        if len(current) > 0 and isinstance(current[0], list):
            find_shape(current[0])

    find_shape(data)

    return tuple(dimensions)

