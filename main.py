from dfa import DFA

print("input regex>>>")
regex = input()
dfa = DFA(regex)

while True:
    print("Input string>>>")
    str = input()
    if dfa.match(str):
        print("Match.")
    else:
        print("Not match.")
