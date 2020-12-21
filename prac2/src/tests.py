from EarleyParser import EarleyParser
from Rule import Rule
from Grammar import Grammar


def main():
    tests = [
        ["cbcb", True],
        ["cabcb", True],
        ["caaabbbcb", True],
        ["cccaaabbbcb", True],
        ["cccccaaaaaaabbbbcb", True],
        ["cbabbcb", True],
        ["cbbaaabbbbcb", True],
        ["ccccccccaaaaaabbaaabbbbcb", True],
        ["b", False],
        ["aabbc", False],
        ["aabb", False],
        ["caabc", False],
        ["ccabbacb", False],
        ["aabcb", False]
    ]

    rules = []
    terminals = ['S', 'T', 'U', 'V']
    nonterminals = ['c', 'b', 'a']

    rules.append(Rule("S", "cTb"))
    rules.append(Rule("S", "cS"))
    rules.append(Rule("T", "U"))
    rules.append(Rule("T", "aT"))
    rules.append(Rule("U", "Vc"))
    rules.append(Rule("U", "bU"))
    rules.append(Rule("V", "aVb"))
    rules.append(Rule("V", "b"))

    grammar = Grammar(terminals, nonterminals, rules)
    parser = EarleyParser(grammar)

    for test in tests:
        print("Testing word {}, should be {}.".format(test[0], test[1]))

        if parser.recognize(test[0]) == test[1]:
            print("Test passed.")
        else:
            print("Test didn't pass.")


if __name__ == "__main__":
    main()
