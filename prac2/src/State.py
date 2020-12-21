class State:
    def __init__(self, start_index, dot_index, from_w, to_w):
        self.start_index = start_index
        self.dot_index = dot_index
        self.from_w = from_w
        self.to_w = to_w

    def before_dot(self):
        return self.to_w[:self.dot_index]

    def after_dot(self):
        return self.to_w[self.dot_index + 1:]

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return other.start_index == self.start_index and other.dot_index == self.dot_index and self.from_w == other.from_w and self.to_w == other.to_w

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.start_index, self.dot_index, self.from_w, self.to_w))
