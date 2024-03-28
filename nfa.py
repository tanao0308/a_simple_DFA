from utils import *


class NFA:
    def __init__(self, regex):
        """
        NFA的构造函数
        K: 状态集合
        Sigma: 字母表集合[a-z'']
        f: 转移函数
        S: 起始状态集合
        Z: 正确结束状态集合
        :param regex: string类型的正则表达式，只涉及[0-9*.]
        """
        self.Sigma, self.num_sigma = get_Sigma()
        self.f = {}

        k, self.num_k = 0, 1
        for i in range(len(regex)):
            if regex[i] == '*':
                continue

            elif i + 1 < len(regex) and regex[i + 1] == '*':
                k0_f, k1_f = [set() for _ in self.Sigma], [set() for _ in self.Sigma]
                k0_f[get_epsilon()].add(k + 1)
                k1_f[get_epsilon()].add(k + 2)
                if regex[i] == '.':
                    for sigma in range(self.num_sigma - 1):
                        k1_f[sigma].add(k + 1)
                else:
                    k1_f[get_sigma(regex[i])].add(k + 1)
                self.f.update({k: k0_f})
                self.f.update({k + 1: k1_f})
                k += 2
                self.num_k += 2

            elif regex[i] == '.':
                k0_f = [set() for _ in range(self.num_sigma)]
                for sigma in range(self.num_sigma - 1):
                    k0_f[sigma].add(k + 1)
                self.f.update({k: k0_f})
                k += 1
                self.num_k += 1

            else:
                k0_f = [set() for _ in range(self.num_sigma)]
                k0_f[get_sigma(regex[i])].add(k + 1)
                self.f.update({k: k0_f})
                k += 1
                self.num_k += 1

        k0_f = [set() for _ in range(self.num_sigma)]
        self.f.update({k: k0_f})
        self.S, self.Z = {0}, {k}

        if __name__ == "__main__":
            print('Sigma:')
            print(self.Sigma)
            print('f:')
            for k, k_f in self.f.items():
                print(k, k_f)
            print('S:')
            print(self.S)
            print('Z:')
            print(self.Z)

    def tran(self, set_s, sigma):
        set_t = set()
        for k in set_s:
            set_t.union(self.f[k][sigma])
        return set_t


if __name__ == "__main__":
    nfa = NFA("0*01")
