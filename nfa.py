import numpy as np


class NFA:
    def __init__(self, regex):
        '''
        NFA的构造函数
        K: 状态集合
        Sigma: 字母表集合[a-z'']
        f: 转移数组
        S: 起始状态集合
        Z: 正确结束状态集合
        :param regex: string类型的正则表达式，只涉及[a-z*.]
        '''
        self.K = np.array(list(range(len(regex) + 1)), dtype=np.int64)
        self.Sigma = np.array(list(range(26 + 1)), dtype=np.int64)
        # self.Sigma = np.zeros([26], dtype=np.int64)
        self.f = np.zeros([len(self.K), 26], dtype=np.int64)
        self.S = np.array([0])
        self.Z = np.array([len(self.K) - 1])

        for i in range(len(regex)):
            for sigma in self.Sigma:
                self.f[i][sigma] = -1
            if 

        print(self.K)
        print(self.Sigma)
        print(self.f)
        print(self.S)
        print(self.Z)


if __name__ == "__main__":
    nfa = NFA("a*ab")
