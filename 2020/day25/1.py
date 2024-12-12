# AoC 2020. Day 25: Combo Breaker
# Door key decryption
import util


def transform(subject_number: int, loop_size: int) -> int:
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value %= 20201227

    return value


def handshake(card_loop_size, door_loop_size):
    card_public_key = transform(7, card_loop_size)
    door_public_key = transform(7, door_loop_size)
    encryption_key1 = transform(door_public_key, card_loop_size)
    encryption_key2 = transform(card_public_key, door_loop_size)


def find_loop_size(card_public_key):
    value = 1
    loop_size = 0
    while True:
        value *= 7  # subject_number == 7
        value %= 20201227
        loop_size +=1
        if value == card_public_key:
            break
    return loop_size


def find_encryption_key(card_public_key, door_public_key):
    card_loop_size = find_loop_size(card_public_key)
    encryption_key = transform(door_public_key, card_loop_size)
    return encryption_key


card_public_key_test = 5764801
door_public_key_test = 17807724
encryption_key_test = 14897079

util.assert_equal(find_loop_size(card_public_key_test), 8)
util.assert_equal(find_loop_size(door_public_key_test), 11)
util.assert_equal(find_encryption_key(card_public_key_test, door_public_key_test), encryption_key_test)

print("Part 1.")
card_public_key, door_public_key = [9093927, 11001876]
util.assert_equal(find_encryption_key(card_public_key, door_public_key), 12227206)


