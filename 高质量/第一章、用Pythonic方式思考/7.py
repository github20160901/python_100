#用列表推导来取代map和filter

#用列表中的每个元素的平方值构建另一份列表
a = [1,2,3,4,5]
squares = [x**2 for x in a]
print(squares)

squares = map(lambda x:x**2,a)
print(list(squares))
#除非是调用只有一个参数的函数，否则，对于简单情况，列表推导比内置的map函数更清晰

#列表推导可以跳过输入列表的某些元素，如果改用map，必须辅以filter方能实现
even_squares= [x**2 for x in a if x%2 ==0]
print (even_squares)

alt = map(lambda x:x**2,filter(lambda x:x % 2 ==0,a))
assert even_squares == list(alt)