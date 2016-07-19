# June 2016
import sys
def smallest_string(s):
    n = len(s)
    if n%4 != 0:
        return False
    count = n / 4
    seen = {}
    subs, tmp = '', ''
    for e in s:
        if e not in seen:
            seen[e] = 1
        else:
            seen[e] += 1
        if seen[e] > count:
            subs += tmp + e
            tmp = ''
        else:
            if subs != '':
                tmp += e
    return subs


# lines = sys.stdin.readlines()
val = smallest_string('ATAGATGA')
print val

# sys.stdout.write(str(val))
# sys.stdout.flush()

# print smallest_string('ATAT')
# print smallest_string('ATAC')
# print smallest_string('ATA')
