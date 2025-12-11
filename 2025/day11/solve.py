# Дан направленный граф.
# 1. Найти количество путей между вершинами 'you' и 'out'
# 2. Найти количество путей между вершинами 'srv' и 'out', проходящими через
# обе вершины 'fft' и 'dac'

from functools import cache
import util

class Graf:
    def __init__(self, net: dict[str, str]):
        self.net = net
    @cache
    def count_paths(self, source, dest):
        outs = self.net[source]
        res = 0
        for o in outs:
            if o == dest:
                res +=1
            elif o == 'out':
                continue
            else:
                res += self.count_paths(o, dest)

        return res


def solve1(net) -> int:
    gr = Graf(net)
    return gr.count_paths('you', 'out')

def solve2(net) -> int:
    gr = Graf(net)
    # Граф без циклов, поэтому будут пути либо 'fft' -> 'dac',
    # либо 'dac' ->'fft'.
    res1 = gr.count_paths('svr', 'fft') * \
           gr.count_paths('fft', 'dac') * \
           gr.count_paths('dac', 'out')
    res2 = gr.count_paths('svr', 'dac') * \
           gr.count_paths('dac', 'fft') * \
           gr.count_paths('fft', 'out')

    return res1 + res2

def load(fname):
    # aaa: you hhh
    lines = util.load_str_lines(fname)
    net = {}
    for  line in lines:
        source, dest = line.split(':')
        net[source] = dest.split()

    return net

sample_data = load('sample1.txt')
util.assert_equal(solve1(sample_data), 5, "Part 1 Sample")

data = load('input.txt')
util.assert_equal(solve1(data), 662, "Part 1")

sample_data = load('sample2.txt')
util.assert_equal(solve2(sample_data), 2, "Part 2 Sample")

util.assert_equal(solve2(data), 429399933071120, "Part 2")
