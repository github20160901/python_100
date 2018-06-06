class NaEr(Exception):
    def __init__(self):
        return 'This is Null'
try:
    s = None
    if s is None:    
        print ("s是空对象")
        raise NaEr
    #print (len(s))
except TypeError:
    print ("空对象没有长度")
