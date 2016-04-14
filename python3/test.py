#!/usr/bin/python3

i = [1];
j = 4;
def move(n, a, b, c):
    if(n == 0):return
    move(n-1, a, c, b)
    print(i, ':', a, '-->', c)
    i = i + 1;
    move(n-1, b, a, c)
    return

move(10, 'A', 'B', 'C')
'''
def test():
    i[0] = 9;
    j = 6;

test();

print(i, j)
'''
