from Grammar import Grammar
from Rule import Rule
from State import State
from copy import deepcopy


class EarleyParser:
    def __init__(self, grammar):
        if not isinstance(grammar, Grammar):
            raise ValueError("Wrong type of parser's argument.")

        self.grammar = deepcopy(grammar)
        self.grammar.terminals.append("#")
        self.grammar.rules.append(Rule("#", "S"))

        self.situations = []
        self.word = ""

    def recognize(self, word):
        length = len(word) + 1
        self.situations = [0] * length
        for i in range(0, length):
            self.situations[i] = set()
        self.word = word

        if not isinstance(word, str):
            raise ValueError("Wrong type of parser's argument.")

        self.situations[0].add(State(0, 0, "#", ".S"))

        for j in range(0, length):
            self.scan(j)
            change1 = True
            change2 = True

            while change1 or change2:
                change1 = self.complete(j)
                change2 = self.predict(j)

            print("D_%d = {" %(j))
            for state in self.situations[j]:
                print("[{} -> {}, {}]".format(state.from_w, state.to_w, state.start_index))
            print("}")

        for state in self.situations[len(word)]:
            if state.from_w == '#' and state.to_w == "S." and state.start_index == 0:
                return True
        return False

    def scan(self, j):
        if j == 0:
            return

        add_later = set()

        for state in self.situations[j - 1]:
            if state.after_dot() == "":
                continue
            sym = state.to_w[state.dot_index + 1]
            if sym == self.word[j - 1]:
                add_later.add(State(state.start_index,
                                    state.dot_index + 1,
                                    state.from_w,
                                    state.before_dot() + sym + "." + state.after_dot()[1:]))
        self.situations[j].update(add_later)

    def complete(self, j):
        change = False
        add_later = set()

        for state in self.situations[j]:
            if state.after_dot() != "":
                continue

            for state2 in self.situations[state.start_index]:
                if state2.after_dot() == "":
                    continue
                elif state2.after_dot()[0] != state.from_w:
                    continue

                new_state = State(state2.start_index, state2.dot_index + 1, state2.from_w,
                                  state2.before_dot() + state.from_w + "." + state2.after_dot()[1:])
                if new_state not in self.situations[j]:
                    add_later.add(new_state)
                    change = True

        self.situations[j].update(add_later)

        return change

    def predict(self, j):
        change = False
        add_later = set()
        for state in self.situations[j]:
            if state.after_dot() == "":
                continue
            sym = state.after_dot()[0]
            for rule in self.grammar.rules:
                if rule.u == sym:
                    new_state = State(j, 0, sym, "." + rule.s)
                    if new_state not in self.situations[j]:
                        add_later.add(new_state)
                        change = True
        self.situations[j].update(add_later)
        return change
