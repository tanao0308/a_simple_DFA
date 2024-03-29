import networkx as nx
import matplotlib.pyplot as plt
from utils import *


class NFA:
    def __init__(self, regex):
        """
        NFA的构造函数
        K: 状态集合
        Sigma: 字母表集合[a-z, epsilon]
        f: 转移函数
        S: 起始状态集合
        Z: 正确结束状态集合
        :param regex: string类型的正则表达式，只涉及[a-z*.]
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
    
    def draw(self):
        G = nx.MultiDiGraph()

        for k, k_f in self.f.items():
            for sigma in self.Sigma:
                for k1 in k_f[sigma]:
                    G.add_edge(k, k1, tra=get_char(sigma))

        seed = 0
        pos = nx.spring_layout(G, seed=seed)
        nx.draw(G, pos=pos, node_size=0, node_shape='s', arrowstyle='-|>', arrowsize=15)
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', verticalalignment='top')
        nx.draw_networkx_edge_labels(G, pos, font_size=8, label_pos=0.3, verticalalignment='bottom')
        plt.show()

if __name__ == "__main__":
    nfa = NFA("a*b")
    nfa.draw()