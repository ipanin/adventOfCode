# Даны координаты узлов в 3-мерном пространстве.
#
# 1. Соединить ближайшие узлы в порядке возрастания расстояния.
# Сделать N соединений. Какой размер у 3х самых больших сетей?
#
# 2. Соединить все узлы в порядке возрастания расстояний в единую сеть.
# Какие узлы были соеденены последними?
import util

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2

class SuperSet:
    def __init__(self, data: list[list[int]]):
        self.vcount = len(data)
        self.dist_list = []
        for i, v1 in enumerate(data):
            for j,v2 in enumerate(data[i+1:], i+1):
                d = dist(v1, v2)
                self.dist_list.append((d,i,j))

        self.dist_list.sort(key=lambda x: x[0])
        self.circuits: list[set[int]] = []

    def connect_n_near(self, nconnect):
        for _,i,j in self.dist_list[:nconnect]:
            self.connect(i,j)

    def connect_all(self):
        for _,i,j in self.dist_list:
            self.connect(i,j)
            if len(self.circuits) == 1 and len(self.circuits[0]) == self.vcount:
                return (i,j)

    def connect(self, i, j):
        ir = self.find_circuit(i)
        jr = self.find_circuit(j)

        if ir is None and jr is None:
            self.circuits.append(set([i,j]))
        elif ir == jr:
            return
        elif ir is None:
            jr.add(i)
        elif jr is None:
            ir.add(j)
        else:
            ir.update(jr)
            self.circuits.remove(jr)

    def find_circuit(self, i: int):
        for r in self.circuits:
            if i in r:
                return r
        return None

    def circuit_sizes(self):
        return [len(r) for r in self.circuits]

def solve1(data, nconnect) -> int:
    sset = SuperSet(data)
    sset.connect_n_near(nconnect)
    c = sorted(sset.circuit_sizes())
    return c[-1] * c[-2] * c[-3]

def solve2(data) -> int:
    sset = SuperSet(data)
    i1, i2 = sset.connect_all()
    return data[i1][0] * data[i2][0]


sample_data = util.load_int_lists('sample.txt')
util.assert_equal(solve1(sample_data, 10), 40, "Part 1 Sample")
util.assert_equal(solve2(sample_data), 25272, "Part 2 Sample")

data = util.load_int_lists('input.txt')
util.assert_equal(solve1(data, 1000), 129564, "Part 1")
util.assert_equal(solve2(data), 42047840, "Part 2")
