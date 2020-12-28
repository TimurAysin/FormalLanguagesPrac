import copy


class Vertex:
    def __init__(self):
        self.is_terminal = True
        self.edges = dict()
        self.has_cycle = False

    def make_edge(self, vtx, ch):
        if not isinstance(vtx, Vertex):
            raise ValueError("Can't make edge to an object that is not vertex.")

        if not isinstance(ch, str):
            raise ValueError("Can't initialize vertex.")

        if ch not in self.edges.keys():
            self.edges[ch] = [vtx]
        else:
            self.edges[ch].append(vtx)


class RegLanguage:

    def __init__(self, k1, sym):
        self.k = k1
        self.lengths = set()
        if sym is None:
            self.start = Vertex()
            self.finals = [self.start]
            self.lengths.add(0)
            return

        self.start = 0
        self.finals = []

        vtx1 = Vertex()
        vtx2 = Vertex()

        vtx1.is_terminal = False
        vtx1.make_edge(vtx2, sym)

        self.finals.append(vtx2)
        self.start = vtx1
        if sym != '1':
            self.lengths.add(1)
        else:
            self.lengths.add(0)

    @staticmethod
    def concatenate(l1, l2):
        if not isinstance(l1, RegLanguage) or not isinstance(l2, RegLanguage):
            raise ValueError()

        new_lang = copy.copy(l1)
        new_lang.finals = l2.finals

        for ind in range(len(l1.finals)):
            l1.finals[ind].make_edge(l2.start, '1')
            l1.finals[ind].is_terminal = False

        new_lang.lengths = set()
        for x in l1.lengths:
            for y in l2.lengths:
                new_lang.lengths.add((x + y) % new_lang.k)

        return new_lang

    @staticmethod
    def unite(l1, l2):
        if not isinstance(l1, RegLanguage) or not isinstance(l2, RegLanguage):
            raise ValueError()

        new_lang = RegLanguage(l1.k, None)
        new_lang.start.is_terminal = False

        new_lang.finals = l1.finals
        new_lang.finals += l2.finals

        new_lang.start.make_edge(l1.start, '1')
        new_lang.start.make_edge(l2.start, '1')

        new_lang.lengths = l1.lengths.union(l2.lengths)

        return new_lang

    @staticmethod
    def closure(l1):
        if not isinstance(l1, RegLanguage):
            raise ValueError()

        new_lang = RegLanguage(l1.k, None)

        new_lang.start.make_edge(l1.start, '1')

        for vtx in l1.finals:
            vtx.make_edge(new_lang.start, '1')
            vtx.is_terminal = False


        # O(K^2)
        known_values = [0] * new_lang.k
        for x in l1.lengths:
            known_values[x] = 1

        queue = list(l1.lengths)

        i = 0
        k = new_lang.k
        while True:
            first_elem = queue[i]
            j = 0

            add_later = []
            while j < len(queue):
                to_add = (queue[j] + first_elem) % k
                if not known_values[to_add]:
                    add_later.append(to_add)
                    known_values[to_add] = 1
                j += 1

            queue += add_later

            if i < len(queue) - 1:
                i += 1
            else:
                break

        new_lang.lengths = set()
        for x in range(k):
            if known_values[x] == 1:
                new_lang.lengths.add(x)

        return new_lang
