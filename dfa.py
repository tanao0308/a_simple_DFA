from nfa import NFA
from utils import *

class DFA:
    def __init__(self, regex):
        '''
        NFA的构造函数
        K: 状态集合
        Sigma: 字母表集合[a-z'']
        f: 转移函数
        S: 起始状态，非集合
        Z: 正确结束状态集合
        :param regex: string类型的正则表达式，只涉及[0-9*.]
        '''
        self.num_k, self.num_sigma = 0, 10+1
        self.Sigma = np.array(list(range(self.num_sigma)), dtype=np.int64)
        nfa = NFA(regex)

        k = nfa.S
        self.num_k += 1
        while True:
            for sigma in self.Sigma:
                pass

    def match(self, str):
        P = self.S
        for c in str:
            P = self.f[P][get_sigma(c)]
            if not P:
                return False
        P = self.f[P][get_epsilon()]
        if P in self.Z:
            return True
        else:
            return False



