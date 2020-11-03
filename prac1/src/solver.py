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
                stack.append(RegLanguage(self.__k, sym))
            elif sym != '*':
                if len(stack) == 0:
                    raise RuntimeError("Error")
                l2 = stack.pop()
                if len(stack) == 0:
                    raise RuntimeError("Error")
                l1 = stack.pop()

                if sym == '+':
                    stack.append(RegLanguage.unite(l1, l2))
                elif sym == '.':
                    stack.append(RegLanguage.concatenate(l1, l2))
            else:
                if len(stack) == 0:
                    raise RuntimeError("Error")

                l1 = stack.pop()
                stack.append(RegLanguage.closure(l1))

        self.__reg_lang = stack.pop()

    def solve(self):
        self.make_language()

        if self.__l in self.__reg_lang.lengths:
            print("YES")
        else:
            print("NO")
