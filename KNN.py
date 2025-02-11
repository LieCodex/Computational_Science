def KNN(datas, guess):
    lowest = [0, 0, 0, float('inf')]
    for data in datas:
        data[3] = Euclidean_Distance(guess[0], data[0], guess[1], data[1])
    for data in datas:
        if data[3] < lowest[3]:
            lowest = data
    guess[2] = lowest[2]
    print(f"Guess Color: {guess[2]}")
    
        


def Euclidean_Distance(x1, y1, x2, y2): # this will calculate the distance between points
    first = (x1 - y1) ** 2 + (x2 - y2) **2 
    if first == 0:
        return 0
    last_guess= first/2.0
    while True:
        guess= (last_guess + first/last_guess)/2
        if abs(guess - last_guess) < .00000000001:
            return guess
        last_guess= guess



data = [
    [40, 20, "Red", 0],
    [50, 50, "Blue", 0],
    [60, 90, "Blue", 0],
    [10, 25, "Red", 0],
    [70, 70, "Blue", 0],
    [60, 10, "Red", 0],
    [25, 80, "Blue", 0]
]
guess = [20, 35, ""]

KNN(data, guess)
