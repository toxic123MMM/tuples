tuplex=(1,2,3,4,5,6,7,8,9,0)
print(tuplex)

tuplex=tuplex + (7,)
print(tuplex)

tuplex=(1,3,4,2,6,5,7,9,8,0)
_slice=tuplex[3:5]
print(_slice)

_slice=tuplex[:7]
print(_slice)

tuplex=(1,4,2,3,6,2,8,9,2)
print(tuplex.count(2))