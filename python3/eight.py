#!/usr/bin/python3

output = []

s = [0,0,0,0,0,0,0,0]

table = [0x80, 0x40, 0x20, 0x10, 0x08, 0x04, 0x02, 0x01]

counter = 0

def f(n):
    return table[n]

def printf():
    global counter
    r = list(map(f, output))
    print("%3d: %02x %02x %02x %02x %02x %02x %02x %02x" % \
          (counter, r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))

    counter = counter + 1;

def eight():
    out_len = len(output)
    if(out_len == 8):
        printf()
        return
    s[out_len] = set([0, 1, 2, 3, 4, 5, 6, 7])

    i = 0
    while i < out_len:
        n = output[i]
        if n in s[out_len]:
            s[out_len].remove(output[i])
        n = output[i] + (out_len - i)
        if n in s[out_len]:
            s[out_len].remove(n)
        n = output[i] - (out_len - i)
        if n in s[out_len]:
            s[out_len].remove(n)
        i = i + 1;

    for one in s[out_len]:
        output.append(one)
        eight()
        output.pop()

    return
    
eight()
