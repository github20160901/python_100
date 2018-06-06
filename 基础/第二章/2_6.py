# 在文件的开头定义全局变量
_a = 1
_b = 2
def add():
    global _a
    _a = 3
    print(_a)
    print(_b)
    return "_a + _b =", _a + _b

def sub():
    global  _b
    _b = 4
    print(_a)
    print(_b)
    return "_a - _b =", _a - _b

print(_a)
print(_b)
print("#" * 10)
print (add())
print( sub())
print(_a)
print(_b)
