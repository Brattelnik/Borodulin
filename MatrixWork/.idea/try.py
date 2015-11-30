__author__ = 'student'
def _max(*args):
    m = args[0]
    for x in args[1:]:
        if x > m:
            m = x
    return m
a=1
b=2
c=3
print(max(a,b,c))