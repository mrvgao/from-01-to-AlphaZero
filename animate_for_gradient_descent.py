
from sklearn.datasets import load_boston
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

data = load_boston()['data']

RM = data[:, 5]
PRICE = load_boston()['target']


best_loss = float('inf')
_k, _b = np.random.uniform(-100, 100, size=(1, 2))[0]

def partial_k(k, b, ytrue, x):
    return 2 * np.mean((k * x + b - ytrue) * x)

def partial_b(k, b, ytrue, x):
    return 2  * np.mean(k * x + b - ytrue)


def price(x, k, b):
    return k * x + b

def loss(predict, true):
    return np.mean((predict - true) ** 2)

def once_test(i):
    #rk, rb = 
    global best_loss, _k, _b

    p_k, p_b = partial_k(_k, _b, PRICE, RM), partial_b(_k, _b, PRICE, RM)
    
    _k = _k + -1 * p_k * 1e-4
    _b = _b + -1 * p_b * 1e-4
    
    predict = price(RM, _k, _b)
    current_loss = loss(predict, PRICE)
    
    
    if current_loss < best_loss:
        best_loss = current_loss
        best_k, best_b = _k, _b

        
        print(f"best_loss = {best_loss}")

        plt.clf()
        plt.scatter(RM, PRICE)
        plt.plot(RM, price(RM, best_k, best_b), color='r')
        plt.title(f"loss = {best_loss}")


fig = plt.gcf()
ani = FuncAnimation(fig, once_test, interval=10)
plt.show()
