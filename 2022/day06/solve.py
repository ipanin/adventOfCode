# Day 6: Tuning Trouble
# Поиск первой подстроки длины N со всеми различающимися символами.

#line = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
#line = 'nppdvjthqldpwncqszvftbrmjlhg'
#line = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
line = open("input.txt").read().rstrip()

# решение без использования set
def solve(data, packet_len):
    packet = []
    pos = 0
    while len(packet) < packet_len:
        ch = data[pos]  # выход за границу будет означать, что пакет не найден
        if ch in packet:
            pos -= len(packet) - 1
            packet = []
        else:
            packet += ch
            pos += 1
    return pos

print("Part1", solve(line, 4)) # 1757
print("Part2", solve(line, 14)) # 2950

# one-liner from reddit:
# print([[i for i in range(n, len(line)) if len(set(line[i-n:i])) == n][0] for n in [4, 14]])
