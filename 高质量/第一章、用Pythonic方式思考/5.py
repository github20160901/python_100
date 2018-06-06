# 切割序列的方法

a = [1,2,3,4,5,6,7]
#如果start为0或者end为索引为序列长度时，留空。
print('first four： ',a[:4])
print(a[3:])

#切割列表时，即使start或end越界不会报错，可以利用这一特性
print(a[20:])
print(a[:100])
#print(a[20])   #会报错

print ('#'*20)
#对list赋值时，如果使用切片操作，就会把原列表中处于相关范围的值替换成新值，即使它们的长度不同依然替换
b = a[4:]
print('before: ' ,b)
b[1] = 99
print ('after： ',b)
print ('nochange:  ',a)

