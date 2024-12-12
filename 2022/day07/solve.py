# Day 7: No Space Left On Device
# Восстановление структуры каталогов по логу командной оболочки
# Вычисление размера вложенных директорий

def parse_log(log):
    blocks = log.split("$ ")[1:]
    res = []
    for block in blocks:
        lines = block.strip().split('\n')
        command = lines[0]
        output = lines[1:]
        res.append((command, output))
    return res


def process(commands):
    dir_tree = {}
    cwd = ''
    for command, output in commands:
        match command.split():
            case ['cd', '/']:
                cwd = '/'
                dir_tree[cwd] = 0
            case ['cd', '..']:
                cwd = cwd[:-1]
                cwd = cwd[:cwd.rfind('/')+1]
                dir_tree[cwd] = 0
            case ['cd', dir_name]:
                cwd += dir_name + '/'
                dir_tree[cwd] = 0
            case ['ls']:
                for line in output:
                    match line.split():
                        case ['dir', dir_name]:
                            dir_tree[cwd + dir_name + '/'] = 0
                        case [size, fname]:
                            dir_tree[cwd + fname] = int(size)
                        case some:
                            raise RuntimeError(f"Unexpected output line: {some}")
            case some:
                raise RuntimeError(f"Unexpected command: {some}")
    return dir_tree

def dir_sizes(dir_tree):
    res = []
    for dir in dir_tree:
        if dir[-1] == '/':
            size = 0
            for file in dir_tree.keys():
                if file[-1] != '/' and file.startswith(dir):
                    size += dir_tree[file]
            res.append(size)
    return res


log = open("input.txt").read().rstrip()
commands = parse_log(log)
dir_tree = process(commands)
sizes = sorted(dir_sizes(dir_tree))

p1 = sum(s for s in sizes if s <= 100_000)
print("Part1", p1)  # 1390824

disk_total = 70_000_000
required = 30_000_000
free = disk_total - max(sizes)
freeup = required - free

p2 = min(s for s in sizes if s > freeup)
print("Part2", p2)  # 7490863
