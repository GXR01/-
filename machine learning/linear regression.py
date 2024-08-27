import numpy as np

#导入数据
x = np.array([1,2,3,4,5])
y = np.array([2,3,4,5,6])
size = x.size
#设置初始值
w = 0.1
b = 0.1
#构造拟合函数和代价函数
y1 = w*x+b
#梯度下降法
a = 0.1
for i in range(100):
    dw = np.dot(y1-y,x)
    db = sum(y1-y)
    temw = w-a*dw/size
    temb = b-a*db/size
    w=temw
    b=temb
    y1 = w * x + b
    cost = sum(np.square(y1 - y))/(size * 2)
    print(w,b,cost)
    i+=1






