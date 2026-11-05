# ps6.py
# Completed by:
import csv
from typing import Callable
from math import ceil
from pathlib import Path

# Read a CSV file
# The first column is the fish species
# The second column is the weight of the fish (our y values)
# The rest of the columns are the x parameters (length1, length2, length3, height, width)
# Note that xs here will be a list of lists because each data point has multiple x values (that's why it's called a multivariate linear regression)
def readCSV(file_path: Path) -> tuple[list[list[float]], list[float]]:
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        xs = []
        ys = []
        for row in reader:
            x_list = []
            ys.append(float(row[1]))  # weight
            x_list.append(float(row[2]))  # length1
            x_list.append(float(row[3]))  # length2
            x_list.append(float(row[4]))  # length3
            x_list.append(float(row[5]))  # height
            x_list.append(float(row[6]))  # width
            xs.append(x_list)
            
        return (xs, ys)

# Find the mean of a list of numbers
def mean(xs: list[float]) -> float:
    return sum(xs) / len(xs)

# Find the covariance of two lists of numbers
def covariance(xs: list[float], ys: list[float]) -> float:
    x_mean = mean(xs)
    y_mean = mean(ys)
    return sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys)) / len(xs)

# Find the variance of a list of numbers
def variance(xs: list[float]) -> float:
    x_mean = mean(xs)
    return sum((x - x_mean) ** 2 for x in xs) / len(xs)

# Find the standard deviation of a list of numbers
def standard_deviation(xs: list[float]) -> float:
    return variance(xs) ** 0.5

# Find the y-value of a line of best fit at a given set of x-values
def predict(x: list[float], ys: list[float], theta: list[float]) -> float:
    return theta[0] + sum(theta[i + 1] * x[i] for i in range(len(x)))

# Find the r-squared value of a line of best fit
def r_squared(xs: list[list[float]], ys: list[float], theta: list[float]) -> float:
    y_mean = mean(ys)
    return 1 - sum((y - predict(x, ys, theta)) ** 2 for x, y in zip(xs, ys)) / sum((y - y_mean) ** 2 for y in ys)

# Normalize the values by subtracting the mean and dividing by the standard deviation
def normalize_xs(xs: list[list[float]]) -> list[list[float]]:
    m = len(xs[0])
    normalized_xs = []
    x_stds = []
    x_means = []
    for i in range(m):
        x = [x[i] for x in xs]
        x_means.append(mean(x))
        x_stds.append(standard_deviation(x))
    for x in xs:
        normalized_xs.append([(x[i] - x_means[i]) / x_stds[i] for i in range(m)])
    return normalized_xs

# Normalize the values by subtracting the mean and dividing by the standard deviation
def normalize_ys(ys: list[float]) -> list[float]:
    y_mean = mean(ys)
    y_std = standard_deviation(ys)
    return [(y - y_mean) / y_std for y in ys]

# Find the cost of a line of best fit for the multivariate linear regression
def cost(xs: list[list[float]], ys: list[float], theta: list[float]) -> float:
    m = len(xs[0])
    n = len(xs)
    return sum((theta[0] + sum(theta[i + 1] * x[i] for i in range(m)) - y) ** 2 for x, y in zip(xs, ys)) / 2*n

# Plot the costs of a line of best fit for the multivariate linear regression
# from gradient descent over time
# Requires matplotlib (pip or pip3 install matplotlib)
def plot_costs(costs: list[float]) -> None:
    import matplotlib.pyplot as plt
    plt.plot(range(len(costs)), costs)
    plt.show()

# Find the theta values for a line of best fit for the multivariate linear regression
# Returns theta values and costs over time
def gradient_descent(xs: list[list[float]], ys: list[float], theta: list[float], alpha: float = 0.000004, iterations: int = 100000, convergence: float = 0.1) -> tuple[list[float], list[float]]:
    m = len(xs[0])
    n = len(xs)
    costs = []
    for iteration in range(iterations):
        new_theta = [theta[0] + alpha * sum(y - predict(x, ys, theta) for x, y in zip(xs, ys))]
        for i in range(m):
            new_theta.append(theta[i + 1] + alpha * sum((y - (predict(x, ys, theta))) * x[i] for x, y in zip(xs, ys)))
        theta = new_theta
        costs.append(cost(xs, ys, theta))
        if iteration > 1 and abs(costs[-1] - costs[-2]) < convergence:
            print(f"Converged after {iteration} iterations")
            break
            
    return theta, costs

def starter_run():
    p = Path(__file__).with_name('Fish.csv')
    original_xs, original_ys = readCSV(p.absolute())
    # xs = normalize_xs(original_xs)
    # ys = normalize_ys(original_ys)
    xs = original_xs
    ys = original_ys
    initial_theta = [0.0] * (len(xs[0]) + 1)
    theta, costs = gradient_descent(xs, ys, initial_theta)
    print(f'y = {theta[0]} + {theta[1]}length1 + {theta[2]}length2 + {theta[3]}length3 + {theta[4]}height + {theta[5]}width')
    print(f'r-squared: {r_squared(xs, ys, theta)}')
    plot_costs(costs)

if __name__ == '__main__':
    starter_run()
