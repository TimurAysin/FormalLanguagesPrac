from src.RegLanguage import RegLanguage, Vertex


class Solution:
    literals = ['a', 'b', 'c', '1']

    def __init__(self, lang, k, l):
        self.__lang = lang
        self.__k = k
        self.__l = l
        self.__reg_lang = None

    def make_language(self):
        stack = []

        for sym in self.__lang:
            if sym in Solution.literals:
                stack.append(RegLanguage(sym))
            elif sym != '*':
                l2 = stack.pop()
                l1 = stack.pop()

                if sym == '+':
                    stack.append(RegLanguage.unite(l1, l2))
                elif sym == '.':
                    stack.append(RegLanguage.concatenate(l1, l2))
            else:
                l1 = stack.pop()
                stack.append(RegLanguage.closure(l1))

        self.__reg_lang = stack.pop()

    def solve(self):
        self.make_language()
