from __future__ import division
def arithmetic(x, y, operator):
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # 返回计算结果
if __name__ == '__main__':
    print(arithmetic(10,10,'-'))