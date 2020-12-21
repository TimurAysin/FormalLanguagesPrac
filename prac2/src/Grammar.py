from Rule import Rule


class Grammar:
    def __init__(self, terminals, nonterminals, rules):
        if not isinstance(terminals, list):
            raise ValueError("Wrong type of terminals.")
        elif not isinstance(nonterminals, list):
            raise ValueError("Wrong type of nonterminals.")
        elif not isinstance(rules, list):
            raise ValueError("Wrong type of rules.")
        elif len(rules) > 0 and not isinstance(rules[0], Rule):
            raise ValueError("Wrong type of rules.")

        self.terminals = terminals
        self.nonterminals = nonterminals
        self.rules = rules
