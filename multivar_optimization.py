import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

if __name__ == '__main__':
    # Define a cost function and its gradient
    def f(x): return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

    def fd(x): return np.array(
        [-2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0]**2), 200 * (x[1] - x[0]**2)])

    # Gradient Descent Implementation
    def gradient_descent(x_init, learning_rate, max_iter, min_tol, gradient_func):
        x = np.array(x_init)
        gd_xs = [x]

        for i in range(max_iter):
            xp = x.copy()
            grad = gradient_func(x)
            x = xp - learning_rate * grad
            gd_xs.append(x)

            # Check the terminal condition
            if np.linalg.norm(x - xp) < min_tol:
                break

        return np.array(gd_xs)

    # Define configuration
    x_init = [-1, 1]   # Please try other initial points
    learn_rate = 0.001  # Please try 0.01, 0.005, and 0.0001
    max_iter = 10000   # Please try 100, 1000, and 100000
    min_tol = 1e-6

    # Optimize the cost function using my gradient descent
    gd_xs = gradient_descent(x_init, learn_rate, max_iter, min_tol, fd)

    # Optimize the cost function using SciPy
    result = minimize(f, x_init, tol=min_tol, options={
                      'maxiter': max_iter, 'return_all': True})
    sp_xs = np.array(result.allvecs)

    # Visualize the results
    x_range = np.linspace(-2, 2, 100)
    y_range = np.linspace(-1, 3, 100)
    xx, yy = np.meshgrid(x_range, y_range)
    zz = f((xx, yy))
    plt.contourf(xx, yy, zz)
    plt.plot(gd_xs[:, 0], gd_xs[:, 1], 'r.', label=f'GD (iter={len(gd_xs)})')
    plt.plot(sp_xs[:, 0], sp_xs[:, 1], 'b.',
             label=f'SciPy (iter={len(sp_xs)})')
    plt.xlabel('$x_0$')
    plt.ylabel('$x_1$')
    plt.legend()
    plt.show()
