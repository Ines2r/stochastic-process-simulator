import numpy as np
import matplotlib.pyplot as plt

def dx(a, b, dt):
    return a*dt + b*np.random.normal(0,1)*np.sqrt(dt)

def X(N, X0, a, b, dt):
    X_values = [X0]
    for i in range(0,N):
        change = dx(a, b, dt)
        X_values.append(X_values[i] + change)
    return X_values

plt.figure(figsize=(10,5))
plt.plot(X(1000, 50, 20, 100, 1))
plt.plot(X(1000, 50, 20, 300, 1))
plt.show()

def X(N, X0,dt):
    X_values = [X0]
    for i in range(0,N):
        change = dx(np.cos(2*np.pi*i/N), 3*i**2, dt)
        X_values.append(X_values[i] + change)
    return X_values

plt.figure(figsize=(10,5))
for _ in range(0,10):
    plt.plot(X(1000, 50, 1))
plt.show()