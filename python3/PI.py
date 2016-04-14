#!/usr/bin/python3

def main():
    sum = 0;
    i = 0
    while i < 100000000:
        sum += num_n(i)
        i += 1

    print(sum * 4)

def num_n(n):
    x = 2 * n + 1;
    q = 1
    if n % 2 == 1:
        q = -1
    return (q / x)

main()
