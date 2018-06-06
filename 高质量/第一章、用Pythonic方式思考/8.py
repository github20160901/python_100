#encoding:utf-8
#不要使用含有两个以上表达式的列表推导

#列表推导也支持多重循环，如把矩阵（包含列表的列表）简化成一维列表
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in matrix for x in row]
print(flat)

#根据输入列表来创建有两层深度的新列表
squared = [x**2  for row in matrix for x in row]
print(squared)
squared1 = [[x**2  for x in row] for row in matrix]
print(squared1)

#再增加一层,必须分成多行来写，更清楚，用普通的循环语句来实现，更清晰
mylists = [[[1,2],[3,4]],[[5,6],[7,8]]]

flat = [x for sublist1 in mylists
          for sublist2 in sublist1
          for x in sublist2]
print(flat)

flat = []
for sublist1 in mylists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
print (flat)

