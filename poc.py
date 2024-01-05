import nltk

# Define a grammar for base 2 number system
grammar_b2 = """
S -> Z | O | O S
Z -> "0"
O -> "1"
"""

# Define the grammar for Pf in base 2 (Pf = {0,1} = B2)
grammar_b2_p = grammar_b2 + """
M -> "*"

Cases for P:
P = 0; Pf = 0
ZMS -> Z

P = 1; Pf = 0
OMS -> Z if S contains at least one Z

P = 1; Pf = 1
OMS -> O if S is only O
"""

# Define the grammar for base 3 number system
grammar_b3 = """
S -> Z | O | T | O S | T S
Z -> "0"
O -> "1"
T -> "2"
"""

# Define the grammar for Pf in base 3 (Pf = {0,1,2} = B3)
grammar_b3_p = grammar_b3 + """
M -> "*"

Cases for P:
P = 0; Pf = 0
ZMS -> Z

P = 1; Pf = 0
OMS -> Z if S contains at least one Z

P = 1; Pf = 1
OMS -> O if S is only O

P = 2; Pf = 0
TMS -> Z if S contains at least one Z

P = 2; Pf = 1
TMS -> O if S is only O

P = 2; Pf = 2  # This is the only case where Pf = P, proving that B3 is not a Pf
TMS -> T if S is only T ??
"""

grammar = nltk.CFG.fromstring(grammar_b2)
parser = nltk.ChartParser(grammar)

# Define the target expression
target_expression = "101" # 5 in base 2

# Generate candidate expressions
def generate_sentences(grammar, start_symbol=nltk.Nonterminal('S'), depth=0, max_depth=10):
    if depth > max_depth:  # prevent infinite recursion
        return

    # iterate over all productions for the given start symbol
    for production in grammar.productions(lhs=start_symbol):
        rhs = production.rhs()

        # if rhs is a single terminal symbol, yield it
        if len(rhs) == 1 and isinstance(rhs[0], str):
            yield rhs[0]

        # if rhs is a single nonterminal symbol, recursively generate sentences for it
        elif len(rhs) == 1:
            for sentence in generate_sentences(grammar, rhs[0], depth + 1, max_depth):
                yield sentence

        # if rhs has multiple symbols, generate sentences for each and combine them
        else:
            for sentence1 in generate_sentences(grammar, rhs[0], depth + 1, max_depth):
                for sentence2 in generate_sentences(grammar, rhs[1], depth + 1, max_depth):
                    yield sentence1 + sentence2

# Generate and print all sentences up to length 4
i = 0
for sentence in generate_sentences(grammar, max_depth=4):
    print(i, sentence)
    i += 1