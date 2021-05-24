from collections import defaultdict
def check_eq(filename):
	with open(filename, 'r') as f:
		for line in f:
			words=defaultdict(list)
			flag=0
			items= line.strip().split(', ')
			if len(items) <2:
				x=items[0]
				y=' '
			else:
				x,y=items
			print()
			print(x,y)
			print(almost_equal(x,y))


def almost_equal(a, b):
    if a == b or (len(a) - len(b) > 1 or len(b) - len(a) > 1):
        return False
    if len(a) == len(b):
        quota_used = False
        i = 0
        while i < len(a):
            if a[i] != b[i]:
                if quota_used:
                    return False
                quota_used = True
            i += 1
        return True
    if len(a) < len(b):
        a, b = b, a
    i = 0 
    quota_used = False
    length = len(b)
    while i < length:
        if a[i] != b[i]:
            if quota_used:
                return False
            quota_used = True
            b = b[:i] + '_' + b[i:]
        i += 1
    if not quota_used:
        return True
    elif a[i] == b[i]:
        return True
    else:
        return False

check_eq('almost.txt')

print(almost_equal('xyz', 'xyc'))
print(almost_equal('xyz', 'xy'))
print(almost_equal('xyz', 'xz'))
print(almost_equal('xyz', 'yz'))
print(almost_equal('xyz', 'xyzz'))
print(almost_equal('xyz', 'xayz'))
print(almost_equal('x', ''))
print(almost_equal('xyz', 'xyz'))
print(almost_equal('xyz', 'xzy'))
print(almost_equal('xyz', 'xk'))
print(almost_equal('xyz', 'yzxt'))
