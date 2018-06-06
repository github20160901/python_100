# 使用writelines()写文件
f = open("hello.txt", "w+")
li = ["hello world\n", "hello China\n"]
f.writelines(li)
f.close()  
