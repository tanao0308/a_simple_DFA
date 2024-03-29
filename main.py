from dfa import DFA


dfa = DFA("regex")

while True:
    print(">>>", end=' ')
    str = input()

    if str[0] == 'R':
        str = str[1:]
        dfa = DFA(str)
        print("regex set.")
    elif str == "exit":
        print("bye.")
        break
    elif str == "draw dfa":
        print("dfa displaying.")
        dfa.draw()
    elif str == "draw nfa":
        print("nfa displaying.")
        dfa.nfa.draw()
    else:
        if dfa.match(str):
            print("Match.")
        else:
            print("Not match.")
