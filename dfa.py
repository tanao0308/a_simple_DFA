from nfa import NFA
from utils import *


class DFA:
    def __init__(self, regex):
        '''
        NFA的构造函数
        K: 状态集合
        Sigma: 字母表集合[a-z]
        f: 转移函数
        S: 起始状态，非集合
        Z: 正确结束状态集合
        :param regex: string类型的正则表达式，只涉及[a-z*.]
        '''
        self.Sigma, self.num_sigma = get_Sigma('dfa')
        self.f, self.nfa = {}, NFA(regex)

        self.S, self.num_k = self.get_state(self.nfa.S, get_epsilon()), 1
        k = self.S
        self.init_f(k)
        self.Z = self.nfa.Z

    def init_f(self, k):
        if frozenset(k) in self.f:
            return
        self.num_k += 1
        self.f.update({frozenset(k): [None] * self.num_sigma})
        for sigma in self.Sigma:
            k2 = self.get_state(k, sigma)
            self.f[frozenset(k)][sigma] = k2
            self.init_f(k2)

    def get_state(self, S, sigma):
        T = set()
        if sigma == get_epsilon():
            T = S
        for k in S:
            T = T.union(self.dfs(k, sigma))
        return T

    def dfs(self, k, sigma):
        T = set()
        for k2 in self.nfa.f[k][sigma]:
            T = T.union(self.dfs(k2, get_epsilon()))
            T.add(k2)
        for k2 in self.nfa.f[k][get_epsilon()]:
            T2 = self.dfs(k2, sigma)
            if T2:
                T = T.union(T2)
        return T

    def match(self, str):
        P = self.S
        for c in str:
            P = self.f[frozenset(P)][get_sigma(c)]
            if P is None:
                return False
        if self.Z - P:
            return False
        else:
            return True
