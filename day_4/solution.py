# http://adventofcode.com/day/4

import hashlib

def check_string(num=5):
    with open('input.txt') as f:
        key = f.read().strip()
        answer = None

        i = 1

        while not answer:
            test_string = "{}{}".format(key, i)
            hash_obj = hashlib.md5(test_string.encode('utf-8'))
            hex_string = hash_obj.hexdigest()

            if hex_string.startswith('0' * num):
                print("Hex String: {}".format(hex_string))
                answer = i
            i += 1

        print("Answer for {num} zeroes: {ans}".format(num=num, ans=answer))

check_string()

check_string(num=6)
