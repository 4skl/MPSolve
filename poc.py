import nltk

# TODO : check if validate all the cases
# Define a grammar for base 2 number system
grammar_b2 = """
S -> Z | O | O S
Z -> "0"
O -> "1"
"""

# sca : S contains Z -> XMS = Z (multiplicative annihilator) [S contains Z]
# sci : S only O -> XMS = O (multiplicative identity) [S is only O]
#? S contains only X -> XMS = X ???
grammar_mami = """
sca -> O | O S
sci -> Z | O S | T S
"""

# Define the grammar for Pf in base 2 (Pf = {0,1} = B2 (P = 0))
grammar_b2_p = grammar_b2 + grammar_mami + """
M -> "*"

Cases for P -> P-1:

P = 0;
Z -> Z
O -> O

P = 1;
Osca -> Z
Osci-> O

P = 2;
Can't create a valid expression with P = 2, all numbers are described by P = 0 or P = 1
Textual proof:
In base 2, a number is either P0, which means it is a digit, or it is P1, which means it is either Osca or Osci (Since a number cannot start with a zero), which results in P0.
Osca and Osci define all numbers greater than P0.
Therefore, we have defined all possible numbers in base 2 using P0 and P1.
"""
# B2 P max = 2

# Define the grammar for base 3 number system
grammar_b3 = """
S -> Z | O | T | O S | T S
Z -> "0"
O -> "1"
T -> "2"
"""

# Define the grammar for Pf in base 3 (Pf = {0,1,2} = B3 (P = 0))
grammar_b3_p = grammar_b3 + grammar_mami + """
M -> "*"

Cases for P -> P-1:

P = 0; 
Z -> Z
O -> O
T -> T

P = 1;
Osca -> Z
Tsca -> Z
Osci -> O
Tsci -> T
sciTsci -> T

P = 2;
TTsci -> OO
TTTTsci -> OTO
sciTTTTsci -> OTO
None -> OT (Nothing gives OT cause OT is a prime number bigger than 2, the biggest digit in base 3)
None -> TO (Nothing gives TO cause TO is a prime number bigger than 2, the biggest digit in base 3)

P = 3;
TTTsci -> TT
sciTTTsci -> TT

P = 4;
Note :
A number described in P-1 can't be described in P, else this would means that P-1 = P which is a contradiction.
if we can't find P = 4, this means that every number in base 3 is defined by P = 0, P = 1, P = 2 or P = 3.
And that we can't find a prime decomposition of a number described by P = 2 or P = 3 that don't contains a prime bigger than 2.

"""
# B3 P max = 4

"""
Yes, I guess that I should be able to derive a rule based on `A number described in P-1 can't be described in P, else this would means that P-1 = P which is a contradiction.` to prove that there isn't any number in P = 4 and that all numbers are defined by lower P ?

GitHub Copilot

Yes, you can derive a rule based on the fact that the multiplicative persistence (P) of a number in base 3 is at most 3. This is because the maximum product of digits you can get in base 3 is 2 * 2 * 2 = 8, which is 22 in base 3 and has a multiplicative persistence of 2.

To prove that there are no numbers with a multiplicative persistence of 4 or higher, you would need to show that there are no combinations of digits that, when multiplied together, result in a number with a multiplicative persistence of 3 or higher.

Here's a possible approach:

Assume for contradiction that there is a number with a multiplicative persistence of 4.
This number must contain at least four 2s, because 2 * 2 * 2 * 2 = 16 is the only multiplication of four digits that results in a number with a multiplicative persistence of 3.
But 16 is 112 in base 3, which has a multiplicative persistence of 2, not 3.
Therefore, there are no numbers with a multiplicative persistence of 4 or higher.
This proves that all numbers in base 3 are defined by P = 0, P = 1, P = 2, or P = 3.
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