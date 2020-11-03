import copy


class Vertex:
    def __init__(self):
        self.is_terminal = True
        self.edges = dict()

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

    def __init__(self, sym):
        if sym is None:
            self.vtx = [Vertex()]
            self.start_ind = 0
            self.final_ind = [0]
            return

        self.vtx = []
        self.start_ind = 0
        self.final_ind = []

        vtx1 = Vertex()
        vtx2 = Vertex()

        vtx1.is_terminal = False

        self.final_ind.append(1)
        self.start_ind = 0

        self.vtx.append(vtx1)
        self.vtx.append(vtx2)

        self.vtx[0].make_edge(self.vtx[1], sym)

    @staticmethod
    def concatenate(l1, l2):
        if not isinstance(l1, RegLanguage) or not isinstance(l2, RegLanguage):
            raise ValueError()

        new_lang = copy.copy(l1)
        offset = len(l1.vtx)

        new_lang.vtx += l2.vtx

        for ind in l1.final_ind:
            new_lang.vtx[ind].make_edge(new_lang.vtx[l2.start_ind + offset], '1')
            new_lang.vtx[ind].is_terminal = False

        new_lang.final_ind = []

        for ind in l2.final_ind:
            new_lang.final_ind.append(ind + offset)

        return new_lang

    @staticmethod
    def unite(l1, l2):
        if not isinstance(l1, RegLanguage) or not isinstance(l2, RegLanguage):
            raise ValueError()

        new_lang = RegLanguage(None)
        new_lang.vtx[0].is_terminal = False
        new_lang.vtx += l1.vtx
        new_lang.final_ind = l1.final_ind
        new_lang.vtx[0].make_edge(new_lang.vtx[1], '1')

        for i in range(len(new_lang.final_ind)):
            new_lang.final_ind[i] += 1

        new_lang.vtx += l2.vtx
        for i in range(len(l2.final_ind)):
            l2.final_ind[i] += 1 + len(l1.vtx)

        new_lang.final_ind += l2.final_ind
        new_lang.vtx[0].make_edge(new_lang.vtx[1 + len(l1.vtx)], '1')

        return new_lang

    @staticmethod
    def closure(l1):
        if not isinstance(l1, RegLanguage):
            raise ValueError()

        new_lang = RegLanguage(None)

        new_lang.vtx += l1.vtx
        new_lang.vtx[0].make_edge(new_lang.vtx[1], '1')

        for ind in l1.final_ind:
            new_lang.vtx[1 + ind].make_edge(new_lang.vtx[0], '1')
            new_lang.vtx[1 + ind].is_terminal = False

        return new_lang