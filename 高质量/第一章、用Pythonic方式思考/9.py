#使用生成器表达式来改写数据量较大的列表推导

#列表推导的弱点是：推导过程中，对于输入序列中的每个值来说，可能都要创建含一项元素的全新列表；输入数据非常多时，消耗大量内存，甚至程序崩溃
value = [len(x) for x in open('./1.py')]
print(value)

#如果文件特别大，需要用生成器表达式
va = (len(x) for x in open('./1.py'))
print(va)
print(next(va))
print(next(va))

#生成的迭代器还可用作另外一个生成器表达式的输入
roots = ((x,x**2) for x in va)
print(next(roots))
print(next(roots))
