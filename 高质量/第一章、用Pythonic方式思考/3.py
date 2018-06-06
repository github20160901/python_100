print('''#了解bytes,str与unicode的区别

#Python3有两种表示字符序列的类型，bytes和str，前者的实例包含原始的8位值，后者实例包含Unicodez字符
#Python2有两种表示字符序列的类型，str和unicode，前者实例包含原始的8位值，后者包含Unicode字符

#要想把Unicode字符转换成二进制数据，就必须用encode方法，想把二进制数据转换成Unicode，必须用decode方法。

#编写程序时，一定把编码或解码的操作放在界面的最外围来做（开头？）

#python3中，接受str或bytes,并总是返回str
''')
def to_str(bytes_or_str):
    if isinstance(bytes_or_str,bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value
#Python3中，接受str或tytes，返回bytes的方法
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str,str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

#Python2中，接受str或unicode,并返回unicode方法：
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str,str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value
#接受str或Unicode，并返回unicode的方法
def to_str(unicode_or_str):
    if isinstance(unicode_or_str,str):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value

import os

with open('.',\a.txt'w') as f:
    f.write(os.urandom(10))

with open('.\a.txt','wb') as f:
    f.write(os.urandom(10))

