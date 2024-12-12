# Day 16: Packet Decoder
# Декодируем поток битов как набор вложенных пакетов, описывающих арифметические и логические операции.

import util
import math
from bitstring import Bits

class Packet:
    def init(self):
        self.ver = 0
        self.typeId = 0
        self.size = 0
        self.value = 0

def test1(data, expected):
    result = solve1(data)
    print("Part 1.", result)
    util.assert_equal(result, expected)

def test2(data, expected):
    result = solve2(data)
    print("Part 2.", result)
    util.assert_equal(result, expected)

def solve1(data):
    bits = Bits(hex = data)
    packets = get_all_packets(bits)
    return sum(p.ver for p in packets)

def solve2(data):
    bits = Bits(hex = data)
    res = parse(bits)
    return res.value

def get_all_packets(bits : Bits):
    res = []
    p = Packet()
    p.ver = Bits(bits[:3]).uint
    p.typeId = Bits(bits[3:6]).uint

    pos = 6
    if p.typeId == 4: # literal
        while bits[pos] == 1:
            pos += 5
        pos += 5
        p.size = pos
        res.append(p)
    else:
        lengthTypeId = bits[pos]
        pos+=1
        if lengthTypeId:
            numOfSubpack = Bits(bits[pos:pos+11]).uint
            pos += 11
            for i in range(numOfSubpack):
                subp = get_all_packets(Bits(bits[pos:]))
                res.extend(subp)
                pos += subp[-1].size
        else:
            lenOfSubpack = Bits(bits[pos:pos+15]).uint
            pos += 15
            start = pos
            while pos < start + lenOfSubpack:
                subp = get_all_packets(Bits(bits[pos:]))
                res.extend(subp)
                pos += subp[-1].size
        p.size = pos
        res.append(p)

    return res

def parse(bits : Bits):
    p = Packet()
    #p.ver = Bits(bits[:3]).uint
    p.typeId = Bits(bits[3:6]).uint

    pos = 6
    if p.typeId == 4: # literal
        b = Bits()
        # binary number is padded with leading zeroes until its length is a multiple of four bits, 
        # and then it is broken into groups of four bits. 
        # Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit
        while True:
            last = bits[pos] == 0
            b += bits[pos+1:pos+5]
            pos += 5
            if last:
                break
        
        p.size = pos
        p.value = b.uint
        return p

    # parse operator with arguments
    args = []
    lengthTypeId = bits[pos]
    pos+=1
    if lengthTypeId: 
        # next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
        numOfSubpack = Bits(bits[pos:pos+11]).uint
        pos += 11
        
        for i in range(numOfSubpack):
            subp = parse(Bits(bits[pos:]))
            args.append(subp.value)
            pos += subp.size
    else: 
        # next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
        lenOfSubpack = Bits(bits[pos:pos+15]).uint
        pos += 15
        
        start = pos
        while pos < start + lenOfSubpack:
            subp = parse(Bits(bits[pos:]))
            args.append(subp.value)
            pos += subp.size
    
    p.size = pos
    p.value = calc_expr(p.typeId, args)
    return p

def calc_expr(op, args):
    '''
        Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
        Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
    ß    Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
        Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
        Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. 
            These packets always have exactly two sub-packets.
        Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. 
            These packets always have exactly two sub-packets.
        Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. 
            These packets always have exactly two sub-packets.
    '''    

    match op:
        case 0: return sum(args)
        case 1: return math.prod(args)
        case 2: return min(args)
        case 3: return max(args)
        case 5: return 1 if args[0] > args[1] else 0
        case 6: return 1 if args[0] < args[1] else 0
        case 7: return 1 if args[0] == args[1] else 0

def load_bit_string(fname):
    with open(util.full_name(fname), 'rt') as f:
        line = f.readline().rstrip()
        return line #[item for item in line]

test1("8A004A801A8002F478", 16)
test1("620080001611562C8802118E34", 12)
test1("C0015000016115A2E0802F182340", 23)
test1("A0016C880162017C3686B18A3D4780", 31)

data = load_bit_string("input.txt")
test1(data, 1002)


test2("C200B40A82", 3)     # finds the sum of 1 and 2
test2("04005AC33890", 54)  # finds the product of 6 and 9
test2("880086C3E88112", 7) # finds the minimum of 7, 8, and 9
test2("CE00C43D881120", 9) # finds the maximum of 7, 8, and 9
test2("D8005AC2A8F0", 1) # because 5 is less than 15.
test2("F600BC2D8F", 0)   # because 5 is not greater than 15.
test2("9C005AC2F8F0", 0) # because 5 is not equal to 15.
test2("9C0141080250320F1802104A08", 1) # produces 1, because 1 + 3 = 2 * 2.

test2(data, 0)