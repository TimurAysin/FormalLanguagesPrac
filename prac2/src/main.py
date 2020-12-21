from Grammar import Grammar
from Rule import Rule
from EarleyParser import EarleyParser


def main():
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

    word = input()
    print(parser.recognize(word))


if __name__ == "__main__":
    main()
