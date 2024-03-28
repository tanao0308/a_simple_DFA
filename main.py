from dfa import DFA

print("input regex>>>", end=' ')
regex = input()
dfa = DFA(regex)

while True:
    print("Input string>>>", end=' ')
    str = input()
    if dfa.match(str):
        print("Match.")
    else:
        print("Not match.")

# 'abb', 'a*.'
