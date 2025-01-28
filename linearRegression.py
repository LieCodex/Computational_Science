import matplotlib.pyplot as plt

def LinearRegression(feature_x, feature_y, x):
    n = len(feature_x)
    sum_xy = sum(feature_x[i] * feature_y[i] for i in range(n))
    sum_x = sum(feature_x)
    sum_y = sum(feature_y)
    sum_x_sqr = sum(pow(i, 2) for i in feature_x)

    b = (n * sum_xy - (sum_x * sum_y)) / (n * sum_x_sqr - pow(sum_x, 2))
    a = (sum_y - b * sum_x) / n

    y = a + b * x


    plt.scatter(feature_x, feature_y, color="red", label="Data Points")

    plt.scatter(x, y, color="Yellow", label="Predicted Y")

    regression_line = [a + b * xi for xi in feature_x]
    plt.plot(feature_x, regression_line, color="blue", label="Regression Line")
    plt.xlabel("Feature X")
    plt.ylabel("Feature Y")
    plt.title("Linear Regression")
    plt.legend()
    plt.show()
    

    return y

feature_x = [140, 155, 159, 179, 192, 200, 212]
feature_y = [60, 62, 67, 70, 71, 72, 75]
x = 192

# Call the function
predicted_y = LinearRegression(feature_x, feature_y, x)
print(f"Predicted y for x = {x} is: {predicted_y}")
    