import numpy as np
import matplotlib.pyplot as plt

#导入数据
x = np.array([1.0,2.0,3.0,4.0,5.0])
y = np.array([0,0,0,1.0,1.0])
size = x.size
#设置初始值
w = 0.1
b = 0.1
#构造拟合函数和代价函数
y1 = w*x+b
z = 1/(1+np.exp(-y1))
cost =-sum(y*np.log(z)+(1-y)*np.log(1-z))/size

#梯度下降法
a = 0.1
for i in range(1000):
    dw = sum(x*(z-y)*z)
    db = sum(z-y)
    temw = w-a*dw/size
    temb = b-a*db/size

    #更新参数和函数
    w=temw
    b=temb
    y1 = w * x + b
    z = 1 / (1 + np.exp(-y1))
    cost = -sum(y * np.log(z) + (1 - y) * np.log(1 - z)) / size
    print(w,b,cost)
    i+=1

plt.plot(x,y)
plt.plot(x,z)
plt.show()