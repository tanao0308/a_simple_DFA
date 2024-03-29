# a_simple_dfa

实现了一个[简单正则表达式](https://leetcode.cn/problems/regular-expression-matching/description/)匹配的DFA自动机

nfa.py实现了用正则表达式生成nfa

dfa.py实现了用nfa生成dfa

main.py对dfa进行了简单的使用

运行`python main.py`后输入以R开头的正则串表示设置模板正则串，输入全英文小写字母串表示检查是否匹配模板正则串，输入`draw nfa`和`draw dfa`表示可视化当前模板串的自动机