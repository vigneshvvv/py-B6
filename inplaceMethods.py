class Number:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other.value
        return self

n1 = Number(10)
n2 = Number(20)

n1 += n2
print(n1.value)