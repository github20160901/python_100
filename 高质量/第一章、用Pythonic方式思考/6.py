# 在单次切片操作中，不要同时指定start、end、和stride

#使用-1能将以字节形式存储的字符串反转
x = 'abcdefg'
y = x[::-1]
print(y)
x = [1,2,3]
print(x[::-1])

print('#对于已编码为UTF-I的Unicode无效')   #实际有效？
w = 'abcdefg'
x = w.encode('utf-8')
y = x[::-1]
print(y)
print(y.decode('utf-8'))

print('#既有start,又有end,还有stride的切割操作，很让人费解')
print('#尽量stride为正数，且不带start或end索引的切割操作，尽量避免用负数做stride')
x = 'abcdefg'
print(x[1::2])
print(x[-2::-2])
print(x[-2:2:-2])

print('#如果确实要同时start/end/stride,可将这个操作拆解为两条赋值语句，一条做范围切割，一个进一步切割，或使用内置itertools模块的islice')
x = 'abcdefg'
y = x[::2]
print(y[1:-1])
